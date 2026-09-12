# 검증 기록

검증일: 2026-09-12. 기존 패키지를 GitHub에 게시하면서 Linux 컨테이너에서 다시 검증했다.

## 실제 수행

- 원본 architecture-guard 패키지의 네 스킬 파일을 재사용했다. SKILL.md, agents/openai.yaml, 두 reference의 내용은 원본과 동일하다.
- `python scripts/validate.py`: 기본 frontmatter 규약과 스킬 내부 상대 참조 검사 통과.
- `python -m unittest discover -s tests -v`: 설치·갱신·충돌·사용자 변경 보존·오류 복구와 검사기 관련 24개 테스트 통과.
- 임시 사용자 경로를 대상으로 실제 CLI의 목록/미리보기/링크/복사/재설치와 종료 코드 확인.
- 원본 스킬 파일의 YAML 파싱, 전체 배포 파일의 상대 Markdown 참조와 ZIP 무결성 검사.
- 사용자가 생성한 `awesomelon/codex-skills` 저장소의 비공개 상태, 빈 초기 이력, 쓰기 권한을 확인했다.
- 초기 ZIP 전용이던 README를 기존 저장소의 설치·업데이트 안내로 정리했다. 스킬 본문·참조 문서·설치기·테스트는 원본 패키지를 보존했다.

복사 경로도 Linux에서 실행했다. Windows/macOS 운영체제 자체의 실행 검증을 대체하지 않는다. 복구 테스트는 I/O 오류를 주입한 단위 테스트이며 모든 저장장치 실패를 보증하지 않는다.

## 미실행·미완료

- GitHub Actions CI는 구성하거나 실행하지 않았다. 위 결과는 로컬 실행 기록이다.
- 사용자 컴퓨터의 ~/.agents/skills, ~/.codex/AGENTS.md, config.toml은 변경하지 않았다.
- 실제 Codex에서 스킬 발견, 자동/명시 호출, 작업 전후의 스킬 실행과 리뷰 품질은 검증하지 않았다.
- `evals/architecture-guard/cases.md`의 12개 항목은 모델 행동 평가 시나리오이며 통과 기록이 아니다.
- `validate.py`는 일반 YAML 파서·공식 Codex 검증기가 아니다. 외부 URL 가용성, 모든 Markdown 문법, 의미적 지침 충돌까지 검증하지 않는다.

## 다시 실행

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Windows에서는 python3 대신 py -3을 사용한다. 실제 Codex 검증은 해당 운영체제에 설치한 뒤 호출 목록과 행동 평가 시나리오를 확인하여 별도로 기록한다.
