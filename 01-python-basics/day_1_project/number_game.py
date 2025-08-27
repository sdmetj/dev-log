# number_game.py
import random

def main():
    print("===숫자 맞추기 게임===")
    print("1부터 100 사이의 숫자를 맞춰보세요!")
    
    number = random.randint(1, 100) # 정답 숫자
    attempts = 0 # 시도 횟수
    
    while True:
        try:
            guess = int(input("숫자를 입력하세요: "))
            attempts += 1
            
            if guess < number:
                print("더 큰 숫자입니다.")
            elif guess > number:
                print("더 작은 숫자입니다.")
            else:
                print(f"정답입니다! 시도 횟수: {attempts}")
                break
        except ValueError:
            print("숫자를 입력해주세요!")
if __name__=="__main__":
    main()
