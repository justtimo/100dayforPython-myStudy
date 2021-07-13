'''
循环结构就是程序中控制某条或某些指令重复执行的结构。在Python中构造循环结构有两种做法，一种是for-in循环，一种是while循环。
'''
import random

'''
如果明确的知道循环执行的次数或者要对一个容器进行迭代（后面会讲到），那么我们推荐使用for-in循环，
例如下面代码中计算1~100求和的结果（$\displaystyle \sum \limits_{n=1}^{100}n$）。
'''
sum=0
for x in range(101):
	sum+=x
print(sum)
'''
需要说明的是上面代码中的range(1, 101)可以用来构造一个从1到100的范围，当我们把这样一个范围放到for-in循环中，就可以通过前面的循环变量x依次取出从1到100的整数。当然，range的用法非常灵活，下面给出了一个例子：

range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。
'''

'''
实现1~100之间的偶数求和。
'''
sum=0
for x in range(0,101,2):
	sum+=x
print(sum)

'''
也可以通过在循环中使用分支结构的方式来实现相同的功能，代码如下所示。
'''
sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)


'''
while循环

构造不知道具体循环次数的循环结构，我们推荐使用while循环
while循环通过一个能够产生或转换出bool值的表达式来控制循环，表达式的值为True则继续循环；表达式的值为False则结束循环。

猜数字游戏的规则是：计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
'''
answer = random.randint(1, 100)
print(answer)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')

'''
上面的代码中使用了break关键字来提前终止循环，需要注意的是break只能终止它所在的那个循环，这一点在使用嵌套的循环结构（下面会讲到）需要引起注意。
除了break之外，还有另一个关键字是continue，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。
'''
'''
循环结构也是可以嵌套的，也就是说在循环中还可以构造循环结构。下面的例子演示了如何通过嵌套的循环来输出一个九九乘法表。
'''
for i in range(1,10):
	for j in range(1,10):
		print('%d*%d=%d'%(i,j,i*j))
	print()
'''
输入一个正整数判断是不是素数。
指的是只能被1和自身整除的大于1的整数。
'''
a=int(input('请输入数字：'))
is_permission=True
while is_permission:
	if (a>1 and a%1==0 and a%a==0) :
		print('是素数')
		is_permission=False
	else:
		print('不是素数')

