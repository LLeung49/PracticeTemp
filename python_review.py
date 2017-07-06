
# -*- coding: utf-8 -*-
import re
str = "0121345601213456"
str_list = list(str)
print(str_list)

print("".join(str_list))

pattern = re.compile("3")
print(pattern.findall(str))
print(str.find("3"))
print(str.rfind('6'),str[12])
# print(str.index("a"))

if str.find('a') == -1:
     print('oookkk')
else:
     print('bad')


#字典

di = {"apple":"store"}
keys = ['a','b','c']
dict = dict.fromkeys(keys)              # 用数组赋值keys
print(dict)
dict = dict.fromkeys(keys,"100")        # 用数组赋值keys 以及 默认 values
print(dict)

d = dict.copy()                         # 复制字典
print(d)
print(d.items())                        # 返回tuple pairs
print(d.keys())                         # 返回key列表
print(d.values())
d.update(di)                            # 合并字典
print(d)

print(d.get("h",199))
print(d.get("h"))

# 字典排序
print("==============Sort dict==============")
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
    'ZTX': 20.75
}


min_price = min(zip(prices.values(), prices.keys()))
print('min_price with zip---->',min_price)
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
print('max_price with zip---->',max_price)
# max_price is (612.78, 'AAPL')

prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]
print('sorted dict on values with zip---->',prices_sorted)
print('min_price company using lambda---->',min(prices, key=lambda k: prices[k]))     # Returns 'FB'
print('max_price company using lambda---->',max(prices, key=lambda k: prices[k]))     # Returns 'AAPL'

print('Sort dict----->\n',sorted(prices.items(), key=lambda k: k[1]))

print('Traverse a sorted dict using a loop: \n')
for item in sorted(prices.items(), key=lambda k: k[1]):
    print('Sorted item',item)
for key in prices:
    print('--',key,prices[key])

print(prices.pop('FB'),prices)                  # 弹出指定键值对应的值
print(prices.pop('GOOGLE','NO SUCH KEY'),prices)        #没有键值输出后面的default 否则keyError
print(prices.popitem(),prices)                  #   弹出并删除随机的键值对


# Python filter+map+reduce
print("==============filter+map+reduce==============")

# filter
def odd_num(x):             # 给定的布尔函数
    return x % 2 !=0
odd_list = list(filter(odd_num, range(2, 25)))      # 一定要加list!!
print('odd num by filter',odd_list)
print('odd num by filter+lambda',list(filter(lambda x:x % 2 !=0, range(2, 25))))
print('test filter function:',odd_num(2))

lst = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]

lst = list(filter(lambda x: x != 0, lst))
print('filter zero by filter+lambda',lst)

# map
def multiply(x,y):
    return x*y

def square(x):
    return x*x

def multiply2(x,y,z):
    return x*y*z

print('unequal num of 2 input variables of map---->',list(map(multiply,range(2),range(2,7))))      # 项数不一定相等
print('one input variable map---->',list(map(square,range(5))))
print('unequal num of 2 input variables of map---->',list(map(multiply2,range(2),range(2,7),range(10,19))))
# reduce
from functools import reduce
def add(x,y):
    return x+y

print(reduce(add,range(11)))
# 可以设置初始值
starting_value = 'hello'
starting_value2 = 'HI'
following_values = [',',' i',' am',' Lucien.']

print(reduce(add,following_values,starting_value))
print(reduce(add,following_values,starting_value2))


print("==============enumerate==============")
# enumerate dict only return key
lst = [1,2,43,5,0,673,7547,24,5]
for item in enumerate(prices):
    print(item)
for i,v in enumerate(lst):
    print('-->',i,v)

