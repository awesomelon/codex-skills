# Earendil 원문 지표

Verbosity·Erosion 계산을 요청받았을 때 사용한다. 공통 비교 조건과 측정 가능한 신호는 [measurement.md](measurement.md)를 따른다.

[Earendil의 Measuring the sloppiness of code](https://earendil.com/posts/measuring-code-sloppiness/)는 정확성과 품질을 구분하고, 단순 AI 채점과 LOC 최적화의 한계를 논의한다. 아래는 글에 제시된 진단 지표이며 보편적인 합격 기준이 아니다.

- `Verbosity = |AST 규칙이 표시한 라인 ∪ clone 라인| / LOC`. 같은 라인을 두 번 세지 않도록 합집합으로 계산한다.
- `mass(f) = CC(f) × sqrt(SLOC(f))`; `Erosion = Σ[CC(f) > 10] mass(f) / Σ mass(f)`. 여기서 10은 이 지표 정의에 사용된 조건이며 모든 프로젝트의 함수 복잡도 상한이 아니다.

원문과 같은 정의를 지원하는 분석 결과가 있을 때만 이름을 붙여 계산한다. 도구·규칙·분모·언어 지원을 밝히고, 분모가 0이면 미정의로 둔다. 다른 정의는 별도 지표라고 표시한다. 값을 낮추려고 함수만 분할하거나 무관한 단순 코드를 늘리지 않는다. 이 스킬에는 해당 분석기나 자동 채점기를 내장하지 않는다.
