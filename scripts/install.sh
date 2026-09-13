#!/bin/bash
# Python-free installer. Uses Bash 3.2 syntax and macOS/BSD-compatible utilities.
set -eo pipefail
export LC_ALL=C
shopt -s nullglob dotglob

COLLECTION=awesomelon/codex-skills
MARKER=.codex-skills-install.v2
LEGACY_MARKER=.codex-skills-install.json

fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }

usage() {
    cat <<'USAGE'
Usage: bash scripts/install.sh [options]
  --dest PATH       Destination (default: ~/.agents/skills)
  --mode link|copy  Symlinks by default; independent managed copies on request
  --skill NAME      Select a skill; repeatable (default: all)
  --dry-run         Show the plan without writing files
  --list            List available skills
  -h, --help        Show this help
Existing foreign links, unmanaged directories, and locally edited copies are preserved.
USAGE
}

# Resolve existing symlink ancestors without GNU realpath/readlink -f or mkdir.
# Process '..' after resolving its preceding component, as filesystem lookup does.
canonical_directory() {
    local rest=$1 current=/ part
    case "$rest" in
        '~') rest=$HOME ;;
        '~/'*) rest=$HOME/${rest#\~/} ;;
    esac
    case "$rest" in /*) ;; *) rest=$PWD/$rest ;; esac
    while [[ -n "$rest" ]]; do
        part=${rest%%/*}
        if [[ "$rest" == */* ]]; then rest=${rest#*/}; else rest=; fi
        case "$part" in
            ''|.) continue ;;
            ..) current=${current%/*}; current=${current:-/}; continue ;;
        esac
        current=${current%/}/$part
        if [[ -d "$current" ]]; then
            current=$(cd -P -- "$current" && printf '%s/.' "$PWD") || return 1
            current=${current%/.}
            if [[ "$current" == *$'\n'* ]]; then
                printf 'ERROR: Destination paths must not contain newlines\n' >&2
                return 1
            fi
        elif [[ -e "$current" || -L "$current" ]]; then
            printf 'ERROR: Not a usable destination directory: %s\n' "$current" >&2
            return 1
        fi
    done
    printf '%s\n' "$current"
}

digest_file() {
    local result
    result=$(shasum -a 256 < "$1") || return 1
    printf '%s\n' "${result%% *}"
}

# Globs are sorted in the C locale. NUL-separated records preserve spaces,
# Unicode, newlines, and directory names; empty directories are included.
tree_records() {
    local folder=$1 prefix=$2 item name relative digest
    [[ -r "$folder" && -x "$folder" ]] || return 1
    for item in "$folder"/*; do
        name=${item##*/}
        relative=$prefix$name
        if [[ -L "$item" ]]; then
            printf 'ERROR: Symlinks inside a skill are not supported: %s\n' "$item" >&2
            return 1
        fi
        if [[ -z "$prefix" && "$name" == "$MARKER" ]]; then
            [[ -f "$item" ]] || return 1
            continue
        fi
        if [[ -d "$item" ]]; then
            printf 'd\0%s\0' "$relative" || return 1
            tree_records "$item" "$relative/" || return 1
        elif [[ -f "$item" ]]; then
            digest=$(digest_file "$item") || return 1
            printf 'f\0%s\0%s\0' "$relative" "$digest" || return 1
        else
            printf 'ERROR: Not a regular skill file: %s\n' "$item" >&2
            return 1
        fi
    done
}

fingerprint() {
    local result
    [[ -d "$1" && ! -L "$1" ]] || return 1
    result=$(tree_records "$1" '' | shasum -a 256) || return 1
    printf '%s\n' "${result%% *}"
}

marker_text() { printf 'version=2\ncollection=%s\nskill=%s\nsha256=%s\n' "$COLLECTION" "$1" "$2"; }

# Sets ACTION and INSTALLED_HASH; never mutates the destination.
disposition() {
    local source=$1 target=$2 source_hash=$3 resolved actual recorded expected
    ACTION=install
    INSTALLED_HASH=
    if [[ -L "$target" ]]; then
        if [[ "$mode" == link && -d "$target" ]]; then
            resolved=$(cd -P -- "$target" && printf '%s/.' "$PWD") || return 1
            resolved=${resolved%/.}
            if [[ "$resolved" == "$source" ]]; then ACTION=unchanged; return 0; fi
        fi
        printf 'ERROR: Existing link preserved: %s\n' "$target" >&2
        return 1
    fi
    [[ -e "$target" ]] || return 0
    if [[ "$mode" != copy || ! -d "$target" ]]; then
        printf 'ERROR: Existing path preserved: %s\n' "$target" >&2
        return 1
    fi
    if [[ -e "$target/$LEGACY_MARKER" || -L "$target/$LEGACY_MARKER" ]]; then
        printf 'ERROR: Legacy Python copy preserved: %s. Back it up outside the skills directory and merge any edits before a fresh shell installation.\n' "$target" >&2
        return 1
    fi
    if [[ ! -f "$target/$MARKER" || -L "$target/$MARKER" ]]; then
        printf 'ERROR: Unmanaged copy preserved: %s\n' "$target" >&2
        return 1
    fi
    actual=$(fingerprint "$target") || return 1
    recorded=$(cat "$target/$MARKER") || return 1
    expected=$(marker_text "${source##*/}" "$actual") || return 1
    if [[ "$recorded" != "$expected" ]]; then
        printf 'ERROR: Locally edited copy or invalid metadata; preserved: %s\n' "$target" >&2
        return 1
    fi
    INSTALLED_HASH=$actual
    ACTION=update
    [[ "$actual" != "$source_hash" ]] || ACTION=unchanged
    return 0
}

copy_skill() (
    local source=$1 target=$2 source_hash=$3 temporary staging backup staged_hash old_hash status
    # Keep backups outside the skill discovery directory, on its parent volume.
    temporary=$(mktemp -d "${destination%/*}/.codex-skills.XXXXXX") || exit 1
    staging=$temporary/staging
    backup=$temporary/backup
    cleanup() {
        status=$?
        trap - EXIT HUP INT TERM
        if [[ -e "$backup" ]]; then
            if [[ ! -e "$target" && ! -L "$target" ]] && mv "$backup" "$target"; then
                printf 'Restored previous copy: %s\n' "$target" >&2
            else
                printf 'ERROR: Previous copy preserved at %s\n' "$backup" >&2
                status=1
            fi
        fi
        if [[ ! -e "$backup" ]]; then rm -rf "$temporary" || status=1; fi
        exit "$status"
    }
    trap cleanup EXIT
    trap 'exit 129' HUP
    trap 'exit 130' INT
    trap 'exit 143' TERM

    cp -pR "$source" "$staging" || exit 1
    staged_hash=$(fingerprint "$staging") || exit 1
    [[ "$staged_hash" == "$source_hash" ]] || fail "Source changed while copying: $source"
    marker_text "${source##*/}" "$staged_hash" > "$staging/$MARKER" || exit 1
    disposition "$source" "$target" "$source_hash" || exit 1
    [[ "$ACTION" != unchanged ]] || exit 0
    old_hash=$INSTALLED_HASH
    if [[ -e "$target" ]]; then mv "$target" "$backup" || exit 1; fi
    mv "$staging" "$target" || exit 1
    if [[ -e "$backup" ]]; then
        # A late edit to the old copy must not be silently discarded.
        [[ $(fingerprint "$backup") == "$old_hash" ]] || fail "Previous copy changed during installation"
        rm -rf "$backup" || exit 1
    fi
)

[[ ! -L "${BASH_SOURCE[0]}" ]] || fail 'Run the installer from its checkout, not through a script symlink'
ROOT=$(cd -P -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && printf '%s/.' "$PWD")
ROOT=${ROOT%/.}
destination=$HOME/.agents/skills
mode=link
dry_run=false
list=false
requested=()
while [[ $# -gt 0 ]]; do
    case "$1" in
        --dest|--mode|--skill)
            [[ $# -ge 2 && -n "$2" ]] || fail "Missing value for $1"
            case "$1" in
                --dest) destination=$2 ;;
                --mode) mode=$2 ;;
                --skill) requested+=("$2") ;;
            esac
            shift 2 ;;
        --dry-run) dry_run=true; shift ;;
        --list) list=true; shift ;;
        -h|--help) usage; exit 0 ;;
        *) fail "Unknown option: $1" ;;
    esac
done
[[ "$mode" == link || "$mode" == copy ]] || fail '--mode must be link or copy'
command -v shasum >/dev/null || fail 'Required macOS utility not found: shasum'
[[ -d "$ROOT/skills" && ! -L "$ROOT/skills" ]] || fail 'Missing or symlinked skills source directory'

names=()
hashes=()
for source in "$ROOT/skills"/*; do
    name=${source##*/}
    [[ "$name" != .* ]] || continue
    [[ "$name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ && ${#name} -le 64 ]] || fail "Invalid skill name: $name"
    [[ -d "$source" && ! -L "$source" && -f "$source/SKILL.md" ]] || fail "Invalid skill directory: $source"
    for marker in "$MARKER" "$LEGACY_MARKER"; do
        [[ ! -e "$source/$marker" && ! -L "$source/$marker" ]] || fail "Installation metadata in source: $source/$marker"
    done
    hash=$(fingerprint "$source") || fail "Cannot inspect skill: $source"
    names+=("$name")
    hashes+=("$hash")
done
[[ ${#names[@]} -gt 0 ]] || fail 'No skills found'
if $list; then printf '%s\n' "${names[@]}"; exit 0; fi

selected=()
if [[ ${#requested[@]} -eq 0 ]]; then requested=("${names[@]}"); fi
for name in "${requested[@]}"; do
    found=false
    for ((i=0; i<${#names[@]}; i++)); do
        [[ "$name" == "${names[i]}" ]] || continue
        found=true
        duplicate=false
        for index in "${selected[@]}"; do [[ "$index" != "$i" ]] || duplicate=true; done
        if ! $duplicate; then selected+=("$i"); fi
        break
    done
    $found || fail "Unknown skill: $name"
done

# Command substitution cannot faithfully retain trailing newline path names.
[[ "$destination" != *$'\n'* && "$ROOT" != *$'\n'* ]] || fail 'Checkout and destination paths must not contain newlines'
destination=$(canonical_directory "$destination") || exit 1
case "$destination/" in "$ROOT/"*) fail 'Installation destination must be outside the source repository' ;; esac
actions=()
for i in "${selected[@]}"; do
    source=$ROOT/skills/${names[i]}
    target=${destination%/}/${names[i]}
    case "$ROOT/" in "$target/"*) fail "Destination overlaps source checkout: $target" ;; esac
    disposition "$source" "$target" "${hashes[i]}" || exit 1
    actions+=("$ACTION")
done

# Preflight every selected target before creating any destination.
for ((j=0; j<${#selected[@]}; j++)); do
    i=${selected[j]}
    source=$ROOT/skills/${names[i]}
    target=${destination%/}/${names[i]}
    prefix=
    if $dry_run; then prefix='DRY RUN '; fi
    printf '%s%s: %s (%s)\n' "$prefix" "${actions[j]}" "$target" "$mode"
    if $dry_run || [[ "${actions[j]}" == unchanged ]]; then continue; fi
    mkdir -p "$destination"
    if [[ "$mode" == link ]]; then
        disposition "$source" "$target" "${hashes[i]}" || exit 1
        if [[ "$ACTION" != unchanged ]]; then ln -s "$source" "$target"; fi
    else
        copy_skill "$source" "$target" "${hashes[i]}"
    fi
done
if ! $dry_run; then printf 'Installation complete.\n'; fi
