# 스킬 감사와 개선 — 2026-09-12

기준 커밋: `2a17c3950824ab6547bc498df4cd9818c1727bcc`. 대상은 두 스킬 전체, 저장소 `AGENTS.md`, 호출용 snippets, 추가 요청 템플릿이다.

사용자가 지정한 [OpenAI 글](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)의 짧고 구별되는 호출 설명, 필요한 참조만 읽기, 결과 중심 지침, 위험에 맞는 검증을 기준으로 감사했다. 특정 모델을 필수 조건으로 지정하지 않았다.

## 발견과 조치

| 발견 | 개선 |
| --- | --- |
| 두 description에 세부 점검 항목이 본문과 중복됨 | 선택에 필요한 용도와 혼동 가능한 제외 범위로 정리 |
| architecture 본문·사전 점검·리뷰에 범위·보고·검증 지침이 반복됨 | 본문에 소유권·의존·계약·개입 기준을 두고, 단계별 참조에는 고유 판단만 유지 |
| 사전 점검의 4개 결과 항목과 리뷰의 고정 분류·판정이 작은 작업에도 보고서 틀을 유도함 | 필요한 근거와 결론은 유지하고 형식은 요청·작업 규모에 맞게 선택 |
| React 진입부가 매번 버전·잠금 파일·빌드·라우터·Compiler 전체 확인으로 읽힘 | API 지원·번들·memo 등 판단을 바꾸는 쟁점에 따라 환경을 확인하고 제공된 정보 재사용 |
| 스킬 문구만 바뀌어도 저장소 지침·추가 템플릿이 설치기 전체 테스트를 요구함 | 구조 검사는 스킬 변경에, 설치기 테스트는 해당 코드 변경에, 행동 평가는 중요한 지침 변경에 연결 |
| 상시 삽입용 snippets가 스킬 본문의 조사·보고 절차를 반복함 | 기존 착수 전·완료 전 점검 정책과 호출 경로·리뷰 전용 범위를 남김 |

기존의 목적, 명시된 필수 검증, 읽기 전용 요청, 원격 쓰기 범위는 보존했다. 비공개 저장소·사용자 변경 보존·강제 push 금지와 macOS 사용 조건도 유지했다. 설치기·검사기·테스트 코드는 변경하지 않았다. `agents/openai.yaml`의 표시명·명시 호출 예시·자동 선택 정책도 그대로다.

React의 네 참조 문서는 유지했다. draft 보존, API 내부 구현이 없을 때의 불확실성, memo 기본값·Effect Event·React 18 transition·서버 캐시의 적용 조건은 이전 평가에서 유용했던 전문 판단 기준이다. 길이만을 이유로 제거하거나 일반적인 체크리스트로 바꾸지 않았다. 최초 게시 템플릿은 이미 완료된 작업을 재현하는 자료라 수정하지 않았다.

## 길이 비교

Python `len(text)` 기준의 유니코드 문자 수다. SKILL.md에는 frontmatter와 개행을 포함한다. 토큰 수·실행 속도·모델 품질 향상 수치가 아니다.

| 대상 | 이전 | 이후 | 감소 |
| --- | ---: | ---: | ---: |
| architecture-guard SKILL.md | 2,720 | 1,367 | 49.7% |
| react-quality-guard SKILL.md | 2,219 | 1,391 | 37.3% |
| architecture description | 89 | 64 | 28.1% |
| React description | 131 | 80 | 38.9% |
| 저장소 AGENTS.md | 1,124 | 975 | 13.3% |

두 SKILL.md 합계는 4,939자에서 2,758자로 줄었다. 이 감사 문서와 평가 기록은 설치되는 스킬 밖에 있다.

## 행동 평가

수정된 스킬과 원본 입력을 서로 다른 임시 폴더에 복사하고, 대화 이력이 없는 별도 에이전트 세 개에 스킬 경로와 해당 TASK.md만 전달했다. 기대 지적·해법·다른 평가 결과는 전달하지 않았다. 모든 실행은 명시 호출이며 별도 모델 버전 식별자는 수집하지 않았다.

| 입력 | 실제 관찰 | 읽은 참조 |
| --- | --- | --- |
| [현재 아키텍처 리뷰](../evals/skill-audit-2026-09-12/fixtures/architecture/TASK.md) | core→기능 역의존과 청구 호출의 숨은 상태 결합을 지적. 허용된 adapter 예외를 결함으로 오인하지 않고, 비교 자료 없이 회귀를 주장하지 않음 | review.md |
| [React 리뷰](../evals/react-quality-guard/fixtures/review/TASK.md) | 테넌트 캐시와 재조회 실패 시 draft 소실을 발견. 불투명한 API 내부의 갱신 누락을 단정하지 않고 draft·memo·저장 상태를 보존하도록 제안 | react-correctness.md, performance.md |
| [React 구현](../evals/react-quality-guard/fixtures/implementation/TASK.md) | DocumentPicker만 수정해 원본 배열 mutation·파생 상태·Effect를 제거. 표시·공개 props·입력·선택 코드를 보존하고 가능한 계산 검증까지 완료 | react-correctness.md, performance.md |

읽은 참조와 실행 명령은 작업 후 에이전트에 추가 실행 없이 확인했다. 전후 해시는 두 리뷰 입력의 무변경과 구현 파일 하나만 변경된 것을 확인한다. 별도 저장한 [아키텍처 리뷰](../evals/skill-audit-2026-09-12/outputs/architecture-review.md), [React 리뷰](../evals/skill-audit-2026-09-12/outputs/react-review.md), [구현 보고](../evals/skill-audit-2026-09-12/outputs/react-implementation.md), [구현 코드](../evals/skill-audit-2026-09-12/outputs/DocumentPicker.tsx), [스킬·입력 해시](../evals/skill-audit-2026-09-12/outputs/manifest.json)로 확인할 수 있다.

세 표본에서는 요청 범위·관련 참조 선택·근거 수준 기준을 충족했다. 이전 스킬과의 통제된 A/B 성능 비교는 아니다. 전체 시나리오의 통과, 자동 발견·비호출 정확도, 반복 안정성을 주장하지 않는다. 새로 추가한 작은 작업·검증 종료 시나리오도 이 세 표본이 직접 다룬 범위를 넘어서는 부분은 미실행이다.

## 실행 검증과 한계

Linux 컨테이너에서 다음을 실행했다.

- 두 스킬의 `quick_validate.py`, 저장소 `scripts/validate.py`, UI YAML 확인 통과.
- 감사 시작 시 지침에 있던 설치기 테스트 24개를 한 번 실행해 모두 통과. 이후 문서 작업 때문에 반복 실행하지 않았다.
- 새 구현 출력의 실제 계산식을 추출한 [Node 검사](../evals/skill-audit-2026-09-12/outputs/check-picker.mjs) 9개 통과. 정렬·검색·원본 불변성·빈 입력·새 props·원소 정체성 등을 확인했다. 기존 검사를 이번 출력에 재사용했다.
- 리뷰 입력과 스킬 사본의 전후 해시 보존, 구현 변경 범위, 배포 파일의 상대 Markdown 링크를 확인했다.

React 렌더·타입 검사·브라우저 상호작용·성능 프로파일은 실행하지 않았다. macOS 실기 설치와 Codex의 자동 호출도 미검증이다. 사용자 Mac의 설치·전역 지침은 변경하지 않았다. 이전 [React 생성 평가](../evals/react-quality-guard/results.md)와 [최초 배포 검증](validation.md)은 당시 기록으로 보존했다.

재현할 때 각 입력 폴더를 별도 작업 공간에 복사하고 해당 스킬에 TASK.md를 요청한다. 입력 원본은 보존하고 결과·변경 파일·사용한 스킬 버전을 별도로 기록한다. 계산 검사는 저장소 루트에서 `node evals/skill-audit-2026-09-12/outputs/check-picker.mjs`로 실행한다.
