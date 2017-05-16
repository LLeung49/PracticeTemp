
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

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
# max_price is (612.78, 'AAPL')

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]

print(min(prices, key=lambda k: prices[k]))     # Returns 'FB'
print(max(prices, key=lambda k: prices[k]))     # Returns 'AAPL'
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

# filter
def odd_num(x):             # 给定的布尔函数
    return x % 2 !=0
odd_list = list(filter(odd_num, range(2, 25)))      # 一定要加list!!
print(odd_list)

lst = [1, 1, 0, 2, 0, 0, 8, 3, 0, 2, 5, 0, 2, 6]

lst = list(filter(lambda x: x != 0, lst))
print(lst)

# map
def multiply(x,y):
    return x*y

def square(x):
    return x*x

print(list(map(multiply,range(2),range(2,7))))      # 项数不一定相等
print(list(map(square,range(5))))

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
