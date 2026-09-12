# 요청

$architecture-guard로 이 코드의 현재 아키텍처를 리뷰만 해줘. 파일을 수정하지 말고 중요한 문제, 최소 조치, 검토 범위와 한계를 한국어로 알려줘.

이 폴더는 전체 제공 자료이며 이전 커밋·diff·실행 의존성은 없다. 네트워크 접속·패키지 설치 없이 검토해줘. core에서 기능 코드로 의존하는 것은 금지한다. 단, adapters/document-export.ts는 export 변환을 위해 features/documents/store.ts를 읽도록 허용한 기존 예외다. 문서 내보내기 권한은 호출 전에 서버에서 검증한다.
