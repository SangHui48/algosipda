import re

def SimplePassword(strParam):
    # 길이 조건을 확인
    if len(strParam) <= 7 or len(strParam) >= 31:
        return "false"
    
    # 문자열에 'password'가 포함되어 있는지 확인
    if "password" in strParam.lower():
        return "false"
    
    # 정규표현식을 사용하여 대문자, 숫자, 구두점(특수 문자) 조건을 확인
    has_capital = re.search(r'[A-Z]', strParam)
    has_number = re.search(r'[0-9]', strParam)
    has_punctuation = re.search(r'[^\w\s]', strParam)  # 구두점 및 특수 문자 확인 (단어 문자와 공백 제외)

    if has_capital and has_number and has_punctuation:
        return "true"
    else:
        return "false"

# 이 함수 호출을 유지하세요 
print(SimplePassword(input()))
