driving = input("你有沒有開過車(1:有 , 2: 沒有):")
age = input("請問你現在幾歲:")
driving = int(driving)
age = int(age)

if driving == 1:
	if age >= 18 :
		print("恭喜妳通過測驗")
	else:
		print("你這個罪犯")
else:
	print("太可惜了")