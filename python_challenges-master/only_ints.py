def only_ints(x,y):
    if type(x)==int:
        if type(y)==int:
            result=True
        else:
            result=False
    else:
        result=False
    return result
