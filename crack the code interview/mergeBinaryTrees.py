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

def inOrderTraversal(node):
	lst=[]
	if node != '':
		lst += inOrderTraversal(node.left)
		lst.append(node.val)
		lst += inOrderTraversal(node.right)
	return lst

def mergeTwoArray(a,b):
	i = j = 0
	outputArray = []
	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			outputArray.append(a[i])
			i += 1
		else:
			outputArray.append(b[j])
			j +=1
	
	if i < len(a):
		outputArray += a[i:]
	if j < len(b):
		outputArray += b[j:]	
	return outputArray

if __name__ == '__main__':
	array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
	print 'TREE1----> ',initiateArrayToBinary(array1)
	array2 = sorted([11,13,16,32,54,3425,35,45,532,345])
	print 'TREE2----> ',initiateArrayToBinary(array2)

	tree1 = initiateArrayToBinary(array1)
	tree2 = initiateArrayToBinary(array2)
	# restore sorted array by in-order traversal
	lst1 = inOrderTraversal(tree1)
	print lst1
	lst2 =  inOrderTraversal(tree2)
	print lst2
	# merge sorted arrays
	lst = mergeTwoArray(lst1,lst2)
	print lst
	# build new binary tree
	tree_merged = initiateArrayToBinary(lst)
	print 'MERGED TREE---> ',tree_merged


