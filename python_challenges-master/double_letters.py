def double_letters(s):
    i=0; length=len(s);
    while i<length-1:
        i+=1;
        if s[i]==s[i-1]:
            result=True
            break
        else:
            result=False
    return result
