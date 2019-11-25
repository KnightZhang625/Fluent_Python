# coding:utf-8

# 使用functools.lru_cache优化, 储存中途会用到的结果
import functools
@functools.lru_cache(maxsize=32, typed=True)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(100))

# 叠放装饰器
def d1(func):
    def d1_inner():
        print('This is d1')
        func()
    return d1_inner

def d2(func):
    def d2_innner():
        print('this is d2')
        func()
    return d2_innner

@d1
@d2
def f():
    print('this is f')

f()

# 带参数装饰器
def log(activate):
    def decorator(func):
        def decorator_inner(info):
            if activate:
                print('haha')
                func(info)
            else:
                func(info)
        return decorator_inner
    return decorator

# 这个带参数的装饰器, python会自动识别, 并返回真正的decorator
@log(activate=True)
def test(info):
    print(info)

test('This is test')