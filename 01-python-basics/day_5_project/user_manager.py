# --- 사용자 정보 관리 프로그램 ---

users = {
    "user_001" : {"name": "프리렌", "job" : "wizard", "age": 1000},
    "user_002" : {"name": "페른", "job" : "wizard", "age": 20}

}

# 프로그램 메뉴 출력
print("--- 사용자 관리 메뉴 ---")
print("1. 모든 사용자 정보 보기")
print("2. 사용자 추가")
print("3. 사용자 정보 수정")
print("4. 사용자 삭제")
print("5. 종료")

# 무한 루프 시작
while True:
    choice = input("\n메뉴를 선택하세요 (1-5: ")
    
    # 1. 모든 사용자 정보 보기
    if choice == '1':
        print("\n--- 모든 사용자 정보 ---")
        if not users:
            print("등록된 사용자가 없습니다.")
        else:
            for user_id, user_info in users.items():
                print(f"ID: {user_id}")
                
                for key, value in user_info.items():
                    print(f"  {key}: {value}")
                print("-" * 10)
        print("---------------------")
    # 2. 사용자 추가 기능
    elif choice == '2':
        new_id = input("새 사용자 ID: ")
        if new_id in users:
            print("이미 존재하는 ID입니다. 다른 ID를 사용해주세요.")
        else:
            name = input("이름: ")
            job = input("직업: ")
            age = int(input("나이: "))
            users[new_id] = {"name": name, "job": job, "age": age}
            print(f"사용자 '{new_id}'가 추가되었습니다.")
        
    # 3. 사용자 정보 수정 기능
    elif choice == '3':
        target_id = input("정보를 수정할 사용자 ID: ")
        if target_id not in users: 
            print("존재하지 않는 사용자 ID입니다.")
        else:
            # 해당 사용자의 현재 정보를 출력
            print(f"사용자 '{target_id}'의 현재 정보: {users[target_id]}")
            field_to_update = input("수정할 항목 (name, job, age): ") # 어떤 항목을 수정할지 입력 받기
            
            # 입력받은 항목이 해당 사용자의 정보 딕셔너리 안에 존재하는지 확인
            if field_to_update in users[target_id]:
                new_value = input(f"새로운 {field_to_update} 값: ")
                
                # 나이 항목일 경우 정수로 변환
                if field_to_update == "age":
                    new_value = int(new_value)
                    
                # 해당 항목의 값 업데이트
                users[target_id][field_to_update] = new_value
                print(f"'{target_id}'의 {field_to_update}가 업데이트되었습니다.")
            else:
                print("유효하지 않은 항목입니다. (name, job, age 중 선택해주세요)")
                
    # 4. 사용자 삭제 기능
    elif choice == '4':
        target_id = input("삭제할 사용자 ID: ")
        if target_id not in users:
            print("존재하지 않는 사용자 ID입니다.")
        else:
            del users[target_id]
            print(f"사용자 '{target_id}'가 삭제되었습니다.")
            
    elif choice == '5':
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("유효하지 않은 선택입니다. 다시 시도해주세요.")