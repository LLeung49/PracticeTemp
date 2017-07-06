

def checkParentheses(input_str):
	parenthsisStr = ''
	stack =[]
	level = 0
	for item in input_str:
		if item == '(':
			level += 1
			parenthsisStr += str(level)
			stack.append(level)
		if item == ')':
			if len(stack) <= 0:
				return 'unbalanced'
			parenthsisStr += str(stack.pop())
	if len(stack) > 0:
		return 'unbalanced'

			

	return parenthsisStr


input_lst = ['(a+b)*(c+d)',
			'(((a+b)*c)/(d-e))',
			'((a+b)',
			'(a+b))',
			'(a+b)*((a+b)+c*(c+b))',
			'(a+b)*((a+b)+c*c+b))',
			'(a+b)*((a+b)+c*(c+b)'
			]

output_lst = ['1122',
			'12332441',
			'unbalanced',
			'unbalanced',
			'11233442',
			'unbalanced',
			'unbalanced']

for i in range(len(input_lst)):
	if checkParentheses(input_lst[i]) != output_lst[i]:
		print('---->Expect: ', output_lst[i], '  Returned: ', checkParentheses(input_lst[i])) 
	else:
		print('Case ' + str(i) + ' looks good') 
