# 다국어 분석기.py
from collections import Counter
import re
from tabulate import tabulate # pip install tabulate
import os  # exe에서 pause용

def analyze_text(text):
    text = input("분석할 문장을 입력하세요 (영어, 한국어, 일본어, 숫자, 특수문자 가능): ")
    
# 전체 글자 수
    total_chars = len(text)

# 공백 제외 글자 수
    chars_no_space = len(text.replace(" ",""))

# 영어 단어 수
    english_words = re.findall(r'\b[a-zA-Z]+\b', text)
    num_english_words = len(english_words)
    
# 영어 단어 (소문자)
    english_words_lower = [w.lower() for w in english_words]
    english_counter = Counter(english_words_lower)
    most_common_english = english_counter.most_common(1)
    
# 한국어/일본어 글자
    non_english_chars = [c for c in text if not c.isascii() and c != " "]
    num_non_english_chars = len(non_english_chars)
    non_english_counter = Counter(non_english_chars)
    most_common_non_english = non_english_counter.most_common(1)

# 숫자
    digits = [c for c in text if c.isdigit()]
    num_digits = len(digits)
    digits_counter = Counter(digits)
    most_common_digit = digits_counter.most_common(1)

# 특수문자 (공백 제외)
    special_chars = [c for c in text if not c.isalnum() and not c.isspace()]
    num_special = len(special_chars)
    special_counter = Counter(special_chars)
    most_common_special = special_counter.most_common(1)
    
# 영어 모음 
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)

# 표 형태 데이터 출력
    table_data = [
        ["전체 글자 수", total_chars],
        ["공백 제외 글자 수", chars_no_space],
        ["영어 단어 수", num_english_words],
        ["영어 모음 수", vowel_count],
        ["가장 많이 나온 영어 단어", most_common_english],
        ["비 영어 글자 수", num_non_english_chars],
        ["가장 많이 나온 비 영어 글자 수", most_common_non_english],
        ["숫자 개수", num_digits],
        ["가장 많이 나온 숫자", most_common_digit],
        ["특수문자 개수", num_special],
        ["가장 많이 나온 특수 문자", most_common_special],
    ]
    return table_data

def main():
    while True:
        text = input("\n문장을 분석하려면 아무 버튼이나 누르십시오. (종료하려면 'q' 입력): ")
        if text.lower() == 'q':
            print("프로그램을 종료합니다.")
            break
        
         # 입력 받은 text로 바로 분석
        result_table = analyze_text(text)
        print("\n=== 분석 결과 ===")
        print(tabulate(result_table, headers=["항목", "결과"], tablefmt="grid"))
        
    # Windows exe에서 콘솔 유지
    os.system("pause")


if __name__ == "__main__":
    main()