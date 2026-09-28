<p align="center">
  <img src="assets/logo.png" width="180" alt="CraftFlow: 서로 연결된 모듈을 받치는 펼쳐진 코드 책">
</p>

# CraftFlow

[English](README.md) · **한국어**

**Make the right change. — 올바른 변경을 만듭니다.**

Codex를 위한 판단 중심 엔지니어링. 문제를 이해하고, 필요한 만큼 변경하고, 결과를 검증합니다.

## 왜 CraftFlow인가

코드가 동작하는 것은 성공적인 변경의 한 부분입니다. 실제 문제를 해결하고, 기존 계약을 지키며, 다음 변경도 이해하고 수행하기 쉬워야 합니다. CraftFlow는 계획·구현·리뷰에 필요한 판단을 돕고, 기술별 전문 지침을 상황에 맞게 적용합니다.

제안된 해결책이 적절한지 살펴봐야 할 때, 변경이 여러 책임 영역에 걸쳐 있을 때, 구현 대안에 따라 유지보수 비용이 달라질 때 활용할 수 있습니다. 범위가 작고 명확한 요청은 바로 실행할 수 있습니다.

## 세 가지 원칙

| 원칙 | 실제 적용 |
| --- | --- |
| **문제를 이해합니다.** | 증상과 원인을 구분하고, 제안된 변경이 목적에 어떻게 기여하는지 확인합니다. 이미 정한 결정은 재사용합니다. 사용자가 결정해야 할 중요한 미정 사항에는 근거와 권고안을 제시합니다. |
| **문제 해결에 필요한 만큼 변경합니다.** | 국소 원인은 해당 위치에서, 공통 원인은 이를 책임지는 곳에서 수정합니다. 현재 요구사항, 영향을 받는 사용처, 향후 변경 비용으로 범위를 판단합니다. 필요한 복잡성과 독립적으로 바뀌는 정책은 보존합니다. |
| **결과를 검증합니다.** | 실제로 수행한 검증을 근거로 완료 여부를 설명합니다. 동작 확인, 유지보수성 판단, 측정된 성능, 남은 불확실성을 구분합니다. |

세 원칙은 작업에 필요한 깊이로 적용하는 판단 기준이며, 매번 거쳐야 하는 고정 단계가 아닙니다. 계획 요청은 권고안으로 마칠 수 있고, 구현 요청에는 관련 검증이 포함됩니다. 리뷰에서는 검토 대상 코드를 수정하지 않습니다. 작은 수정에 별도 명세서, 리뷰 패널, 학습 문서를 만들 필요는 없습니다.

## 사용 방법

원하는 결과와 작업 범위를 함께 요청하세요.

```text
$craftflow-orchestrator를 사용해 이 마이그레이션이 보고된 문제를 해결하는지
검토하고 계획을 제안해줘. 코드는 수정하지 마.

$craftflow-orchestrator를 사용해 승인된 변경을 구현하고 통합 동작을 검증해줘.

$craftflow-react를 사용해 이 폼의 상태와 요청 처리를 리뷰해줘. 파일은 수정하지 마.
```

예를 들어 큰 모듈을 나눠 달라는 요청에서는 무엇이 함께 바뀌고 무엇이 독립적으로 바뀌는지 살펴봅니다. 파일 길이만으로 적절한 경계를 정할 수는 없습니다. 선택한 경계와 그에 따른 변경 비용, 유지해야 할 동작을 설명하는 것이 유용한 결과입니다.

오케스트레이터는 범위·의존성·완료 여부를 책임집니다. 전문 스킬은 작업에 필요한 기술적 판단을 지원하며, 각각 독립적으로 사용할 수도 있습니다. 에이전트 위임은 독립적인 작업에 이점이 있을 때 선택합니다. 프로젝트의 학습 내용은 검증되었지만 코드만으로 파악하기 어려운 판단 근거가 다음 결정에 도움이 되고, 기록하는 일이 요청 범위에 포함될 때 남깁니다.

플러그인을 지원하는 환경에서는 해당 환경에 표시된 스킬 이름을 사용하세요. 이름에 플러그인 접두사가 붙을 수 있습니다.

## Codex 플러그인으로 설치하기

플러그인 기능을 지원하는 Codex CLI와 Git이 필요합니다.

```bash
codex plugin marketplace add awesomelon/craftflow
codex plugin add craftflow@craftflow
```

첫 번째 명령이 성공한 뒤 두 번째 명령을 실행하세요. 7개 스킬이 **CraftFlow** 플러그인으로 함께 설치됩니다. 저장소를 직접 복제하거나 셸 설치 스크립트를 실행할 필요는 없습니다. `codex plugin list`로 설치 여부를 확인할 수 있습니다.

[업데이트와 개별 스킬 설치에서 전환](docs/installation.md) · [플러그인 구성](docs/plugin.md)

## 포함된 스킬

| 스킬 | 지원하는 판단 |
| --- | --- |
| [craftflow-orchestrator](skills/craftflow-orchestrator/SKILL.md) | 무엇에 우선 집중할지, 의존하는 작업을 어떻게 연결할지, 언제 완료로 볼지 판단합니다. |
| [craftflow-architecture](skills/craftflow-architecture/SKILL.md) | 책임을 어디에 둘지, 어떤 경계와 계약을 지켜야 할지 판단합니다. |
| [craftflow-code-quality](skills/craftflow-code-quality/SKILL.md) | 무엇이 다음 변경의 비용을 높이는지, 어떤 규칙을 한 곳에서 관리해야 할지 판단합니다. |
| [craftflow-refactoring](skills/craftflow-refactoring/SKILL.md) | 관찰 가능한 동작을 보존하면서 구조를 개선하는 방법을 판단합니다. |
| [craftflow-react](skills/craftflow-react/SKILL.md) | 컴포넌트·훅·상태·렌더링이 의도한 사용자 상호작용을 유지하도록 설계합니다. |
| [craftflow-tanstack-query](skills/craftflow-tanstack-query/SKILL.md) | Query v5의 조회와 변경이 여러 사용처에서 서버 데이터의 정확성을 유지하도록 설계합니다. |
| [craftflow-typescript](skills/craftflow-typescript/SKILL.md) | 타입으로 보장할 부분과 런타임 검증이 필요한 부분을 구분합니다. |

## 문서

- [가이드와 설계 이력](docs/README.md)
- [기여 방법과 검증](CONTRIBUTING.md)
- [평가 근거](evals/README.md)

연결된 상세 문서와 스킬 지침은 영어로 제공됩니다.

[OpenAI의 스킬 작성 가이드](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)를 바탕으로, 진입 문서는 간결하게 유지하고 세부 지침은 필요할 때 읽으며 작업 규모에 맞게 수행하도록 구성했습니다. 스태프 엔지니어 수준의 판단이 설계 목표이며, 평가 기록에는 실제로 검증한 범위가 명시되어 있습니다.
