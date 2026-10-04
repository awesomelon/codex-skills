외부 프로필 검증 누락이 실제 결함이며, 현재 테스트도 이를 확인하지 못합니다. 나머지 개선은 타입 계약과 불필요한 복잡도에 관한 사항입니다. 평가 대상 파일은 수정하지 않았습니다.

**→ [P1] `decode`가 검증하지 않은 JSON을 `Profile`로 반환합니다.** [client.ts:4](/private/tmp/tact-integration-kify091l/review/client.ts:4)의 `as object as Profile`은 런타임 검증을 하지 않습니다. 실제 파일을 실행했을 때 `{}`, `null`, 숫자 `id`, 지원하지 않는 `role`이 모두 반환됐고, 이후 `route`에서 각각 호출 대상 부재, null 접근, `toUpperCase` 호출 실패 등이 발생했습니다. JSON 파싱 직후 null이 아닌 객체인지, `id`가 문자열인지, `role`이 `reader` 또는 `editor`인지 확인하고 실패를 명시적으로 반환하거나 예외로 알려야 합니다. 현재 계약에 없는 비어 있지 않은 ID 같은 조건까지 추가할 근거는 없습니다. `JSON.parse` 결과의 `unknown`은 적절하며, 검증 없는 연속 단언을 제거하는 것이 핵심입니다.

**→ [P2] 검증 테스트가 구현을 전혀 실행하지 않습니다.** [client.test.ts:2](/private/tmp/tact-integration-kify091l/review/client.test.ts:2)의 모듈 모킹은 `decode`를 언제나 고정 프로필을 반환하는 함수로 바꿉니다. 따라서 테스트는 `{}`가 거부되는지 확인하지 않으며 실제 구현이 고장 나도 통과할 수 있습니다. 순수 함수인 실제 `decode`를 직접 호출해 정상 입력과 위의 잘못된 입력, 잘못된 JSON 구문을 확인하는 테스트로 바꾸면 충분합니다. 별도의 의존성 주입 구조는 필요하지 않습니다.

**→ 타입 계약 손실과 리플렉션은 개선 대상이며, 정상 입력에서 확인된 런타임 결함은 아닙니다.** [client.ts:9](/private/tmp/tact-integration-kify091l/review/client.ts:9)의 `profileId(profile: object): unknown`은 ID가 없는 객체도 허용하고 문자열 반환 정보를 지웁니다. 프로필용 함수라면 `Profile` 또는 실제로 필요한 `Pick<Profile, "id">`를 받고 `profile.id`를 반환하는 계약이 적합합니다. [client.ts:18](/private/tmp/tact-integration-kify091l/review/client.ts:18)에서는 이미 `Profile`인 값을 `unknown`으로 넓혔다가 단언으로 되돌리고 `Reflect.apply`로 호출할 이유가 없습니다. `routes[profile.role](profile)`로 직접 호출하면 됩니다. 단, 이것만으로 외부 입력 검증 누락이 해결되지는 않습니다.

**→ 열린 사전 타입을 좁히면 컴파일 시 확인할 수 있는 정보가 늘어납니다.** [client.ts:13](/private/tmp/tact-integration-kify091l/review/client.ts:13)의 라우트 타입은 `Record<Profile["role"], (p: Profile) => string>` 또는 이에 대한 `satisfies`로 필수 역할의 존재를 확인할 수 있습니다. 현재 두 역할이 모두 구현돼 있으므로 누락 버그가 있다고 보고하지는 않습니다. [client.ts:23](/private/tmp/tact-integration-kify091l/review/client.ts:23)의 `loadProfile`은 반환 타입을 `Profile`로 유지하면 됩니다. `ProfileShape = Record<string, unknown>`은 이미 알려진 필드와 역할 정보를 지우며 별도 도메인 개념도 표현하지 않습니다. 이는 스킬의 타입 보존 원칙에 따른 개선이고, 이름만 바꾸는 수정은 효용이 작습니다.

**→ `parseName`의 경계 검증은 유지하는 것이 타당합니다.** [boundary.ts:1](/private/tmp/tact-integration-kify091l/review/boundary.ts:1)은 별도의 외부 입력 경계이므로 `unknown`과 `typeof` 검사가 필요합니다. 스키마 의존성을 도입하거나 검사를 제거할 근거는 없습니다. 공백 제거 결과를 변수에 담아 재사용할 수 있지만, 현재 두 번의 `trim()`은 정확성 결함으로 볼 수 없습니다.

**→ 확인 범위:** Node.js v24.21.0에서 실제 TypeScript 파일을 직접 불러와 정상 라우팅, 잘못된 프로필 4종의 후속 오류, 이름 정규화와 거부 동작을 확인했습니다. README에 명시된 대로 실행 가능한 프로젝트와 테스트 의존성이 없어 Vitest 및 TypeScript 타입 검사는 실행하지 않았습니다. 테스트 관련 판단은 소스 검토에 근거합니다.
