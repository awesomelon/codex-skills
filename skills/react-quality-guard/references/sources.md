# 출처와 적용 방식

확인일: 2026-09-12.

## 기준 원문

- 제공된 [Vercel React Best Practices AGENTS.md](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/AGENTS.md).
- 작성 기준 [고정 커밋의 AGENTS.md](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/AGENTS.md): `063bee94c3f4df8453406c830b0a7df0f2860278`, 파일 blob `4e340a50684a8e7811d5bfa4df48bd9989d0fd87`.
- 저자 표기: Vercel Engineering. 원본 [SKILL.md](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices/SKILL.md)는 라이선스를 MIT로 명시한다.

이 스킬은 공식 Vercel 배포본이 아니다. 원문 전체나 예제 코드를 번들하지 않고, 판단 기준을 한국어로 재구성하며 정확성·검증 조건을 보강했다. upstream의 변경을 자동 반영하지 않는다.

## 원문의 8개 영역과 로컬 문서

| 원문 영역 | 이 스킬에서 다루는 위치 |
| --- | --- |
| 1. Eliminating Waterfalls | [performance.md](performance.md)의 요청 의존관계 |
| 2. Bundle Size Optimization | [performance.md](performance.md)의 초기 전송·공개 import 경로 |
| 3. Server-Side Performance | [server-react.md](server-react.md)의 실행 환경·캐시·서버 경계 |
| 4. Client-Side Data Fetching | [performance.md](performance.md)의 기존 데이터 계층·구독 |
| 5. Re-render Optimization | [react-correctness.md](react-correctness.md)의 상태·Effect와 성능 문서의 렌더 비용 |
| 6. Rendering Performance | [performance.md](performance.md)의 UI 비용과 서버 문서의 hydration |
| 7. JavaScript Performance | [performance.md](performance.md)의 계산량·캐시 수명 |
| 8. Advanced Patterns | [react-correctness.md](react-correctness.md)의 Effect Event·앱 수명 |

## 그대로 일반화하지 않는 기준

- `SWR`, `better-all`, LRU는 원문의 구현 선택지다. 기존 데이터 계층과 표준 Promise로 충족되는 요구에 새 의존성을 강제하지 않는다.
- barrel 파일 자체를 결함으로 보지 않는다. 원문 §2.1도 프레임워크의 import 최적화와 서브패스 타입 지원을 구분한다.
- 원문 §5.5의 기본 인자 안정성은 downstream 전달·의존성에 한정해 판단한다. 생략된 prop이 memo 경계에서 비교되는 과정과 컴포넌트가 실행된 뒤의 기본값 생성을 혼동하지 않는다.
- §8.1과 React 공식 문서를 따라 Effect Event를 의존성에서 제외한다. §8.3의 'stable reference' 설명을 일반 콜백 안정성 보장으로 옮기지 않는다.
- `useTransition`의 네트워크 로딩 대체, 새 React API, hydration 억제는 버전·의미·실제 문제가 일치하는 경우에만 검토한다. 원문의 숫자는 이 프로젝트에서 얻은 측정값이 아니다.

## 보강에 사용한 공식 문서

- [React: You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect) — 파생값·이벤트·외부 동기화 구분.
- [React: Preserving and Resetting State](https://react.dev/learn/preserving-and-resetting-state) — 컴포넌트 정체성과 key·상태 보존.
- [React: memo](https://react.dev/reference/react/memo) — props 비교와 Compiler 적용 조건.
- [React: useEffectEvent](https://react.dev/reference/react/useEffectEvent) — 호출 위치·반응형 값·의존성 제한.
- [React 18: useTransition](https://18.react.dev/reference/react/useTransition)와 [현재 문서](https://react.dev/reference/react/useTransition) — 비동기 지원 차이와 입력·요청 상태의 의미.
- [React: cache](https://react.dev/reference/react/cache) — RSC 요청 범위.
- [TanStack Query: Query Keys](https://tanstack.com/query/latest/docs/framework/react/guides/query-keys) — 데이터 식별과 의존 변수.
- [Next.js: Data Security](https://nextjs.org/docs/app/guides/data-security) — 서버 함수와 데이터 경계.

현재 문서가 저장소에 설치된 버전과 다를 수 있다. API 적용 시 대상 버전의 문서·타입을 우선한다. 이 문서를 읽는 것만으로 관련 없는 의존성을 업그레이드하지 않는다.

스킬 구성은 사용자가 지정한 [OpenAI의 skills·prompts 재검토 글](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)을 참고해 짧은 발견 정보, 필요한 참조만 읽기, 결과 중심의 판단 기준으로 유지한다.
