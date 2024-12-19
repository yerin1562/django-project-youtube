# django-project-youtube
oz-project for django rest-framework and release

## (1) Project Settings
- GitHub Repository 

## (2) Docker 
- Docker란?
    Docker는 컨테이너 기반 가상화 기술로, 애플리케이션과 그 실행 환경을 컨테이너에 패키징하여 일관된 환경에서 실행할 수 있게 해준다.

- Docker 구성요소
    1. Docker Engine
        - Docker 플랫폼의 핵심, 컨테이너를 실행하고 관리하는 역할
            주요 구성:
            Server (Docker Daemon): 컨테이너와 이미지 관리
            REST API: Docker Daemon과 통신하는 인터페이스
            CLI (Command Line Interface): Docker 명령어를 통해 작업 수행

    2. Docker Image
        - 컨테이너 실행을 위한 읽기 전용 템플릿
        - 애플리케이션과 그에 필요한 모든 라이브러리, 종속성, 파일 시스템 등을 포함
        - Dockerfile을 작성하여 이미지를 생성
            - 하나의 이미지를 여러 컨테이너가 재사용 가능
    
    3. Docker Container
        - Docker 이미지를 기반으로 실행되는 가상 환경
        - 애플리케이션이 실행되는 독립된 단위로, 필요한 파일 시스템, 네트워크, CPU, 메모리 등을 격리하여 제공
        - 컨테이너는 읽기-쓰기 계층이 포함되며, 동일한 이미지를 기반으로 여러 컨테이너를 생성할 수 있음

    4. Docker Registry
        - Docker 이미지를 저장하고 배포하는 시스템
        주요 Registry:
        Docker Hub: Docker에서 제공하는 기본 퍼블릭 레지스트리
        Private Registry: 조직 내부에서 운영하는 사설 레지스트리

    5. Docker Compose
        - 여러 컨테이너를 정의하고 실행하기 위한 도구로, YAML 파일 (docker-compose.yml)로 서비스 간의 관계를 설정
        - Docker Image와 Docker Container

