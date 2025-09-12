# --- 1. 스택 (Stack) 구현 ---
class Stack:
    def __init__(self):
        # 스택의 데이터를 저장할 리스트, 가장 뒤가 스택의 '상단'이 된다.
        self._items = []
    
    def push(self, item):
        # 스택의 상단에 데이터를 추가한다. (리스트의 append와 동일)
        self._items.append(item)
        print(f"PUSH: {item} -> 현재 스택: {self._items}")
        
    def pop(self):
        # 스택의 상단에서 데이터를 제거하고 반환한다.
        # 스택이 비어있으면 오류를 발생시킨다.
        if not self.is_empty():
            popped_item = self._items.pop()
            print(f"POP: {popped_item} <- 현재 스택: {self._items}")
            return popped_item
        else:
            print("스택이 비어있어 POP 할 수 없습니다.")
            return IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self._items[-1]
        else:
            print("스택이 비어있어 PEEK 할 수 없습니다.")
            return None
    
    def is_empty(self):
        # 스택이 비어있는지 확인한다.
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
# --- 스택 동작 테스트 ---
if __name__ == "__main__": # 이 코드는 이 파일이 직접 실행될 떄만 작동한다.
    print("=== 스택 테스트 시작 ===")
    my_stack = Stack()
    
    print(f"스택이 비어있나요? {my_stack.is_empty()}") # True
    
    my_stack.push("첫 번째 책")
    my_stack.push("두 번째 책")
    my_stack.push("세 번째 책")
    
    print(f"스택 크기: {my_stack.size()}") #3
    print(f"스택 최상단: {my_stack.peek()}") # 세 번째 책
    
    my_stack.pop() # 세 번째 책
    print(f"스택 최상단: {my_stack.peek()}") # 두 번째 책
    
    my_stack.pop() # 두 번째 책
    my_stack.pop() # 첫 번째 책
    my_stack.pop() # 스택이 비어있어 POP 할 수 없습니다.
    
    print(f"스택이 비어있나요? {my_stack.is_empty()}") # True
    print("=== 스택 테스트 완료 ===")
    
    from collections import deque # 큐 구현에 효율적인 deque를 불러온다.
    
    # --- 2. 큐 (Queue) 구현 ---
    class Queue:
        def __init__(self):
            # 큐의 데이터를 저장할 deque. 양쪽 끝에서 빠른 추가/제거가 가능하다.
            self._items = deque()
        
        def enqueue(self, item):
            # 큐의 뒤쪽에 데이터를 추가합니다.
            self._items.append(item)
            print(f"ENQUEUE: {item} -> 현재 큐: {list(self._items)}") # 출력 시 deque를 list로 변환
        
        def dequeue(self):
            # 큐의 앞쪽에서 데이터를 제거하고 반환한다.
            if not self.is_empty():
                dequeued_item = self._items.popleft() # deque의 popleft()는 0(1)
                print(f"DEQUEUE: {dequeued_item} <- 현재 큐: {list(self._items)}")
                return dequeued_item
            else:
                print("큐가 비어있어 DEQUEUE 할 수 없습니다.")
                return None
        
        def peek(self):
            # 큐의 가장 앞에 있는 데이터를 제거하지 않고 반환한다.
            if not self.is_empty():
                return self._items[0]
            else:
                print("큐가 비어있어 PEEK 할 수 없습니다.")
                return None
        
        def is_empty(self):
            # 큐가 비어있는지 확인한다.
            return len(self._items) == 0
        
        def size(self):
            # 큐의 현재 크기를 반환한다.
            return len(self._items)
        
    # --- 큐 동작 테스트 ---   
    if __name__ == "__main__": # 이 코드는 이 파일이 직접 실행될 때만 작동한다.
        print("\n=== 큐 테스트 시작 ===")
        my_queue = Queue()
        
        print(f"큐가 비어있나요? {my_queue.is_empty()}") # True
        
        my_queue.enqueue("첫 번째 손님")
        my_queue.enqueue("두 번째 손님")
        my_queue.enqueue("세 번째 손님")
        
        print(f"큐 크기: {my_queue.size()}") # 3
        print(f"큐 맨 앞: {my_queue.peek()}") # 첫 번째 손님
        
        my_queue.dequeue() # 첫 번째 손님
        print(f"큐 맨 앞: {my_queue.peek()}") # 두 번째 손님
        
        my_queue.dequeue() # 두 번째 손님
        my_queue.dequeue() # 세 번째 손님
        my_queue.dequeue() # 큐가 비어있어 DEQUEUE 할 수 없습니다.
        
        print(f"큐가 비어있나요? {my_queue.is_empty()}") # True
        print("=== 큐 테스트 완료 ===")
        
    # --- 3. 이진 탐색 (Binary Search) 구현 ---
    def binary_search(sorted_list, target):
        low = 0                 # 탐색 시작 지점 (인덱스)
        high = len(sorted_list) - 1 # 탐색 끝 지점 (인덱스)
        
        print(f"\n--- 이진 탐색 시작: 찾을 값={target}, 대상 리스트={sorted_list} ---")
        
        while low <= high:
            mid = (low + high) // 2 # 중간 인덱스 계산
            guess = sorted_list[mid] # 중간 인덱스의 값
            
            print(f"현재 범위: low={low}, high={high}, mid={mid}, guess={guess}")
            
            if guess == target:
                print(f"{target}을(를) 인덱스 {mid}에서 찾았습니다!")
                return mid # 값을 찾으면 해당 인덱스 반환
            elif guess < target:
                print(f"{guess}은(는) {target}보다 작습니다. 검색 범위를 오른쪽으로 줄입니다.")
                low = mid + 1 # 중간 값보다 작으니, 중간의 오른쪽 부분을 탐색
            else: # guess > target
                print(f"{guess}은(는) {target}보다 큽니다. 검색 범위를 왼쪽으로 줄입니다.")
                high = mid - 1 # 중간 값보다 작으니, 중간의 왼쪽 부분을 탐색
                
        print(f"{target}을(를) 리스트에서 찾을 수 없습니다.")
        return -1 
    
    # --- 이진 탐색 동작 테스트 ---
    if __name__ == "__main__":
    
        sorted_numbers = [1, 5, 7, 8, 12, 13, 19, 23, 29, 30]
    
    # 존재하는 값 찾기
    result1 = binary_search(sorted_numbers, 13)
    # 다른 값으로도 테스트 해보세요:
    # result1 = binary_search(sorted_numbers, 1)
    # result1 = binary_search(sorted_numbers, 30)

    # 존재하지 않는 값 찾기
    result2 = binary_search(sorted_numbers, 4)
    # 다른 값으로도 테스트 해보세요:
    # result2 = binary_search(sorted_numbers, 2)
    # result2 = binary_search(sorted_numbers, 25)
    # result2 = binary_search(sorted_numbers, 0)
    # result2 = binary_search(sorted_numbers, 31)

    # 최종 결과 출력 (위의 함수 호출 후에 아래 줄들을 주석 해제하여 사용할 수 있습니다.)
    # print(f"찾은 인덱스 (13): {result1}")
    # print(f"찾은 인덱스 (4): {result2}")