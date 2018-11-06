#猜數字遊戲




import random
r = random.randint(1,100)
time = 0
while True :
	x = input('請輸入一個數字 1-100:', )
	x = int(x)	
	time = time + 1
	if r == x :
		print('正確答案是',r,'你答對了呢!')
		print('你總共猜了',time,'次')
		break
	elif x < r :
		print('數字太小')
	else :
		print('數字太大')

