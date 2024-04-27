# BDAV1 소개
- aSSIST(Seoul School of Integrated Sciences &amp; Technologies)의 AI 빅데이터 석사과정 9기(9-1,2) 빅데이터플랫폼 구축 강의 1조 리포지터리
- BDAV1는 "Big Data Analytics and Visualization Team 1"의 약자로, 환경관련 빅 데이터 분석과 시각화에 초점을 맞추어 자연환경을 보호하고 자원순환이 모두에게 이롭게 되도록하는 인사이트를 제공하려고 함.

## 로컬 환경에 리포지터리 클론
- [GitHub 리포지터리 페이지](https://github.com/arkwith7/BDAV1)로 이동.
- Code 버튼 클릭 후 나타나는 URL 복사.
- 로컬 컴퓨터에서 Git이 설치된 폴더로 이동 후, 터미널이나 명령 프롬프트를 열고 다음 명령어 입력:
```
git clone https://github.com/arkwith7/BDAV1
```

## 개발환경 구성
- 파이썬 가상환경 만들기(맥북,리눅스)
```
$ python -m venv venv
```
```
$ source venv/bin/activate
```
- python package 설치
```
$ pip install -r requirements.txt
```
- 윈도우에서 파이썬 가상환경 만들기
>> - 명령 프롬프트 열기: 시작 메뉴에서 'cmd'를 검색하고 명령 프롬프트를 엽니다.
>> - 프로젝트 폴더로 이동: cd 명령어를 사용하여 프로젝트 폴더로 이동합니다.
>> - 예: cd C:\Users\YourUsername\Documents\MyProject
>> 1. 가상환경 생성:
>>```
>>$ python -m venv venv
>>```
>>여기서 venv는 가상 환경의 이름입니다. 원하는 다른 이름을 사용할 수 있습니다.
>> 2. 가상환경 활성화:
>>```
>>$ venv\Scripts\activate
>>```
>>이 명령을 실행하면 가상 환경이 활성화되며, 프롬프트 앞에 (venv)가 표시됩니다.
>> 3. Python 패키지 설치
>> - 필요한 패키지가 명시된 requirements.txt 파일 확인: 이 파일에는 프로젝트에 필요한 모든 Python 패키지가 나열되어 있습니다.
>> - 패키지 설치:
>>```
>>$ pip install -r requirements.txt
>>```
>>이 명령은 requirements.txt 파일에 나열된 모든 패키지를 설치합니다.
>> 4. 작업 완료 후 가상환경 비활성화
>> - 작업을 마치고 가상환경을 비활성화하려면, 명령 프롬프트에서 다음 명령을 입력하세요:
>>```
>>$ deactivate
>>```
>>이 명령을 실행하면 가상 환경이 비활성화되고, 일반 시스템 환경으로 돌아갑니다.
