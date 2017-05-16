#Calculate the product of other elements of each element in a list

def test():
    test =[[1,2,4,6],[1,2,3,4],[2],[1,2,'a'],[1,3,3,54,0],[9,0,8,6,0],[]]
    test_result = [[48, 24, 12, 8],[24,12,8,6],[1],'error',[0,0,0,0,eval("9*54")],[0,0,0,0,0],[]]
    # test =[[1,2,4,6]]
    # test_result = [[48, 24, 12, 8]]
    for i in range(len(test)):
        if product_array2(test[i]) != test_result[i]:
            print("Expect: ",test_result[i],"Saw: ",product_array(test[i]))
        else:
            print("Correct: ", test_result[i])
    
def product_array(list):
    output = []
    for i in range(len(list)):
        # if not isinstance(list[i], int):
        #     # raise Exception("not array of ints")
        #     print("---not array of ints---")
        product = 1
        for j in range(len(list)):
            if not isinstance(list[i], int):
                output = 'error'
                return  output
            if j != i and isinstance(list[j], int):
                product = product * list[j]
        output.append(product)
    return output

def product_array2(list):
    output = []
    product = 1
    for i in range(len(list)):
        if not isinstance(list[i], int):
            return 'error'
        if list[i] != 0:
            product *= list[i]  
            # print(str(list[i])+'*',end='')
    # print('='+str(product))        
    numOfZero = list.count(0)
    if numOfZero == 0:
        for i in range(len(list)):
            output.append(product/list[i])
    elif numOfZero == 1:
        indexOfZero = list.index(0)
        output = [0] * len(list)
        output[indexOfZero] = product
    else:
        output = [0] * len(list)
    return output



test()