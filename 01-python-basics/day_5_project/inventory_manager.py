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
        if not products:
            print("등록된 상품이 없습니다.")
    
        for i, product_data in enumerate(products):
            product_name = product_data["name"]
            product_price = product_data["price"]
            product_stock = product_data["stock"]
            
            print(f"{i+1}. {product_name} (가격: {product_price}원, 재고: {product_stock}개)")
        print("------------------------")
