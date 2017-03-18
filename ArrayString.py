def isUnique(string):
    # print(len(string))
    if len(string) > 128:
        return False
    char_set = {}
    for i in range(0, len(string)):
        if string[i] in char_set:
            return False
        char_set[string[i]] = 1

    # for (k,v) in char_set.items():
    #     print(k,v)

    return True


def urlify(str):
    space = re.compile(r" ")
    return space.sub(r"%20",str)


def palindrome_permutation(str):
    a = set()
    for character in str:
        if character in a:
            a.remove(character)
        else:
            a.add(character)
    if len(a) < 2:
        return True
    else:
        return False


def one_way(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    if len(str2) < len(str1):
        temp = str1
        str1 = str2
        str2 = temp
    index1 = 0
    index2 = 0
    foundDiff = False
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] != str2[index2]:
            if foundDiff:
                return False
            foundDiff = True
            if len(str1) == len(str2):  # replace
                index1 += 1
                index2 += 1
            else:  # insert or delete
                index2 += 1

        else:
            index1 += 1
            index2 += 1
    return True


def rotate_matrix(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    for layer in range(0, int(n/2)):  # layer by layer, the central stays
        first = layer  # the first element of current layer
        last = n - 1 - layer  # the last element of current layer
        for i in range(first,last):
            offset = i - first
            top = matrix[first][i]  #save top
            matrix[first][i] = matrix[last - offset][first]  # left --> top
            matrix[last - offset][first] = matrix[last][last-offset]  # bottom -->left
            matrix[last][last - offset] = matrix[i][last]  # right --> bottom
            matrix[i][last] = top
    return matrix









if __name__ =='__main__':
    import re
    # print(isUnique("sanb"))
    # print(urlify("dfs dgds dsgsd bjhhj"))
    # print(palindrome_permutation("carerac"))
    # print(one_way('pale', 'ple'))
    a = [[1, 2, 3, 'a'],
         [4, 5, 6, 'b'],
         [7, 8, 9, 'c'],
         ['a', 'b', 'c', 'd']]
    print(rotate_matrix(a))