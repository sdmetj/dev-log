from inventory_system.inventory_manager_module import InventoryManager

# --- 재고 관리 시스템 메뉴 ---
print("\n---재고 관리 시스템 메뉴---")
print("1. 상품 목록 보기")
print("2. 재고 업데이트")
print("3. 총 재고 가치 합계")
print("4. 종료")

manager = InventoryManager()

# 무한 루프 시작
while True:
    choice = input("\n원하시는 메뉴를 선택해주세요.(1-4): ")
    
    # 1. 상품 목록 보기
    if choice == '1':
        manager.display_products()
    
    elif choice =='2':
        print("\n--- 현재 재고 상태 ---")
        
        manager.update_product_stock()
        
    elif choice == '3':
        manager.calculate_and_display_total_value()
        
    elif choice == '4':
        manager.save_products_data() # <<< 종료 전에 데이터 저장
        print("재고 관리 시스템을 종료합니다.")
        break