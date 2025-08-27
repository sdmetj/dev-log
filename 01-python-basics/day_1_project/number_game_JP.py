# number_game.py
import random

def main():
    print("===数字当てゲーム===")
    print("1から100の間の数字を当ててみてください！")
    
    number = random.randint(1, 100) # 正答数字
    attempts = 0 # 試行回数
    
    while True:
        try:
            guess = int(input("数字を入力してください: "))
            attempts += 1
            
            if guess < number:
                print("より大きな数字です。")
            elif guess > number:
                print("より小さい数字です。")
            else:
                print(f"正解です！挑戦回数: {attempts}")
                break
        except ValueError:
            print("数字を入力してください！")
if __name__=="__main__":
    main()
