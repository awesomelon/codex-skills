중요한 문제는 **core의 금지된 기능 의존과 그에 따른 workspace 상태 결합** 1건입니다. 파일은 수정하지 않았습니다.

- **근거·영향:** core/http.ts의 `getJSON()`은 `documentStore`를 직접 가져와 `workspaceId`를 요청 헤더로 사용합니다. 명시된 `core → features` 금지 규칙을 위반합니다. 실제 의존 경로는 `billing/load.ts의 loadInvoices → core/http.ts의 getJSON → documents/store.ts`입니다. 따라서 청구서 조회의 workspace가 문서 기능의 가변 상태에 종속되며, 해당 상태가 바뀌면 청구서 요청 대상도 바뀝니다.
- **최소 조치:** `getJSON`이 workspace 값을 인자로 받도록 하고, `loadInvoices`도 호출자로부터 해당 값을 전달받게 하세요. core에서 문서 store import를 제거하면 됩니다. 새 공통 계층은 필요하지 않습니다. 상위 호출자는 제공되지 않았으므로 실제 workspace 소유자는 추가 확인이 필요합니다.
- **확인 방법:** core의 기능 코드 의존이 제거됐는지 확인하고, 전달한 workspace가 청구서 요청 헤더에 반영되며 문서 store 변경에 영향을 받지 않는지 검증하세요.

`adapters/document-export.ts → features/documents/store.ts`는 명시적으로 허용된 예외이므로 문제로 지적하지 않습니다. 내보내기 권한도 호출 전 서버에서 검증한다는 제공 조건을 따랐습니다.

검토 범위는 제공된 TypeScript 파일 4개 전체의 import, 호출 경로, 상태 소유권입니다. 정적 검토만 수행했으며, 테스트와 실행 의존성이 없어 동작 검증은 하지 않았습니다. 이전 커밋·diff가 없어 신규 문제나 회귀 여부는 판단할 수 없습니다.
