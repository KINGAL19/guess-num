import random

print('模式1:手動: , 模式2:隨機: ')
mode = input('請輸入模式: ')
mode = int(mode)
if mode == 1:
	r = input('請輸入數字: ')
	r = int(r)
	ra = input('請輸入範圍: ')
	ra = int(ra)
	max = r + ra
	min = r - ra
elif mode == 2:	
	start = input('請決定隨機數字範圍開始值: ')
	end = input('請決定隨機數字範圍結束值')
	start = int(start)
	end = int(end)
	r = random.randint(start, end)
else:
	print('不要亂輸入!!')

count = 0
while True:
	count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你答對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')
