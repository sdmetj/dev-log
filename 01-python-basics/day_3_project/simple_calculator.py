# --- 간단 계산기 프로그램 ---

print("간단 계산기 프로그램입니다.")

# 사용자로부터 첫 번째 숫자 입력 받기 (문자열로 입력됨)
input_str_num1 = input("첫 번째 숫자를 입력하세요: ")

# 사용자로부터 두 번째 숫자 입력 받기 (문자열로 입력됨)
input_str_num2 = input("두 번째 숫자를 입력하세요: ")

# 입력받은 문자열을 숫자로 변환 (실수형으로 변환하는 것이 나눗셈 등에서 유리)
num1 = float(input_str_num1)
num2 = float(input_str_num2)

# 사칙 연산 수행
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2 
div_result = num1 / num2 # 0으로 나누는 경우 오류 발생 가능성 있음

# 결과 출력
print("\n--- 계산 결과 ---")
print(f"{num1} + {num2} = {add_result}")
print(f"{num1} - {num2} = {sub_result}")
print(f"{num1} * {num2} = {mul_result}")
print(f"{num1} / {num2} = {div_result}")
print("-----------------\n")

print("계산이 완료되었습니다.")