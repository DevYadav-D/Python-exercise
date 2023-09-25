#two string are anagram if you can make one form the other
#by rearranging the letters

def is_anagram(x,y):
    result=True
    if len(x)==len(y):
        x=sorted(x);y=sorted(y);i=len(x)
        while i>0:
            i=i-1;
            if x[i]==y[i]:
                pass
            else:
                result=False
                break
    else:
        result=False
    return result
