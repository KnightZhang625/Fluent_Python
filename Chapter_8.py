# coding:utf-8

# 变量的引用, '='比较的是值相同, 'is'比较的是id相同
str_1 = 'a'
str_2 = 'a'
print(str_1 == str_2)
print(str_1 is str_2)

str_3 = '大叔大婶大所多埃文斯无'
str_4 = '大叔大婶大所多埃文斯无'
print(str_3 == str_4)
print(str_3 is str_4)

# 函数可能会修改接收到的可变对象
def f(a, b):
    a += b
    return a

n_1 = 3
n_2 = 5
print(f(n_1, n_2))
print(n_1)
print(n_2)
aa = [1, 2, 3]
bb = [4, 5]
print(f(aa, bb))
print(aa)           # aa的值会被改变
print(bb)

# 不要使用可变类型作为参数的默认值
class Bus(object):
    def __init__(self, passengers=[]):
        self.passengers = passengers
    
    def add(self, people):
        self.passengers.append(people)

    def remove(self, people):
        self.passengers.remove(people)

b1 = Bus()
b1.add(1)
b2 = Bus()
print(b1.passengers)
print(b2.passengers)    # b2中出现b1的1

basketball_team = ['a', 'b', 'c', 'd', 'e']
bus = Bus(basketball_team)
bus.remove('b')
print(bus.passengers)
print(basketball_team)  # 下车以后竟然从basketball_team中除名了

# 正确做法
class Bus_new(Bus):
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

b1 = Bus_new()
b1.add(1)
b2 = Bus_new()
print(b1.passengers)
print(b2.passengers)

basketball_team = ['a', 'b', 'c', 'd', 'e']
bus = Bus_new(basketball_team)
bus.remove('b')
print(bus.passengers)
print(basketball_team)

# 可散列的对象
class Vector2d(object):
    __slots__ = ('__x', '__y')  # can not be inherited
    
    def __init__(self, x, y):
        self.__x = float(x)     # object has no access to double underscore variable
        self.__y = float(y)
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __iter__(self):
        for i in (self.x, self.y):
            yield i
        # return (i for i in (self.x, self.y))
    
    def __str__(self):
        return str(tuple(self))
    
    def __hash__(self):
        return hash(self.x) * hash(self.y)
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)

v1 = Vector2d(3, 5)
v2 = Vector2d(3, 5)
print(v1.x)
for i in v1:
    print(i)
print(v1 == v2)

# 实现切片
from array import array

class Vector(object):
    def __init__(self, components):
        self._components = array('d', components)
    
    def __len__(self):
        return len(self._components)
    
    def __getitem__(self. index):
        return self._components[index]