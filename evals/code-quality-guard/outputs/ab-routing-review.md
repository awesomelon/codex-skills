# A/B 비교 — 독립 평가 최종 응답

2026-09-14 실행. 아래는 실제 최종 응답이며 임시 절대 파일 링크는 `A/`, `B/` 상대 표기로 정리했다. A는 기존 `fixtures/policy`, B는 같은 입력에 기존 `outputs/implementation.patch`를 적용한 사본이다. 준비 과정·입력 해시·요청·한계는 [manifest](ab-routing-manifest.json)에 있다.

**유지보수에는 B가 더 낫습니다. 현재 정확성은 두 구현 모두 제공된 검증을 통과했습니다.**

- **코드 근거:** A는 같은 보관 조건을 `A/list.mjs` 2–3행, `A/detail.mjs` 3–4행, `A/bulk.mjs` 3–4행에 각각 구현합니다. 예를 들어 보관 대상에서 `cancelled`를 제외하면 세 판단을 함께 바꿔야 하므로 누락 시 화면과 일괄 처리 사이에 불일치가 생길 수 있습니다.
- B는 `B/archive-policy.mjs`의 `canArchive`를 `B/list.mjs`, `B/detail.mjs`, `B/bulk.mjs`에서 호출합니다. 정책을 찾는 데 한 단계가 추가되지만, 보관 조건의 수정 지점은 한곳입니다. 이는 **코드 추적에 따른 판단**이며 변경 실험은 하지 않았습니다.
- 양쪽의 `canPin`은 독립적으로 유지됩니다. `CONTRACT.md`가 별도 변경을 요구하므로 보관과 조건이 같다는 이유로 합치면 안 됩니다. B의 UI용 함수명과 기존 export도 유지됩니다. 최소 조치는 B의 구조를 채택하고, 정책 변경 시 기존 공개 함수들을 통해 회귀를 확인하는 것입니다.

**정확성 검증:** 동일한 `A/policy.test.mjs`와 `B/policy.test.mjs`가 상태 3종 × 잠금 여부 2종, 상세 액션 순서, 일괄 ID 순서와 빈 입력, 동결한 입력의 비수정을 확인합니다. 실제 UI 호출자와의 통합은 제공되지 않아 검증하지 않았습니다.

| 실행 위치·명령 | 결과 |
| --- | --- |
| A와 B 각각: `node --version && node --test policy.test.mjs` | 동일한 Node v24.19.0, 각각 7개 통과·0개 실패, 종료 0 |
| 비교 폴더: `cmp A/policy.test.mjs B/policy.test.mjs && diff -ru A B` | 테스트 파일 동일. 제품 코드 차이와 B의 새 정책 파일 확인. 종료 1은 `diff`의 차이 발견 상태 |
| `cat`, `nl -ba`, `rg --files`, `find … -name AGENTS.md` | 계약·스킬·제품 코드·테스트를 읽음. 비교 폴더 및 확인한 상위 경로에 적용할 AGENTS.md 없음 |

판단 기준은 요청한 `SKILL.md`와 A/B 비교용 `references/measurement.md`를 적용했습니다. 복잡도·중복률은 분석기가 없어 미측정이며 점수는 매기지 않았습니다. 파일 수정, 네트워크, 패키지 설치, GitHub 작업은 하지 않았습니다.
