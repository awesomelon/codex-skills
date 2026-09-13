# 검증 기록

2026-09-13 설치 진입점을 셸로 전환했다. 현재 설치·검증 방법은 [셸 설치기 기록](shell-installer-validation.md)에 있다.

아래는 게시 단계별 당시 기록이다. 이후 두 스킬 본문의 감사·개선과 별도 행동 평가 결과는 [2026-09-12 감사 기록](skill-audit-2026-09-12.md)에 있다.

검증일: 2026-09-12. 기존 패키지를 GitHub에 게시하면서 Linux 컨테이너에서 다시 검증했다.

## 실제 수행

- 원본 architecture-guard 패키지의 네 스킬 파일을 재사용했다. SKILL.md, agents/openai.yaml, 두 reference의 내용은 원본과 동일하다.
- `python scripts/validate.py`: 기본 frontmatter 규약과 스킬 내부 상대 참조 검사 통과.
- `python -m unittest discover -s tests -v`: 설치·갱신·충돌·사용자 변경 보존·오류 복구와 검사기 관련 24개 테스트 통과.
- 임시 사용자 경로를 대상으로 실제 CLI의 목록/미리보기/링크/복사/재설치와 종료 코드 확인.
- 원본 스킬 파일의 YAML 파싱, 전체 배포 파일의 상대 Markdown 참조와 ZIP 무결성 검사.
- 사용자가 생성한 `awesomelon/codex-skills` 저장소의 비공개 상태, 빈 초기 이력, 쓰기 권한을 확인했다.
- 초기 ZIP 전용이던 README를 기존 저장소의 설치·업데이트 안내로 정리했다. 스킬 본문·참조 문서·설치기·테스트는 원본 패키지를 보존했다.

## macOS 사용 범위 반영

- 설치·업데이트 안내와 이후 작업 지침을 macOS 기준으로 정리했다.
- 설치기의 운영체제별 기본값 분기를 제거하고 심볼릭 링크를 기본으로 사용한다. 프로젝트에 독립 사본이 필요할 때의 명시적 복사 옵션은 유지했다.
- 변경 후 기본 CLI 링크 설치·재실행, 구조 검사, 기존 24개 테스트를 Linux의 임시 경로에서 재검증했다. 스킬 본문과 참조 문서는 변경하지 않았다.

링크와 복사 경로 모두 Linux에서 실행했다. macOS 운영체제 자체의 실행 검증을 대체하지 않는다. 복구 테스트는 I/O 오류를 주입한 단위 테스트이며 모든 저장장치 실패를 보증하지 않는다.

## React 품질 스킬 추가

`react-quality-guard`의 구조·설치·행동 평가와 한계는 [별도 기록](../evals/react-quality-guard/results.md)에 남겼다. 기존 `architecture-guard`와 설치기 코드는 변경하지 않았다.

## 미실행·미완료

- GitHub Actions CI는 구성하거나 실행하지 않았다. 위 결과는 로컬 실행 기록이다.
- 사용자 컴퓨터의 ~/.agents/skills, ~/.codex/AGENTS.md, config.toml은 변경하지 않았다.
- 실제 Codex에서 스킬 발견, 자동/명시 호출, 작업 전후의 스킬 실행과 리뷰 품질은 검증하지 않았다.
- `evals/architecture-guard/cases.md`의 12개 항목은 모델 행동 평가 시나리오이며 통과 기록이 아니다.
- `validate.py`는 일반 YAML 파서·공식 Codex 검증기가 아니다. 외부 URL 가용성, 모든 Markdown 문법, 의미적 지침 충돌까지 검증하지 않는다.

## 다시 실행

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

실제 macOS Codex 검증은 Mac에 설치한 뒤 호출 목록과 행동 평가 시나리오를 확인하여 별도로 기록한다.
