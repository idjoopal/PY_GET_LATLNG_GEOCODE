# 패키지 다운로드
## pip
### connection error : SSL: CERTIFICATE_VERIFY_FAILED
- 사설망 인증서 오류 : pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <패키지명> 

# 데이터 불러오기
## pandas read_csv()
### UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb1 in position 0: invalid start byte
- 인코딩 오류. 옵션으로 encoding = 'CP949' 추가
