class MultiStack:

    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item

    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    def print_all(self):
    	return self.array

    def print_size(self):
    	return self.size


def ThreeInOne():
	# two elements per stack
    newstack = MultiStack(2)
    print '---creat MultiStack with depth = 2---'
    print "---check emptyness---"
    print newstack.IsEmpty(0)
    print newstack.IsEmpty(1)
    print newstack.IsEmpty(2)
    print '---puch 3 to stack 1---'
    newstack.Push(3, 1)
    print '---peek stack 1---'
    print newstack.Peek(1)
    print '---print array---'
    print newstack.print_all()
    print '---puch 2 to stack 1---'
    newstack.Push(2, 1)
    print '---print array---'
    print newstack.print_all()
    print '---peek stack 1---'
    print newstack.Peek(1)
    print '---pop stack 1---'
    print newstack.Pop(1)
    print '---peek stack 1---'
    print newstack.Peek(1)
    print '---puch 3 to stack 2---'
    newstack.Push(6, 2)
    print '---print array---'
    print newstack.print_all()

ThreeInOne()
