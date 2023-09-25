#To analyze a bingary string consisting of only zeros and ones
#To find the biggest number of consecutive zeros in the string.

def consecutive_zeros(s):
    j=0;
    result=0;
    for i in s:
        if i=='0':
            j=j+1;
            if j>result:
                result=j
        else:
            j=0;
    return result

'''shorter solution
def consecutive_zeros(s):
    return max([len(s) for s in s.split('1')])'''
