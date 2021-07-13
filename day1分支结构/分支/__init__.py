'''
if elase鱼语句
'''
user_name = input('请输入用户名')
pass_word = input('请输入密码')
if user_name == 'admin' and pass_word == '123':
	print('验证成功')
else:
	print('验证失败')

'''
Python中没有用花括号来构造代码块而是使用了缩进的方式来表示代码的层次结构
连续的代码如果又保持了相同的缩进那么它们属于同一个代码块，相当于是一个执行的整体
'''

'''
如果要构造出更多的分支，可以使用if...elif...else...结构或者嵌套的if...else...结构

分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
'''
x = int(input('请输入x的值'))
if x > 1:
	y = 3 * x - 5
elif -1 <= x <= 1:
	y = x + 2
else:
	y = 5 * x + 3
print('f(%.3f)=%.3f' % (x, y))

'''
分支结构是可以嵌套的，例如判断是否通关以后还要根据你获得的宝物或者道具的数量对你的表现给出等级（比如点亮两颗或三颗星星），那么我们就需要在if的内部构造出一个新的分支结构，
同理elif和else中也可以再构造新的分支，我们称之为嵌套的分支结构，也就是说上面的代码也可以写成下面的样子
'''
x1 = int(input('请输入x的值'))
if x1>1:
	y1=3*x-5
else:
	if -1 <= x1 <= 1:
		y1 = x1 + 2
	else:
		y1 = 5 * x1 + 3
print('f(%.3f)=%.3f' % (x1, y1))

'''
英制单位英寸与公制单位厘米互换。
'''
value=int(input('请输入长度：'))
danwei=input('请输入单位：')
if danwei =='in' or danwei=='英寸':
	limi=value*2.54
	print("%.3f 英寸 等于 %.3f里面"%(value,limi))
elif danwei=='cm'or danwei=='厘米':
	yingcun=value/2.54
	print("%.3f 厘米 等于 %.3f英寸"%(value,yingcun))
else:
	print('请输入正确的单位')

'''
输入三条边长，如果能构成三角形就计算周长和面积。
'''
side1=int(input('第一条边长度：'))
side2=int(input('第二条边长度：'))
side3=int(input('第三条边长度：'))
if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
	zhoucahng=side3+side2+side1
	print('周长是:%d'%zhoucahng)
	#海伦公式求园面积
	p = (side1 + side2 + side3) / 2
	area = (p * (p - side1) * (p - side2) * (p - side3)) ** 0.5
	print('面积: %.4f' % (area))
else:
	print('不能构成三角形')


