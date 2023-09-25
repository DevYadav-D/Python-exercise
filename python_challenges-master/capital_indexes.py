def capital_indexes(s):
    result=[];a=0;
    for element in s:
        if element.isupper():
            result.append(a)
            a+=1
        else:
            a+=1
    return result
#print(capital_indexes('HellLLo'))
#output=[0, 4, 5]
