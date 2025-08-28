menu_items = [
    ("아메리카노", 3000),
    ("카페 라떼", 3500),
    ("카푸치노", 4000),
    ("에스프레소", 2500)
]

# --- 1. 메뉴판 출력 ---
print("--- 메뉴판 ---")
for i, item in enumerate(menu_items):
     menu_name = item[0]
     menu_price = item[1]
     print(f"{i+1}, {menu_name} ({menu_price}원)")
     
print("---------------")

# --- 2. 사용자로부터 주문 입력 받기 ---     
selected_menu_number_str = input("주문할 메뉴 번호를 입력하세요: ")
quantity_str = input("수량을 입력하세요: ")

# --- 3. 입력값 숫자형으로 변환 ---
# 사용자가 입력한 문자열 메뉴 번호를 정수로 변환(주문처리를 위한 사전 공정)
selected_menu_number = int(selected_menu_number_str)
# 사용자가 입력한 문자열 수령을 정수로 변환("")
order_quantity = int(quantity_str)

# --- 4. 주문 처리 ---
if 1 <= selected_menu_number <= len(menu_items):
    menu_number = selected_menu_number - 1
    selected_menu_tuple = menu_items[menu_number]
    
    final_menu_name = selected_menu_tuple[0]
    final_menu_price = selected_menu_tuple[1]
    # 총 가격 계산
    total_order_price = final_menu_price * order_quantity
    
    #최종 결과 출력
    print(f"선택하신 메뉴: {final_menu_name}, 가격: {final_menu_price}원")
    print(f"결제하실 금액은 {total_order_price}원 입니다.")
    print("-------------------------------")
    print("주문이 완료되었습니다. 감사합니다!")
    
else:
    
    print("유효하지 않은 메뉴 번호입니다. 프로그램을 종료합니다.")
    exit()
    