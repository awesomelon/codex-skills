완료했습니다. [checkout.mjs](/private/tmp/astra-optimization-20260919/refactoring/checkout.mjs)에서 배송 방식만 조건으로 선택하고 영수증 생성·완료 감사·반환을 한 경로로 합쳤습니다. API, 필드 평가 순서, 오류 전파, 비동기 경계와 부수 효과 순서를 유지했습니다. TASK.md와 테스트는 수정하지 않았습니다.

실행 명령과 결과:

- `cat TASK.md` — 성공, 요구사항 확인.
- `cat /private/tmp/astra-optimization-20260919/candidate-skills/refactoring-guard/SKILL.md` — 성공.
- `rg --files -g '!TASK.md'` — 성공, 구현·테스트 파일 확인.
- `cat checkout.mjs` — 수정 전후 모두 성공.
- `cat /private/tmp/astra-optimization-20260919/candidate-skills/refactoring-guard/references/transformations.md` — 성공.
- `cat checkout.test.mjs` — 성공, 기존 assertions 확인.
- `node --test checkout.test.mjs` — 수정 전 **8/8 통과**, 수정 후 **8/8 통과**.

읽은 스킬 파일은 위 `SKILL.md`, `references/transformations.md` 두 개입니다. 미해결 사항은 없습니다. 검증은 기존 Node 테스트 범위이며 외부 소비자는 조사하지 않았습니다.
