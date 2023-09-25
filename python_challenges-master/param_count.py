#This function takes a variable number of parameters.
#function should return the number of arguments it was called with

def param_count(*args):
    result=[]
    for i in args:
        result.append(i)
    return len(result)
'''
def param_count(*args):
    return len(args)
'''
