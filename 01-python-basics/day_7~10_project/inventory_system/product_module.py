import json

# --- 재고 관리 시스템 ---

class Product: #Product 클래스 정의 시작
    def __init__(self, name, price, stock):
        self.name = name   # 상품 이름
        self.price = price # 상품 가격
        self.stock = stock # 상품 재고
    
    # 1. 재고를 업데이트 하는 메서드 (외부에서 받은 값으로 내부 재고를 변경)
    def update_stock(self, new_stock_quantity):
        if new_stock_quantity >= 0: # 재고는 음수가 될 수 없음
            self.stock = new_stock_quantity
            return True # 업데이트 성공
        else:
            return False # 업데이트 실패
    
    # 2. 한 상품의 총 가치를 계산해서 반환하는 메서드 
    def calculate_total_value(self):
        return self.price * self.stock
    
    # 3. 자신의 정보를 문자열로 반환하는 메서드 (나중에 print() 함수에서 더 깔끔하게 사용 가능)
    def get_info_string(self):
        return f"{self.name} (가격: {self.price}원, 재고: {self.stock}개)"

class ToolProduct(Product): # Product를 상속받음
    def __init__(self, name, price, stock, durability):
        
        # Product의 속성을 초기화함 
        super().__init__(name, price, stock)
        self.durability = durability
    def get_info_string(self):
        # 부모가 제공하는 기본 정보 문자열을 가져옴
        base_info = super().get_info_string()
        return f"{base_info}, 내구도: {self.durability}"
