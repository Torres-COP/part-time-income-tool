people=int(input("作業した人数は？"))
hour=int(input("一人当たりの勤務時間は?"))
wage=1200
print(f"全員分の合計勤務時間は{people*hour}時間です")
print(f"支給総額は{people*hour*wage}円です")