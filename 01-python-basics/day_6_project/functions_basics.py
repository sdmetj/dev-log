# --- 1. 기본적인 함수 정의와 호출 ---
print("--- 1. 기본적인 함수 정의와 호출 ---")

# 매개변수, 반환값도 없는 간단한 함수
def greet():
    print("안녕하세요, 휴먼")

# 함수 호출
greet()
greet()

def line():
    print("-" * 30)

line() # 구분 선 함수

# --- 2. 매개변수(Parameter)와 인자(Argument)

print("--- 2. 매개변수와 인자 ---")

# 이름을 매개변수로 받아 인사하는 함수
def greet_person(name):
    print(f"안녕하세요, {name}님!")
    
greet_person("로바트")
greet_person("리바이")

line()

# --- 3. return 문 (함수의 결과값 반환)
print("--- 3. return 문 --- ")

# 두 숫자를 받아 합을 반환하는 함수
def add_numbers(num1, num2): # 'num1','num2'가 매개변수
    sum_result = num1 + num2
    return sum_result # 계산된 결과를 함수를 호출한 곳으로 '반환'(출력의 개념인듯)

# 함수 호출 및 반환값 사용
result_from_add = add_numbers(10, 5) # 10과 5가 인자, 함수는 15를 반환, 그 값이 result_from_add
print(f"10 + 5의 결과: {result_from_add}")

# 다른 숫자들로 호출하고 반환값을 바로 출력
print(f"7 + 3의 결과: {add_numbers(7, 3)}")

line()

# --- 4. 매개변수 기본값 설정 ---
print("--- 4. 매개변수 기본값 설정 ---")

# 매개변수에 기본값을 설정하여 호출 시 값을 생략할 수 있게 함
def greet_with_default(name, greeting="안녕하세요"): # greeting의 기본값을 "안녕하세요"로 설정
    print(f"{greeting}, {name}!")
    
greet_with_default("라인")
greet_with_default("레니아", "반가워")
