i = 0
j = 3
password = '123456' 
while i < 3:
	pwd = input('請輸入您的密碼:')
	if pwd == password:
		print('登入成功!')
		break
	else:
		# print(f'密碼錯誤,還有{j}次機會') # 進階作法
		j = j - 1
		print('密碼錯誤還有',j , '次機會')
		i = i + 1
		

