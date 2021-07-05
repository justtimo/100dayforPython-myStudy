"""
通过键盘输入两个整数来实现对两个整数的算术运算
"""
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

'''
上面的print函数中输出的字符串使用了占位符语法，
其中%d是整数的占位符，
%f是小数的占位符，
%%表示百分号（因为百分号代表了占位符，所以带占位符的字符串中要表示百分号必须写成%%），
字符串之后的%后面跟的变量值会替换掉占位符然后输出到终端中
'''
# a=int(input("a = "))
# b=int(input("b= "))
#
# print('%d +%d = %d' % (a,b,a+b))