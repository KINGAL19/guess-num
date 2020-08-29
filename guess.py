import random

r = random.randint(1, 100)
while True:
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('終於答對了')
		break
	elif num > r:
		print('比答案字大')
	elif num < r:
		print('比答案小')
