# 終極密碼 讓使用者猜數字

# 1.告訴使用者需要輸入的數字範圍


# 使用者猜對要回傳「恭喜中獎」


# 2.數字太大 要提示「請輸入更小的數字」


# 3.數字太小 要提示「請輸入更大的數字」


# 4.超出範圍要顯示「輸入錯誤，請重新輸入」

import random

def guess_the_number():
    # 設定數字範圍
    min_number = 1
    max_number = 100
    secret_number = random.randint(min_number, max_number)
    
    print(f"請猜一個數字，範圍是 {min_number} 到 {max_number}。")
    
    while True:
        try:
            # 取得使用者輸入
            user_guess = int(input("請輸入你的猜測: "))
            
            # 檢查輸入是否在範圍內
            if user_guess < min_number or user_guess > max_number:
                print("輸入錯誤，請重新輸入。")
            elif user_guess < secret_number:
                print("請輸入更大的數字。")
            elif user_guess > secret_number:
                print("請輸入更小的數字。")
            else:
                print("恭喜中獎！")
                break  # 使用者猜對了，退出循環
                
        except ValueError:
            print("無效輸入，請輸入一個數字。")

# 執行主程式
if __name__ == "__main__":
    guess_the_number()
