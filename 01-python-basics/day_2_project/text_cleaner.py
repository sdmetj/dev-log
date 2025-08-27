# 간단 텍스트 정리기

#1. 사용자 입력 받기
text = input("문장을 입력하세요: ")

#2. 문자열 다듬기
cleaned = text.strip() # 앞뒤 공백 제거
cleaned = cleaned.lower() # 소문자로 변환

#3. 출력
print("정리된 문장:", cleaned)

#4. 공백을 기준으로 나눈 뒤 다시 합치기
words = cleaned.split()   # 리스트로 나누기 
cleaned = " ".join(words) # 다시 공백 하나로 합치기

print("최종 정리된 문장:", cleaned)