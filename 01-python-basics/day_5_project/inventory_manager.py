# --- 재고 관리 시스템 ---
products = [
    {"name": "철 검", "price": 1000, "stock": 10},
    {"name": "고목나무 지팡이", "price": 2500, "stock": 20},
    {"name": "중급 회복물약", "price": 500, "stock": 100}

]

# 메뉴 출력
print("\n---제고 관리 시스템 메뉴---")
print("1. 상품 목록 보기")
print("2. 재고 업데이트")
print("3. 총 재고 가치 합계")
print("4. 종료")

# 무한 루프 시작
while True:
    choice = input("\n원하시는 메뉴를 선택해주세요.(1-4): ")
    
    # 1. 상품 목록 보기
    if choice == '1':
        print("\n--- 모든 상품 목록 ---")
        if not products: # 상품 리스트가 비어있다면
            print("등록된 상품이 없습니다.")
        else: # 상품이 있을 때
            for i, product_data in enumerate(products):
                product_name = product_data["name"]
                product_price = product_data["price"]
                product_stock = product_data["stock"]
                print(f"{i+1}. {product_name} (가격: {product_price}원, 재고: {product_stock}개)")
        print("------------------------")
    
    elif choice =='2':
        print("\n--- 현재 재고 상태 ---")
        for i, product_data in enumerate(products):
            product_name = product_data["name"]
            product_stock = product_data["stock"]    
            print(f"{i+1}. {product_name} (재고: {product_stock}개)")
        print("------------------------")    
        
        try:
           selected_product_number_str = input("재고를 업데이트할 상품 번호를 입력하세요: ")
           selected_product_number = int(selected_product_number_str)
           # 임시 출력(변환 확인 용도)
           # print(f"선택된 상품 번호 (숫자): {selected_product_number}")
           
        except ValueError: # int() 변환 시 숫자가 아닌 것을 입력했을 때 발생
            print("유효하지 않은 상품 번호입니다. 숫자를 입력해주세요.")
        else:
            
            if 1 <= selected_product_number <= len(products):
                print(f"유효한 상품 번호를 선택했습니다! (선택된 번호: {selected_product_number})")
                
                try:
                    new_stock_str = input("새로운 재고 수량을 입력하세요: ")
                    new_stock = int(new_stock_str) # 변수명 변경
                    
                    if new_stock >= 0:
                        
                        # 실제 인덱스 계산
                        actual_index = selected_product_number - 1
                        
                        # products 리스트에서 해당 상품 딕셔너리 가져오기
                        product_to_update = products[actual_index]
                        
                        # 상품 딕셔너리의 'stock' 값 업데이트
                        product_to_update["stock"] = new_stock
                        
                        # 업데이트 완료 메시지 출력
                        print(f"'{product_to_update['name']}'의 재고가 {new_stock}개로 업데이트되었습니다.")
                        
                        print("------------------------")
                        
                    
                    else:
                        print("재고 수량은 음수가 될 수 없습니다.")
                
                except ValueError:
                    print("유효하지 않은 재고 수량입니다. ")
            else:
                print(f"유효하지 않은 상품 번호입니다. 1부터 {len(products)} 사이의 숫자를 입력해주세요.")
    
    elif choice == '3':
        print("\n--- 총 재고 가치 합계 ---")
        
        #1. 총 가치를 저장할 변수를 0으로 촉화
        total_value = 0
        
        for product_data in products:
            price = product_data["price"]
            stock = product_data["stock"]
            
            item_value = price * stock
            
            total_value += item_value
            
        # 3. 최종 출력
        print(f"현재 총 재고 가치는 {total_value}원 입니다.")
        print("-----------------------")
        
    elif choice == '4':
        print("재고 관리 시스템을 종료합니다.")
        break