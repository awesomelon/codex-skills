# codex-skills

개인 Codex 스킬을 한 저장소에 모으고, 여러 Mac에 필요한 스킬을 설치·업데이트하기 위한 모음입니다. 사용 환경은 macOS입니다.

GitHub 저장소: [awesomelon/codex-skills](https://github.com/awesomelon/codex-skills).

## 포함된 스킬

| 스킬 | 용도 |
| --- | --- |
| [architecture-guard](skills/architecture-guard/SKILL.md) | 모듈 경계·의존성·상태 소유권·공개 계약을 검토합니다. 설계와 리뷰 단계에 필요한 기준을 선택합니다. |
| [react-quality-guard](skills/react-quality-guard/SKILL.md) | Vercel 기준으로 React 웹 코드의 정확성·성능을 개선합니다. 쟁점에 맞는 상태·요청·렌더링·서버 기준만 적용합니다. |
| [code-quality-guard](skills/code-quality-guard/SKILL.md) | 정확성 검증과 유지보수 품질을 분리합니다. 변경 전후 지표·코드 근거·현실적인 변경 비용으로 검사하고, 요청 시 최소 개선과 검증을 수행합니다. |

`architecture-guard`는 모듈 경계, `react-quality-guard`는 React 실행 방식과 사용자 동작, `code-quality-guard`는 언어·프레임워크 공통의 유지보수 품질 평가에 집중합니다. 각 스킬은 단독 설치로 사용할 수 있습니다. 여러 관점이 필요한 작업은 이미 확보한 근거를 재사용하며, 매번 세 스킬을 함께 호출할 필요는 없습니다. 소규모 품질 리뷰는 본문의 근거로 판단합니다. 전후·A/B 비교, 점수 평가, 특수 지표 계산은 요청에 맞는 참조만 선택합니다. React 리뷰만 원하면 `$react-quality-guard로 현재 변경을 리뷰만 해줘`, 수정까지 원하면 `$react-quality-guard로 React 코드 품질을 개선하고 검증해줘`라고 요청합니다.

공통 품질 검사는 다음처럼 요청합니다.

```text
$code-quality-guard로 현재 변경의 정확성과 유지보수 품질을 분리해 검사해줘. 근거와 최소 개선안을 제시하고 파일은 수정하지 마.

$code-quality-guard로 이 모듈의 유지보수 품질을 개선하고 검증해줘. 현재 상태를 기준으로 동작 보존과 변경 비용의 차이를 확인해줘.
```

테스트 통과, 복잡도·중복 같은 진단 신호, 실제 유지보수 판단을 별도로 보고합니다. 분석 도구가 없는 수치는 미측정으로 남기며, 단일 점수나 LOC 감소를 목표로 삼지 않습니다. [비교·측정 기준](skills/code-quality-guard/references/measurement.md), [점수 평가](skills/code-quality-guard/references/scoring.md), [Earendil 원문 지표](skills/code-quality-guard/references/earendil-metrics.md), [품질 검사 평가 사례](evals/code-quality-guard/cases.md), [실행 기록](evals/code-quality-guard/results.md)을 참고하세요. 설치기는 새 폴더를 자동 발견하므로 업데이트 후 `bash scripts/install.sh --skill code-quality-guard`로 선택 설치할 수 있습니다.

원문 출처·기준 커밋·적용 예외는 [React 스킬 출처](skills/react-quality-guard/references/sources.md), 행동 평가 범위는 [React 평가 기록](evals/react-quality-guard/results.md)에 있습니다.

2026-09-12의 [스킬 감사와 개선 기록](docs/skill-audit-2026-09-12.md)에서 중복 지침 정리, 조건부 문서·검증 선택, 행동 평가 결과를 확인할 수 있습니다.

새 품질 스킬을 포함한 [2026-09-14 전체 감사](docs/skill-audit-2026-09-14.md)에서는 적용 조건·참조 선택을 정리하고, 실제 평가에서 발견된 검사 반복을 보완했습니다. [후속 감사](docs/skill-audit-2026-09-14-followup.md)에서는 세부 참조 선택, 요청 템플릿 중복과 안내를 정리했습니다. 각 기록에 검증 범위와 미실행 항목을 구분했습니다.

## 새 Mac에 설치

설치에는 **Python이 필요하지 않습니다.** macOS의 `/bin/bash`와 기본 명령(`shasum` 등)을 사용합니다. 저장소 다운로드에는 Git이 필요합니다. 아래 HTTPS clone은 공개 저장소를 기준으로 하며 GitHub CLI나 인증이 필요하지 않습니다. 접근이 제한된 저장소를 사용한다면 권한 있는 계정으로 인증한 GitHub CLI의 `gh repo clone awesomelon/codex-skills`를 사용할 수 있습니다.

모든 스킬을 설치하는 기본 대상은 `~/.agents/skills`입니다. 사용자 설정이나 `AGENTS.md`는 자동 변경하지 않습니다.

Git을 준비한 다음 실행합니다. 각 명령의 성공을 확인하고 다음으로 진행합니다.

```bash
git clone https://github.com/awesomelon/codex-skills.git
cd codex-skills
bash scripts/install.sh
```

`install.sh`가 설치·업데이트 진입점입니다. 설치 과정에서 Python·Node·jq나 패키지 설치를 호출하지 않습니다.

기본은 심볼릭 링크 설치입니다. 따라서 저장소를 Downloads 같은 임시 위치가 아닌 오래 유지할 위치에 clone해야 합니다. 설치 후 원본 폴더를 이동하거나 삭제하면 링크가 끊어집니다.

### 설치 확인과 선택 설치

```bash
bash scripts/install.sh --list
bash scripts/install.sh --dry-run
bash scripts/install.sh --skill architecture-guard
```

Codex CLI·IDE에서 `/skills`로 목록을 확인하거나 `$architecture-guard`를 호출합니다. 나타나지 않으면 새 세션에서 확인합니다. 파일 설치 성공은 모델의 실행·리뷰 정확도 검증과 다릅니다.

팀 프로젝트에 복사하려면 대상 프로젝트의 경로를 명시합니다. 사용자 범위와 같은 이름의 스킬을 이중 설치하지 않도록 주의합니다.

```bash
bash scripts/install.sh --mode copy --dest /path/to/other-project/.agents/skills
```

이 스킬 모음 저장소 내부로 자기 자신을 설치하는 것은 차단합니다. 설치 모드를 바꾸려면 기존 설치를 먼저 별도로 백업·정리해야 합니다.

## 업데이트

clone한 `codex-skills` 폴더에서 실행합니다. pull에 실패했으면 설치 단계로 넘어가지 않습니다.

```bash
git pull --ff-only
bash scripts/install.sh
```

특정 스킬만 유지하려면 매번 같은 `--skill` 옵션을 사용합니다. 기본값은 저장소의 모든 스킬이며 선택 목록을 별도로 저장하지 않습니다.

링크 설치는 기존 스킬의 변경이 pull 직후 원본에 반영되며, 설치 스크립트 재실행은 신규 스킬을 연결합니다. 복사 설치는 재실행 때 기존 관리 사본을 갱신하고 신규 스킬을 추가합니다. 설치 전에 스크립트와 스킬 변경을 검토하세요.

안전 동작:

- 같은 설치는 다시 실행해도 중복하지 않습니다. 새 스킬은 `skills/`에서 자동 발견하므로 설치 스크립트를 수정할 필요가 없습니다.
- 기존 수동 설치, 다른 저장소의 링크, 이름 충돌은 덮어쓰지 않고 오류로 알립니다. 기존 폴더를 스킬 검색 경로 **밖으로** 백업하고 필요한 변경을 병합한 후 재실행합니다.
- 관리 복사본의 로컬 파일·폴더 추가/수정/삭제를 해시로 확인하고 변경이 있으면 갱신을 중단합니다. 수정은 되도록 원본 `skills/<name>/`에서 하고 커밋합니다. 복사본의 관리 메타데이터를 편집하지 마세요.
- 선택된 경로의 충돌을 먼저 확인하지만, 전체 스킬 묶음이 하나의 트랜잭션인 것은 아닙니다. 중간 I/O 오류가 발생하면 이미 설치된 스킬은 남고 재실행할 수 있습니다. 복사 교체 실패는 이전 사본 복구를 시도하며, 복구까지 실패하면 백업 경로를 알려줍니다.
- 원격에서 제거된 스킬이나 다른 설치는 자동 삭제하지 않습니다. 스크립트를 동시에 여러 개 실행하지 마세요. 별도 파일 권한 변경은 콘텐츠 해시 검사의 대상이 아닙니다.

### 기존 Python 설치에서 전환

- 기본 **링크 설치**였다면 같은 clone에서 `bash scripts/install.sh`를 실행하면 됩니다. 기존 링크를 재사용합니다.
- `install.py --mode copy`로 만든 **복사본**은 셸 설치기가 자동 변환하거나 덮어쓰지 않습니다. 복사본을 스킬 검색 경로 밖으로 백업하고, 로컬 수정이 있으면 저장소 원본에 병합한 다음 `bash scripts/install.sh --mode copy --dest <기존-설치-경로>`로 새로 설치합니다. 기존 방식으로 당장 갱신해야 한다면 Python 설치기를 계속 사용할 수 있습니다.

셸 복사본은 `.codex-skills-install.v2`, 기존 Python 복사본은 `.codex-skills-install.json`으로 관리합니다. 관리 파일을 바꾸어 설치 방식을 전환하지 마세요.

## 관련 작업에서 아키텍처 검토 적용하기

설치와 호출 정책은 별개입니다. 모듈 책임·의존 방향·공유 상태·공개 API 설계가 바뀌거나 구조 리뷰를 요청할 때 적용할 예제입니다. 모든 코드 작업의 착수·완료에 별도 검토를 의무화하지 않습니다. `snippets/architecture-guard.project.md`는 프로젝트 지침용, `snippets/architecture-guard.global.md`는 개인 전역 지침용입니다. **기존 지침 파일을 덮어쓰지 않고 필요한 블록만 병합합니다.** 설치 스크립트는 이 작업을 대신 수행하지 않습니다.

프로젝트 지침은 해당 프로젝트의 `AGENTS.md`에, 개인 전역 지침은 보통 `~/.codex/AGENTS.md`에 둡니다. `CODEX_HOME`이나 `AGENTS.override.md`를 쓰면 실제로 읽히는 파일을 먼저 확인합니다. 적용 뒤 새 Codex 세션에서 어떤 지침을 읽었는지 확인합니다.

`AGENTS.md`는 에이전트 지침이지 강제 차단 장치가 아닙니다. 반드시 강제해야 하는 의존성·경계 규칙은 실제 프로젝트의 lint·테스트·CI에 두세요. 이 저장소는 상주 감시, 자동 Git 동기화, 백그라운드 리뷰를 설치하지 않습니다.

## 스킬을 하나씩 추가하기

`skills/<skill-name>/SKILL.md`를 만들고 필요할 때만 `references/`, `scripts/`, `agents/openai.yaml`을 추가합니다. README 목록과 `evals/<skill-name>/cases.md`도 갱신합니다. 설치기는 폴더를 자동 발견합니다.

저장소를 개발·검증할 때만 Python 3.10 이상이 필요합니다. 아래 Python 검사는 사용자 설치 과정에서 실행하지 않습니다. 셸 설치기는 Bash 3.2 호환 문법과 BSD 호환 옵션을 사용하며, 테스트 러너에서 CLI를 직접 실행합니다.

다음 요청은 `prompts/add-skill.md`에 있습니다. 스킬 하나의 실제 용도를 적고 그 프롬프트를 사용합니다. 처음부터 많은 스킬을 만들거나 공통 프레임워크로 추상화할 필요는 없습니다.

```bash
bash -n scripts/install.sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

`validate.py`는 이 저장소의 한 줄 `name`·`description` 규약과 파일 참조를 검사하는 작은 검사입니다. 일반 YAML 파서나 공식 Codex 검증기는 아닙니다. 실제 호출/비호출과 실행 품질은 각 `evals/` 시나리오로 별도 확인합니다.

## 참고

설치 위치·발견·링크 지원·호출 방식은 아래 OpenAI 문서를 확인했습니다. 이 저장소의 설치기는 자체 구현이며 공식 설치기가 아닙니다. GitHub 생성·인증 명령은 GitHub CLI 문서를 따릅니다.

- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/agent-configuration/agents-md
- https://cli.github.com/manual/gh_repo_create
- https://cli.github.com/manual/gh_auth_login

사용자가 스킬 작성 시 참고하도록 지정한 글: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra

셸 전환의 검증 범위와 제한은 [셸 설치기 검증 기록](docs/shell-installer-validation.md), 이전 작업 기록은 [검증 기록](docs/validation.md)에 있습니다.
