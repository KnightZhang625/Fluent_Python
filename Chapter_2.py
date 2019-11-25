# coding:utf-8

# 1. 对对象切片, s[a:b:c], s在a和b之间以c为间隔取值
s = 'bicyle'
print(s[::3])
print(s[::-1])
print(s[::-2])

# 2. bisect 可对有序序列, 实现有序插入
import bisect

a = [1, 2, 5]
bisect.insort(a, 3)
print(a)

# 3. 数组, 当创建一个只包含数字的列表
from array import array
floats = array('d', [1.2, 2.3])
print(floats)