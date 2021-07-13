from math import sqrt

a=int(input('请输入数字：'))
is_permission=True
end=int(sqrt(a))
for x in range(2,end):
	if a%x==0:
		is_permission=False
		break
if is_permission and a!=1:
	print("是素数")
else:
	print('不是素数')