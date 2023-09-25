#this function takes a list of list and flatten it
#into one-dimentional list

def flatten(x):
    result=[]
    for i in x:
        if type(i) is list:
            for i in i:
                result.append(i)
        else:
            result.append(i)
    return result
