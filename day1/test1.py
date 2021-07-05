"""
使用变量保存数据并进行加减乘除运算


"""
a = 233
b =15.12311

print(a+b)
print(a-b)
print(a*b)
print(a/b)

'''
type函数对变量的类型进行检查
'''
print(type(a))
print(type(b))

"""
使用Python中内置的函数对变量类型进行转换。

int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将字符串（一个字符）转换成对应的编码（整数）。
"""
print("-------------")
print(int(b))
print(type(str(b)))
print(chr(a))
print(ord(a))