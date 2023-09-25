#This funciton takes a non-negative number as its only parameter
#Function should convert the number to a string and add commas as
#a thousand parameter Ex: fn(1000000) should return "1,000,000"

def format_number(n):
    if isinstance(n,int)or isinstance(n,float):
        if n<0:
            print("please enter a positive number")
        else:
            n = list(str(int(n)))
            n.reverse()
            n = n
            b=0
            for i in range(len(n)+1):
                b=b+1;
                if b==4:
                    n.insert(i,',')
                    b = 0
                else:
                    None
            n.reverse()
            a=''
            n=a.join(n)
            return print(n)
    else:
        print("please enter a valid input or number")
    return None

'''
#built-in solution
def format_number(n):
    return "{:,}".format(n)
'''
