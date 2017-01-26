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






if __name__ =='__main__':
    import re
    # print(isUnique("sanb"))
    # print(urlify("dfs dgds dsgsd bjhhj"))
    # print(palindrome_permutation("carerac"))
    print(one_way('pale', 'ple'))
