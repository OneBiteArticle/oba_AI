# OBA 서버 구조 분리 (Spring Backend & FastAPI AI Service)

## 개요
OBA(One Bite Article)는 IT 기사를 기반으로 AI가 자동으로 요약, 키워드, 퀴즈를 생성하는 **AI 기반 학습 서비스**입니다.  
이 프로젝트는 **두 개의 서버로 구성**되어 있으며, 각각의 역할과 기술 스택이 다릅니다.

---

## 서버 구성 개요

| 서버명 | 주요 역할 | 기술 스택 | 실행 환경 |
|--------|------------|-------------|-------------|
| **oba_backend** | 사용자 관리, 인증, 기사/퀴즈 API 제공 (핵심 백엔드) | Java / Spring Boot | IntelliJ |
| **oba_ai_service** | OpenAI API를 통한 AI 분석 및 콘텐츠 생성 (AI 연산 전용) | Python / FastAPI | VSCode |

---

## 서버 분리의 이유와 목적

### **역할과 책임 분리 (Separation of Concerns)**
- Spring 서버는 **서비스 로직, 데이터 관리, 보안, 인증** 중심입니다.  
- FastAPI 서버는 **AI 연산(GPT 호출, 뉴스 분석, 퀴즈 생성)** 전용입니다.  
→ 두 서버의 역할을 명확히 구분함으로써 **코드 복잡도를 낮추고 유지보수성을 향상**시킵니다.

---

### **기술 스택의 독립성 확보**
| 항목 | Spring (Backend) | FastAPI (AI Service) |
|------|------------------|----------------------|
| 언어 | Java | Python |
| 빌드 도구 | Gradle / Maven | pip / requirements.txt |
| 실행 환경 | JVM | Uvicorn |
| 주요 프레임워크 | Spring Boot | FastAPI |

> 서로 다른 생태계를 사용하는 만큼, 한 프로젝트에 섞어 관리하면  
의존성 충돌, 빌드 환경 불일치, 테스트 파이프라인 꼬임 등의 문제가 발생합니다.  
→ 각 서버를 **독립 리포지토리로 관리**하는 것이 가장 안정적입니다.

---

### **배포 및 운영 효율성 향상**
- Spring 서버와 FastAPI 서버는 **서로 다른 배포 주기**를 가집니다.  
  - 예) Spring → API 변경 / DB 업데이트  
  - FastAPI → AI 프롬프트 수정 / 모델 변경  
- 서버를 분리하면 **각각 독립적으로 배포, 롤백, 버전 관리**가 가능합니다.

---

### **보안 및 환경 변수 관리 분리**
- FastAPI는 `OPENAI_API_KEY`, `ORG_ID`, `PROJECT_ID` 등 **민감한 AI 관련 키**를 필요로 합니다.  
- Spring 서버에는 이런 키가 필요하지 않습니다.  
→ `.env` 파일, `.gitignore`, Docker 환경 변수 설정을 **각 서버별로 독립 관리**할 수 있습니다.

---

### **확장성과 마이크로서비스 아키텍처(MSA) 기반 구조**
- AI 서버를 별도로 구성하면 **AI 기능만 확장/스케일링** 가능 (예: GPU 전용 서버)  
- 추후 GPT 외 Gemini, Claude, HyperCLOVA 등 다른 모델을 추가하기 용이  
- Spring 서버는 API Gateway 역할로 고정, AI 서버는 Worker 역할로 확장 가능
