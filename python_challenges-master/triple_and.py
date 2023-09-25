#It takes three parameters and returns True only if all True, otherwise False

def triple_and(a,b,c):
    result=False;
    if a==b:
        if b==c:
            if a==True:
                result=True
    return result
'''
def triple_and(a,b,c):
    return a and b and c'''
