#It takes a string as a paramenter to check if it is palindrome or not
#A string is palindrome when it is the same when read backwards

def palindrome(s):
    x=list(s)
    y=list(s)
    y.reverse()
    result=True;
    i=len(s)
    while i>0:
        if x[len(s)-i]==y[len(s)-i]:
            result=True
        else:
            result=False
            break
        i=i-1;
    return result

'''def palindrome(s):
        return s == s[::-1]'''
