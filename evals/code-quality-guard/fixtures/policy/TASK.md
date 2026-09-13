# 문서 액션 모듈

입력은 유효한 문서 배열이다. 문서는 id(문자열), status(draft/completed/cancelled), locked(불리언)를 가진다.

제품 계약:
- 목록의 보관 버튼, 상세 메뉴의 archive 액션, 일괄 보관 대상은 모두 같은 보관 정책을 따른다. 현재 completed 또는 cancelled이면서 locked가 false인 문서만 보관할 수 있다.
- 상세 메뉴는 open을 먼저, 보관 가능하면 archive를 다음에 반환한다. 일괄 대상 ID는 입력 순서를 유지한다.
- 핀 기능은 독립적인 제품 정책이다. 현재 조건이 보관과 같지만 별도로 변경할 수 있어야 한다.
- 모든 함수는 입력을 수정하지 않는다. UI용 이름과 모듈의 export는 호출자가 사용 중이다.

검증: node --test policy.test.mjs
외부 의존성이나 AST·clone 분석기는 없다. 제공 파일은 현재 스냅샷이며 이전 버전은 없다.
