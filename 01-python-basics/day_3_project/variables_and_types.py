# --- 변수 선언과 값 할당 ---
# int (정수) 자료형
student_id = 2023001
year = 2025

# float (실수) 자료형
gravity = 9.81
temperature = 25.5

# str (문자열) 자료형
item_name = "스마트폰"
product_category = '전자제품'
programming_lang = "파이썬을 통한 코딩은 '유용하다'!"

# bool (참/거짓) 자료형
is_active = True
has_discount = False

# --- 변수 값 출력해보기 ---
print("---변수 값 출력 ---")
print("아이템 이름:", item_name)
print("학생 ID:", student_id)
print("중력 가속도:", gravity)
print("활성화 상태인가요?", is_active)
print("-" * 20) # 구분선 출력

# --- 변수의 자료형 확인해보기 ---
# type() 함수를 사용하면 변수의 자료형을 알 수 있어
print("--- 변수 자료형 확인 ---")
print("student_id 변수의 자료형:", type(student_id))
print("item_name 변수의 자료형:", type(item_name))
print("gravity 변수의 자료형:", type(gravity))
print("is_active 변수의 자료형:", type(is_active))
print("-" * 20)

# --- 변수를 이용한 연산 ---
# 숫자 변수는 사칙 연산이 가능하다
price = 100
quantity = 3
total_cost = price * quantity

speed = 60.5
time = 2.0
distance = speed * time

print("--- 변수 연산 결과 ---")
print("상품 총 가격:", total_cost)
print("이동 거리:", distance)
print("-" * 20)

# 문자열 변수는 덧셈으로 이어 붙이거나 곱셈으로 반복할 수 있다.
full_phrase = product_category + " - " + item_name
print("전체 구절:", full_phrase)

warning_message = "경고! " * 2
print("경고 메세지:", warning_message)
print("-" * 20)

# 자료형 변환 (예시)
str_id = str(student_id) # 정수 student_id를 문자열로 변환
print("문자열로 변환된 ID:", str_id, type(str_id))

num_from_str = int("456") # 문자열 "456"을 정수로 변환
print("정수로 변환된 숫자:", num_from_str, type(num_from_str))