def add_dots(s):
    a=[]; 
    for i in s:
        i=i+".";
        a.append(i)
    result=''.join(a)  #join inbuilt function combine the element of list into string
    a=list(result)     #converting the string into list
    a.pop()            #need to delete the last '.'
    result=''.join(a)  #converting the list into string 
    return result

def remove_dots(s):
    result=s.replace('.','') #using replace function
    return result

#short method
def add_dot(s):
    return ".".join(s)
def remove_dot(s):
    return s.replace('.','')
