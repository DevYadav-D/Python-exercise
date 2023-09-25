#This function takes a list and check whether all elements are the same

def all_equal(l):
    result=False; i=0;
    if len(l)<=1 :
        result=True
    else:
        while len(l)-1>i:
            if l[i]==l[i+1]:
                result=True
                i=i+1
            else:
                result=False
                break
    return result
