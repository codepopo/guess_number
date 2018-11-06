#猜數字遊戲



import random
print ("請輸入兩個數字,來猜猜範圍內的隨機數值")  #讓使用者自己決定猜的範圍
a = input("請輸入第一個數字: ")
b = input('請輸入第二個數字: ')
a = int(a)
b = int(b)
r = random.randint(a,b)
time = 0
print('你選定的範圍是',a, '到', b)
while True :
	x = input('請輸入一個數字:', )
	x = int(x)	
	time += 1       #與time = time +1 是相同意思
	if r == x :
		print('正確答案是',r,'你答對了呢!')
		print('你總共猜了',time,'次')
		break
	elif x < r :
		print('數字太小')
	else :
		print('數字太大')

