def main():
    # input() 函數 讓使用者在終端機輸入資料
    user_input = input("請輸入一個數字: ")

    # 取得使用者輸入的資料
    # 將使用者輸入強制轉型成 int
    try:
        number = int(user_input)
        print(f"您輸入的數字是: {number}")
    except ValueError:
        print("輸入的資料不是有效的整數。")

# 執行主程式
main()
