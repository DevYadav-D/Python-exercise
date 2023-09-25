#This function to translate from strings of length 2
#to a tuple (row, column)

def get_row_col(s):
    s=list(s)
    result=[]
    result.append(ord(s[1])-49)
    result.append(ord(s[0])-65)
    result=tuple(result)
    return result
