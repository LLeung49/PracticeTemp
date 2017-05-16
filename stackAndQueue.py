# stack and queues form interview book
names = ['Alice', 'Betty', 'Fred', 'Tom']
for index, name in enumerate(names):
    print ('index:',index,'=>', name)


alist = ['a','s','d','f']
try:
    alist.index('name')
    print ('Find it.')
except ValueError as e:
    print ('Not Found.',e)

import random
alist = [1, 2, 3, 4]
random.shuffle(alist)  
print (alist)

# 交集 去重等
list1 = [1, 3, 4, 6]
list2 = [1, 2, 3, 4]
l3 = [1,1,2,3,4,3,3,4,4,6,8,9,5,4,5,7,2,4]
print([i for i in list1 if i not in list2])
print([i for i in list1 if i in list2])
print([i for i in l3 if i in set(l3)])

# 找到元素的所有位置
l = ['a','b','c','c','d','c']
find = 'c'
print([i for i,v in enumerate(l) if v==find])
