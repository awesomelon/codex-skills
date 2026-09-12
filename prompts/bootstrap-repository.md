# 최초 게시용 Codex 원샷 프롬프트

먼저 이 패키지를 풀고, `README.md`, `skills/`, `scripts/`가 보이는 `codex-skills` 폴더를 데스크탑 Codex에서 연다. 아래 블록 전체를 요청한다. 이 파일은 실행 기록이 아니라 요청 템플릿이다.

```text
현재 폴더의 파일로 내 GitHub 계정에 비공개 awesomelon/codex-skills 저장소를 만들고 최초 업로드해줘. 설명만 하지 말고 가능한 작업을 실제로 수행해줘.

목표는 앞으로 만든 Codex 스킬을 skills/<name>/에 하나씩 추가하고, 새 데스크탑에서 clone 후 설치 명령 한 번으로 재사용하는 것이다. 기존 architecture-guard 본문과 참조 문서를 보존해줘.

1. 현재 폴더의 AGENTS.md, README.md, skills/, scripts/, tests/를 읽고 제공된 구성을 사용해. 새로운 구현이나 패키지 관리 시스템으로 다시 만들지 마.
2. 현재 Git 저장소 경계, 작업 트리와 remote를 확인해. 이 폴더가 무관한 상위 저장소 안에 있으면 그 저장소를 커밋하거나 게시하지 마. 사용자 기존 변경과 인증 파일도 보존해.
3. Git, GitHub CLI, Python 3.10+를 확인해. gh auth status와 gh api user --jq .login으로 github.com의 활성 계정이 awesomelon인지 확인해. 토큰·인증 파일을 출력하거나 채팅에 요구하지 마. 인증이 없으면 브라우저 인증이 필요하다고 정확히 알리고, 검증 등 독립적으로 가능한 작업은 완료해.
4. gh repo view로 awesomelon/codex-skills의 존재와 공개 범위를 확인해. 조회 실패를 무조건 '저장소 없음'으로 간주하지 말고 인증·접근·네트워크 오류를 구분해. 기존 저장소가 있으면 파일과 이력을 확인해서 보존하고, 재생성·공개 전환·강제 push하지 마. 파일 충돌이 있으면 기존 저장소의 작업 브랜치와 PR로 변경을 분리해.
5. python3 scripts/validate.py와 python3 -m unittest discover -s tests -v를 실행해. Windows에서는 py -3을 사용해. 임시 경로에서 링크/복사 설치와 재실행을 검사하되 내 실제 전역 설정이나 설치 스킬은 변경하지 마.
6. 신규 로컬 저장소라면 main으로 초기화하고, 게시할 파일만 명시적으로 stage해. diff와 비밀정보 포함 여부를 확인한 뒤 feat: add architecture-guard and portable skill installer로 커밋해. Git 작성자 정보가 없으면 임의로 만들지 마.
7. 신규 원격 저장소라면 gh repo create awesomelon/codex-skills --private --source=. --remote=origin --push로 생성·업로드해. 기존 원격이 비어 있으면 읽은 상태를 확인한 뒤 정상 push하고, 기존 이력이 있으면 안전한 브랜치/PR 경로를 사용해. 현재 폴더와 다른 저장소나 계정에는 쓰지 마.
8. 업로드 후 원격 파일과 커밋 SHA, 비공개 여부를 다시 조회해. 로컬 생성·원격 업로드·실행 검증을 구분해 보고해. 인증·권한 때문에 막힌 단계는 성공이라고 표현하지 마.

마지막에는 실제 저장소 또는 PR 주소, 추가한 스킬, 검증 결과와 한계, macOS/Linux와 Windows의 최초 설치·업데이트 명령을 한국어로 알려줘. Codex 모델이 스킬을 실제로 실행한 것은 별도로 확인하지 않았다면 미검증으로 남겨줘. 내 전역 AGENTS.md와 config.toml은 자동으로 수정하지 마.
```
