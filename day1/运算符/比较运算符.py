'''
比较运算符有的地方也称为关系运算符，包括==、!=、<、>、<=、>=

'''
flag0 = 1==1
flag1 = 1>=2
flag2 = 1!=1
flag3 = 2 < 3
flag4= 2>3
flag5= 1>=2
print(flag0,flag1,flag2,flag3,flag4,flag5)
'''
比较运算符的优先级高于赋值运算符，所以flag0 = 1 == 1先做1 == 1产生布尔值True，再将这个值赋值给变量flag0。
print函数可以输出多个值，多个值之间可以用,进行分隔，输出的内容之间默认以空格分开。
'''

f=int(input('请输入华氏温度： '))
c= (f-32)/1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
'''
在使用print函数输出时，也可以对字符串内容进行格式化处理，上面print函数中的字符串%1.f是一个占位符，稍后会由一个float类型的变量值替换掉它。
同理，如果字符串中有%d，后面可以用一个int类型的变量值替换掉它，而%s会被字符串的值替换掉。

除了这种格式化字符串的方式外，还可以用下面的方式来格式化字符串，其中{f:.1f}和{c:.1f}可以先看成是{f}和{c}，
表示输出时会用变量f和变量c的值替换掉这两个占位符，后面的:.1f表示这是一个浮点数，小数点后保留1位有效数字。
'''
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

r=int(input('请输入圆的半径： '))
zhouchang=2*r*3.1416
mianji=r**2*3.1416
print('周长是: %.4f  ； 面积是: %.4f'%(zhouchang,mianji))
print(f'周长是：{zhouchang:.4f} ； 面积是：{mianji:.4f}')


year=int(input('输入年份：'))
flag_ruinian=year%4==0 and year%100!=0 or year%400==0
print(flag_ruinian)