#This takes a single number as its parameter. and it returns a
#tuple containing two numbers; first number is lower than input
#second number is higher than input

def up_down(n):
    result=[]
    result.append(n-1)
    result.append(n+1)
    result=tuple(result)
    return result

''' def up_down(x):
            return (x-1, x+1)'''
