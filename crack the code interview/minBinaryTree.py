class Node:
	def __init__(self,value):
		self.right = None
		self.left = None
		self.val = value

	def __str__(self):
		return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'
def initiateArrayToBinary(array):
    return arrayToBinary(array, 0, len(array) - 1)


def arrayToBinary(array, start, end):
    if start > end:
        return ''
    mid = (start + end) / 2
    root = Node(array[mid])
    root.left = arrayToBinary(array, start, mid - 1)
    root.right = arrayToBinary(array, mid + 1, end)
    return root



if __name__ == '__main__':
	test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
	print(initiateArrayToBinary(test_array))