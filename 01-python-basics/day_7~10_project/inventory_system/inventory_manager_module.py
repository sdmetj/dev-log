import json
from .product_module import Product, ToolProduct

class InventoryManager: 
    def __init__(self):
        # 시작할 때 재고 데이터를 파일에서 불러옴
        self.products = self.load_products_data()
        
        # 만약 파일이 비어있거나 불러오기 실패했다면, 기본 상품들을 추가
        if not self.products:
            print("초기 상품 데이터를 불러오거나 생성합니다.")
        
            self.products = [
                Product("철 검", 1000, 10),
                Product("고목나무 지팡이", 2500, 20),
                Product("중급 회복물약", 500, 100),
                ToolProduct("나무 곡괭이", 100, 5, 50),
                ToolProduct("다이아몬드 도끼", 50000, 1, 1500)
            ]
            # 초기 데이터를 파일에 한번 저장
            self.save_products_data()
            
    # 재고 데이터를 파일에 저장하는 메서드
    def save_products_data(self):
        data_to_save = []
        for product in self.products:
            product_data = {
                "name": product.name,
                "price": product.price,
                "stock": product.stock,
                # ToolProduct일 경우 durability 속성도 저장
                "type": "ToolProduct" if isinstance(product, ToolProduct) else "Product",
                "durability": product.durability if isinstance(product, ToolProduct) else None
            }
            data_to_save.append(product_data)
            
        with open("inventory_data.json", "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4, ensure_ascii=False) # indent로 보기 좋게, ensure_ascii=False로 한글 깨짐 방지
        print("\n>> 재고 데이터가 'inventory_data.json'에 저장되었습니다.")
    
    def load_products_data(self):
        try:
            with open("inventory_data.json", "r", encoding="utf-8") as f:
                loaded_data = json.load(f)
            
            products_list = []
            for item_data in loaded_data:
                # 저장된 타입에 따라 적절한 클래스의 객체를 생성
                if item_data.get("type") == "ToolProduct":
                    products_list.append(ToolProduct(
                        item_data["name"],
                        item_data["price"],
                        item_data["stock"],
                        item_data["durability"]
                    ))
                else:
                    products_list.append(Product(
                        item_data["name"],
                        item_data["price"],
                        item_data["stock"]
                    ))
            print(">> 기존 재고 데이터를 'inventory_data.json'에서 불러왔습니다.")
            return products_list
        except FileNotFoundError:
            print(">> 'inventory_data.json' 파일을 찾을 수 없습니다. 새로운 데이터를 시작합니다.")
            return [] # 파일이 없으면 빈 리스트 반환
        except json.JSONDecodeError:
            print(">> 'inventory_data.json' 파일 형식이 잘못되었습니다. 새로운 데이터를 시작합니다.")
            return [] # JSON 파싱 오류 시  빈 리스트 반환
        except Exception as e:
            print(f">> 데이터 로드 중 알 수 없는 오류 발생: {e}. 새로운 데이터를 시작합니다.")
            return []
    def display_products(self): # 모든 상품 디스플레이 함수
        print("\n--- 모든 상품 목록 ---")
        if not self.products: # 상품 리스트가 비어있다면
            print("등록된 상품이 없습니다.")
        else: # 상품이 있을 때
            for i, product_obj in enumerate(self.products):
                print(f"{i+1}. {product_obj.get_info_string()}")
        print("------------------------")
            
    def update_product_stock(self):
        print("\n--- 현재 재고 상태 ---")
        self.display_products()
    
        try:
           selected_product_number_str = input("재고를 업데이트할 상품 번호를 입력하세요: ")
           selected_product_number = int(selected_product_number_str)
           # 임시 출력(변환 확인 용도)
           # print(f"선택된 상품 번호 (숫자): {selected_product_number}")
           
        except ValueError: # int() 변환 시 숫자가 아닌 것을 입력했을 때 발생
                print("유효하지 않은 상품 번호입니다. 숫자를 입력해주세요.")
        else:
            
            if 1 <= selected_product_number <= len(self.products):
                actual_index = selected_product_number - 1
                product_to_update = self.products[actual_index] # 여기서 Product 객체를 가져옴
                
                print(f"유효한 상품 번호를 선택했습니다! (선택된 번호: {selected_product_number})")
                
                try:
                    new_stock_str = input("새로운 재고 수량을 입력하세요: ")
                    new_stock = int(new_stock_str) # 변수명 변경
                    
                    if product_to_update.update_stock(new_stock):
                        print(f"'{product_to_update.name}'의 재고가 {new_stock}개로 업데이트되었습니다.")
                        
                        print("------------------------")
                                            
                    else:
                        print("재고 수량은 음수가 될 수 없습니다.")
                
                except ValueError:
                    print("유효하지 않은 재고 수량입니다. ")
            else:
                print(f"유효하지 않은 상품 번호입니다. 1부터 {len(self.products)} 사이의 숫자를 입력해주세요.")
    
    
    def calculate_and_display_total_value(self):
        print("\n--- 총 재고 가치 합계 ---")
        
        #1. 총 가치를 저장할 변수를 0으로 촉화
        total_value = 0
        
        for product_obj in self.products:
            
            total_value += product_obj.calculate_total_value()
            
        # 3. 최종 출력
        print(f"현재 총 재고 가치는 {total_value}원 입니다.")
        print("-----------------------")