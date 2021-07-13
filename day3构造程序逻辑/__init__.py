'''
寻找水仙花数。
说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
'''
print(223//10%10)

for x in range(100,1000):
	one=x%10
	two=x//10%10
	three=x//100
	if one**3+two**3+three**3==x :
		print(x)
'''
用类似的方法，我们还可以实现将一个正整数反转，例如：将12345变成54321，代码如下所示。
'''
num=int(input('请输入一个数字'))
reverse_num=0
while num>0:
	reverse_num=reverse_num*10+num%10
	num=num//10
print(reverse_num)

'''
百钱百鸡问题。
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
穷举（也称为暴力搜索法）：思路：100元最多买20只攻击，33只母鸡，300只小鸡
'''
for x in range(0,20):
	for y in range(0,33):
		z=100-x-y
		if 5*x + 3*y + z/3 == 100:
			print('公鸡%d，母鸡%d,小鸡%d'%(x,y,z))
'''
CRAPS赌博游戏。

说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。

我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
'''
from random import randint

money=1000
while money>0:
	print('你当前资金为%d'%money)
	can_goon=False
	while True:
		deep=int(input('请下注'))
		if 0< deep <=money:
			break
		else:
			print('堵住不能小于0 或大于当前资金')
	first=randint(1,6)+randint(1,6)
	print('玩家摇出了%d' % first)
	if first==7 or first==11:
		print('玩家胜')
		money+=deep
	elif first==2 or first==3 or first==12:
		print('庄家胜')
		money-=deep
	else:
		can_goon=True
	while can_goon:
		can_goon=False
		print('其他玩家继续摇骰子')
		current=randint(1,6)+randint(1,6)
		print('玩家摇出了%d'%current)
		if current==7 :
			print('庄家胜')
			money-=deep
		elif current==first:
			print('玩家胜')
			money+=deep
		else:
			can_goon=True
print('你破产了')

'''
练习
'''
'''
生成斐波那契数列的前20个数。

说明：斐波那契数列（Fibonacci sequence），又称黄金分割数列，是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）在《计算之书》中提出一个在理想假设条件下兔子成长率的问题而引入的数列，
所以这个数列也被戏称为"兔子数列"。
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，
每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
'''
owe=1
two=1
index=2
while True:
	new_num=owe+two
	print(new_num)
	owe=two
	two=new_num
	index+=1
	if index==20:
		break
'''
找出10000以内的完美数。

说明：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。
'''
for x in range(1,10000):
	for y in range(1,x):
		if x%y==0:
			if y==1:
				index=y
			else:
				index=1+y+x/y
				if x==index:
					print(x)

