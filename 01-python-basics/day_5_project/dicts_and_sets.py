# --- 1. 딕셔너리 (Dictionary) 실습 ---
print("--- 딕셔너리(Dictionary) 실습 ---")

# 딕셔너리 생성
student = {
    "학번": "2023001",
    "이름": "춘식왕",
    "학과": "컴퓨터공학과",
    "성적": "4.2"
}
print("초기 학생 정보:", student)

# 값 접근 (키를 이용)
print("학생 이름:", student["이름"])
print("학생 학과:", student["학과"])

# 값 수정 (기존 키에 새로운 값 할당)
student["성적"] = 4.3
print("성적 수정 후:", student)

# 새 키-값 쌍 추가
student["전화번호"] ="010-XXXX-XXXX"
print("전화번호 추가 후:", student)

# 키-값 쌍 삭제 (del 키워드)
del student["학번"]
print("학번 삭제 후:", student)

# 딕셔너리 주요 메소드
print("모든 키:", student.keys())
print("모든 값:", student.values())
print("모든 키-값 쌍:", student.items())

print("-" * 30)

# --- 2. 세트 (Set) 실습 ---
print("--- 세트(Set) 실습 ---")

# 세트 생성 (중복된 값은 제거됨)
numbers = {1, 2, 3, 2, 1, 4, 5}
print("초기 숫자 세트:", numbers) # 출력: {1, 2, 3, 4, 5} (순서는 다를 수 있음)

# 요소 추가 (.add())
numbers.add(6)
print("6 추가 후:", numbers)

numbers.add(3) # 이미 있는 값은 추가되지 않음
print("3 추가 시도 후 (변화 없음):", numbers)

# 없는 요소 삭제 시도 (주석 해제 시 에러 발생!)
# numbers.remove(10) # KeyError: 10

# 다른 세트와 집합 연산 (추후에 더 자세하게 공부할 예정)
set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}

print("세트 A:", set_A)
print("세트 B:", set_B)
print("합집합 (A | B):", set_A | set_B) # 모든 고유한 요소
print("교집합 (A & B):", set_A & set_B) # 공통 요소
print("차집합 (B - A):", set_B - set_A) # A에는 있지만 B에는 없는 요소

print("-" * 30)