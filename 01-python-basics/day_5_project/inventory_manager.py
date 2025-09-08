# --- 재고 관리 시스템 ---

class Product: #Product 클래스 정의 시작
    def __init__(self, name, price, stock):
        self.name = name   # 상품 이름
        self.price = price # 상품 가격
        self.stock = stock # 상품 재고
        

#products = [
    #{"name": "철 검", "price": 1000, "stock": 10},
    #{"name": "고목나무 지팡이", "price": 2500, "stock": 20},
    #{"name": "중급 회복물약", "price": 500, "stock": 100}

#]

products = [
    Product("철 검", 1000, 10),
    Product("고목나무 지팡이", 2500, 20),
    Product("중급 회복물약", 500, 100)
]



def display_products(): # 모든 상품 디스플레이 함수
    print("\n--- 모든 상품 목록 ---")
    if not products: # 상품 리스트가 비어있다면
            print("등록된 상품이 없습니다.")
    else: # 상품이 있을 때
        for i, product_obj in enumerate(products):
                product_name = product_obj.name   # .name
                product_price = product_obj.price # .price
                product_stock = product_obj.stock # .stock
                print(f"{i+1}. {product_name} (가격: {product_price}원, 재고: {product_stock}개)")
        print("------------------------")
        
def update_product_stock():
    try:
           selected_product_number_str = input("재고를 업데이트할 상품 번호를 입력하세요: ")
           selected_product_number = int(selected_product_number_str)
           # 임시 출력(변환 확인 용도)
           # print(f"선택된 상품 번호 (숫자): {selected_product_number}")
           
    except ValueError: # int() 변환 시 숫자가 아닌 것을 입력했을 때 발생
                print("유효하지 않은 상품 번호입니다. 숫자를 입력해주세요.")
    else:
            
            if 1 <= selected_product_number <= len(products):
                
                # 왜 여기서 인덱스 계산을 하는거지?
                actual_index = selected_product_number - 1
                # 왜 여기로 옮긴거지?
                product_to_update = products[actual_index] # 여기서 Product 객체를 가져옴
                
                print(f"유효한 상품 번호를 선택했습니다! (선택된 번호: {selected_product_number})")
                
                try:
                    new_stock_str = input("새로운 재고 수량을 입력하세요: ")
                    new_stock = int(new_stock_str) # 변수명 변경
                    
                    if new_stock >= 0:
                        
                        # Product 객체로 변경했기 때문에 코드도 바뀌어야함
                        product_to_update.stock = new_stock
                        
                        # 업데이트 완료 메시지 출력
                        print(f"'{product_to_update.name}'의 재고가 {new_stock}개로 업데이트되었습니다.")
                        
                        print("------------------------")
                        
                    
                    else:
                        print("재고 수량은 음수가 될 수 없습니다.")
                
                except ValueError:
                    print("유효하지 않은 재고 수량입니다. ")
            else:
                print(f"유효하지 않은 상품 번호입니다. 1부터 {len(products)} 사이의 숫자를 입력해주세요.")
    
def calculate_and_display_total_value():
    print("\n--- 총 재고 가치 합계 ---")
        
        #1. 총 가치를 저장할 변수를 0으로 촉화
    total_value = 0
        
    for product_obj in products:
            price = product_obj.price
            stock = product_obj.stock
            
            item_value = price * stock
            
            total_value += item_value
            
        # 3. 최종 출력
    print(f"현재 총 재고 가치는 {total_value}원 입니다.")
    print("-----------------------")
    
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
        display_products()
    
    elif choice =='2':
        print("\n--- 현재 재고 상태 ---")
        display_products()  
        update_product_stock()
        
    elif choice == '3':
        calculate_and_display_total_value()
        
    elif choice == '4':
        print("재고 관리 시스템을 종료합니다.")
        break