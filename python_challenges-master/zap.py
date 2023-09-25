#this function two lists and it will return a list of tuples
#and each tuple contians one item from both list

def zap(l1,l2):
    if len(l1)==len(l2):
        result=[];
        for i in range(len(l1)):
            a=[l1[i],l2[i]]
            a=tuple(a)
            result.append(a)
    return result
            
'''
def zap(a,b):
    return [(a[i],b[i]) for i in range(len(a))]
'''
