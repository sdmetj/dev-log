# --- 쇼핑 리스트 관리 프로그램 ---

shopping_list = [] # 빈 리스트로 시작

while True: # 무한 반복 (사용자가 종료하기 전까지 계속 메뉴 보여줌)
    print("\n--- 쇼핑 리스트 관리 ---")
    print("1, 쇼핑 리스트 보기")
    print("2. 아이템 추가")
    print("3, 아이템 삭제")
    print("4, 종료")
    
    choice = input("선택: ")
    
    if choice == '1': # '1'을 선택했을 때
        if not shopping_list: # 리스트가 비어있는지 확인 (비어있으면 True)
            print("쇼핑 리스트가 비어 있습니다.")
        else:
            print("\n--- 현재 쇼핑 리스트 ---")
            # euumerate는 리스트의 요소와 인덱스를 동시에 반환해준다.
            for i, item in enumerate(shopping_list):
                print(f"{i+1}, {item}") # 사용자에게는 1번부터 보여주기 위해 i+1
            print("------------------------")
            
    elif choice == '2': # '2'를 선택했을 때
        item = input("추가할 아이템 이름: ")
        shopping_list.append(item) # 리스트 맨 뒤에 아이템 추가
        print(f"'{item}'이(가) 리스트에 추가되었습니다.")
    
    elif choice == '3': # '3'을 선택했을 때
        if not shopping_list:
            print("삭제할 아이템이 없습니다.")
            continue # 현재 반복을 건너뛰고 다음 반복(메뉴 출력)으로 넘어감
        
        print("\n--- 현재 쇼핑 리스트 (삭제용) ---")
        for i, item in enumerate(shopping_list):
            print(f"{i+1}, {item}")
        print("---------------------------------")
        
        try: # 에러가 발생할 가능성이 있는 코드를 감싸는 블록
            item_index = int(input("삭제할 아이템 번호 (숫자): ")) #문자열을 숫자로 변환
            if 1 <= item_index <= len(shopping_list): # 유효한 인덱스인지 확인
                #pop()은 해당 인덱스의 요소를 삭제하고 그 요소를 반환해줌
                remove_item = shopping_list.pop(item_index - 1) # 사용자 입력은 1번부터이므로 -1
                print(f"'{remove_item}'이(가) 리스트에서 삭제되었습니다.")
            else:
                print("유효하지 않은 아이템 번호입니다.")
        except ValueError: # int() 변환 실패 시 (숫자가 아닌 것을 입력했을 때)
            print("유효하지 않은 입력입니다. 숫자를 입력해주세요.")
    elif choice == '4': # '4'를 선택했을 때
        print("쇼핑 리스트 관리를 종료합니다.")
        break # while 반복문을 완전히 종료
    
    else: # 1,2,3,4 외의 다른 것을 입력했을 때
        print("유효하지 않은 선택입니다. 다시 입력해주세요.")