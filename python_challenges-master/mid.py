#This function for mid value of the string 
def mid(s):                             
    if len(s)%2 == 0:
        result=''
    else:
        result=s[len(s)//2]               # '//' = integer division only return int
    return result

