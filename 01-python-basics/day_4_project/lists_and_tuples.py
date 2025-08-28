# --- 1. 리스트 사용하기 ---
print("---리스트 실습---")

# 리스트 생성
fruits = ["apple", "banana", "cherry"]
print("초기 과일 리스트:", fruits)

# 요소 접근 (인덱스는 0부터 시작)
print("첫 번째 과일:", fruits[0]) # apple
print("세 번째 과일:", fruits[2]) # cherry

# 리스트 길이 확인
print("리스트 길이:", len(fruits))

# 요소 추가 (맨 뒤에)
fruits.append("orange")
print("orange 추가 후:", fruits)

# 요소 삽입(특정 위치에)
fruits.insert(1, "grape")
print("grape 삽입 후:", fruits)

# 요소 수정
fruits[0] = "kiwi"
print("apple -> kiwi 수정 후:", fruits)

# 요소 삭제 (값으로  삭제)
fruits.remove("grape")
print("grape 삭제 후:", fruits)

# 요소 삭제 (인덱스로 삭제)
del fruits[2] # "cherry" 삭제
print("인덱스 2 삭제 후:", fruits)

# 리스트 슬라이싱 (부분 List 추출)
selected_fruits = fruits[0:2] # 인덱스 0부터 1까지 (끝 인덱스 2는 포함 안됨)
print("슬라이싱 (0~1):", selected_fruits)

print("-" * 30)

# --- 2. 튜플 사용하기 ---
coordinates = (10, 20)
colors = ("red", "green", "blue")
print("초기 좌표 튜플:", coordinates)
print("초기 색상 튜플:", colors)

# 요소 접근
print("첫 번째 좌표:", coordinates[0])
print("두 번째 색상:", colors[1])

# 튜플 길이 확인
print("튜플 길이:", len(colors))

# Tuple 슬라이싱 (List처럼 가능)
primary_colors = colors[0:2]
print("슬라이싱 (0~1):", primary_colors)

# 튜플 수정/추가/삭제 시도 (주석 해제 시 에러 발생!)
# coordinates[0] = 30 # TypeError: 'tuple' object does not support item assignment
# colors.append("yellow") # AttributeError: 'tuple' object has no attribute 'append'

print("튜플은 생성 후 수정/추가/삭제할 수 없습니다.")
print("-" * 30)