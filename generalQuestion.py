import re
a=5
b=6
# swap 2 variable
a,b = b,a 
print ('swap: ', a, b)
# delete duplicated element in an array
old_list = [1,1,1,3,4] 
new_list = list(set(old_list)) 
print ('uniq a array: ', old_list, new_list)

# reverse string
s = 'abcde' 
ss = s[::-1] 
print ('reverse: ', s, ss)

# make a dict using 2 related array
names = ['lucien', 'joe'] 
ages = [23, 40] 
m = dict(zip(names,ages)) 
print ('make dict', m)
# how to connect many strings,why: using '+' will apply memories every time
fruits = ['apple', 'banana'] 
result = ''.join(fruits) 
print ('concatenate array of strings instead of using plus: ', result)

# iterate reverse
list=[1,2,3,4,5]
list.reverse()
try:
	for x in list:
	    print(x,end=' ')	# add , so it won't start a new line, in python3: print(x, end="")
finally:
    list.reverse()
print ('Restore list', list)

import re
s = '<html><head><title>Title</title>'
search = re.search('<.*>', s)
print('search: ',search.group())
findall = re.findall('<.*?>', s)
print('find all: ',findall)
print('match: ', re.match('<.*>', s).group())

# 异常处理

# while True:
# 	try:
# 		x = int(input("Please enter a number: "))
# 		break
# 	except ValueError:
# 		print("Oops!  That was no valid number.  Try again...")

list=[3,4,6,'r','d',5,6,5]
for i in list:
	try:
		print(int(i))
	except ValueError as e:
		print("Oops!  That was not a valid number.",e)
	else:
		print('done')

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


