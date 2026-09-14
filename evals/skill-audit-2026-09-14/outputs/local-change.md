`volume.mjs`에서 음수를 0으로 제한하도록 수정했습니다. 반환값은 0~100이며 기존 함수 이름과 export는 유지했습니다.

`node --test volume.test.mjs` 테스트가 통과했습니다. TASK.md, 테스트, 스킬 원문은 변경하지 않았습니다.
