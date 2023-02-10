# 케이씨넷 빅데이터분석팀 미니 프로젝트 API

`2023.02.10` 세 가지 기능 제공
- 케이씨넷 결재 문서 번호 추출
  - easyocr 을 활용한 OCR
- 한글 파일 텍스트 추출
  - hwp 파일일 경우
    - olefile 활용
    - olefile 로 안될 시, hwp5txt 활용(윈도우일 경우만)
  - hwpx 파일일 경우
    - xml 텍스트 추출
- ko-GPT2 기반 문장 생성 기능 추가
  - [SKT-AI/KoGPT2](https://github.com/SKT-AI/KoGPT2) 모델사용
  



