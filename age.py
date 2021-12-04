driving = input("你有沒有開過車(1:有 , 2: 沒有):")
age = input("請問你現在幾歲:")
#driving = int(driving)
age = int(age)

if driving == '有':
	if age >= 18 :
		print("恭喜妳通過測驗")
	else:
		print("你這個罪犯")
elif driving == '沒有':
	if age >= 18:
		print("太可惜了")
	else:
		print("再過幾年就能開車了")
else:
	print("請輸入有或沒有")