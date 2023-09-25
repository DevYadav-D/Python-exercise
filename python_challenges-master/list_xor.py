#This function should take 3 parameters: n, list1, list2
#if n is in both list or in none of the lists, return False
#if n is in only one of the lists, return True

def list_xor(n, list1, list2):
    result = True
    for i in list1:
        for i in list2:
            if i == n:
                result = False
                break
    else:
        list1.extend(list2)
        if n in list1:
            result = True
        else:
            result = False
    return result
'''
def list_xor(n, list1, list2):
    return (n in list1) ^ (n in list2)


def list_xor(n, list1, list2):
    if n not in list1 and n not in list2:
        return False
    if n in list1 and n in list2:
        return False
    return True
'''

#test
n=1
list1=[1,2,3]
list2=[2,3,4]
print(list_xor(n, list1,list2))

a = list1 and list2
print('a=',a)
