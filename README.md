## CrewAI 기반 주식 분석 프로젝트 README.md

**개요:**

본 프로젝트는 CrewAI 프레임워크를 활용하여 주식 분석을 수행하는 가상의 전문가 팀을 구축합니다. 이 팀은 뉴스와 시장 여론 수집, 기술 분석, 재무 분석을 수행하고, 최종적으로 투자 추천을 제공하는 역할을 합니다.

**주요 기능:**

* CrewAI 프레임워크를 활용한 에이전트 조율 및 협업
* yfinance 라이브러리와의 통합을 통한 금융 데이터 획득
* 연구, 기술 분석, 재무 분석, 투자 관리를 담당하는 전문 에이전트로 구성된 모듈형 설계
* 투명성을 위해 명확한 작업 설명과 예상 출력 제공

**필수 조건 및 패키지 설치:**

* Python 3.10 <3.9버전은 crewai-tools가 지원되지 않습니다.>
* CrewAI (https://www.crewai.com/, https://docs.crewai.com/)
* crewai-tools
* yfinance

**유의사항:**

1. 필요한 라이브러리 설치: requirements.txt파일을 참고하세요!
2. 이 리포지토리를 복제하거나 다운로드합니다.
3. OpenAI API 키를 `OPENAI_API_KEY` 환경 변수에 설정합니다. OpenAI 계정 설정에서 API 키를 확인할 수 있습니다 ([https://platform.openai.com/login](https://platform.openai.com/login)).
4. (선택 사항) `OPENAI_MODEL_NAME` 환경 변수를 원하는 LLM 모델로 설정합니다 (기본값: "gpt-4-0125-preview"). <모델 context 사이즈가 작으면 텍스트 입력 과정에서 오류가 발생합니다.>

**사용 방법:**

1. crew_ai.py 파일에서 OpenAI API KEY를 변경하세요
2. 코드 145번째의 company에 희망하는 회사를 입력하세요
3. CrewAI 에이전트가 협력하여 정보를 수집하고, 데이터를 분석하고, 보고서를 생성합니다.
4. 최종 투자 추천은 "investment_recommendation.md" 파일로 저장됩니다.


**참고:**
* 이는 기본적인 예시이며, 추가 기능 및 기능을 포함하도록 확장될 수 있습니다.
* 테스트 목적으로 샘플 회사 데이터를 추가하는 것이 좋습니다.
* OpenAI API를 책임감 있게 사용하고 서비스 약관을 준수하십시오.
* 본 코드를 실행하며 얻은 결과로 한 투자에 대한 책임은 본인에게 있습니다.(저도 연습 중입니다)
