#combination of print and return

def even_or_odd(i):     #defining the function here
    #input: i a positive int, return true if i is even , otherwise false
    #print("with return")
    remainder=i%2
    if remainder==0:
        x="even"
    else:
        x="odd"
    return x

#even_or_odd(4)
#print(even_or_odd(4))
#print(even_or_odd(5))

def even_or_odd_withoutreturn(i):       #defining the function without return
    print("without return")
    remainder=i%2

#print(even_or_odd_withoutreturn(3))
def print_1to10_evenorodd():
    print("all number between 1 and 10: even or odd:")
    for i in range(10):
        i+=1
        print(i," is ",even_or_odd(i))  # here the function is called which we made above
    #return 0
print_1to10_evenorodd()

