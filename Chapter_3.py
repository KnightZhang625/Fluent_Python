# coding:utf-8

# 字典 setdefault(), 这个对于value是list的时候很有用
sample_data = ['a', 'b', 'c', 'a', 'e']
dic = {}
for i, d in enumerate(sample_data):
    dic.setdefault(d, []).append(i)
print(dic)

# 字典 defaultdict
import collections

dic_2 = collections.defaultdict(list)
for i, d in enumerate(sample_data):
    dic_2[d].append(i)
print(dic_2)

# collections.Counter
test = ['a', 'b', 'c', 'a', 'a']
ct = collections.Counter(test)
print(ct)
ct.update(['e', 'f', 'b'])
print(ct)
print(ct.most_common(2))

# 指定key为专门类型
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def __contains__(self, key):
        return str(key) in self.data
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item

str_key_dict = StrKeyDict()
str_key_dict[1] = 'a'
str_key_dict['2'] = 'b'
print(str_key_dict)
print(2 in str_key_dict)

# 不可变映射类型
from types import MappingProxyType

original_dict = {'a': 1}
proxy_dict = MappingProxyType(original_dict)

# # proxy_dict只能查看, 不能修改
try:
    proxy_dict['b'] = 2
except Exception as e:
    print(e)

original_dict['b'] = 2
print(proxy_dict)