# Restaurant Menu# Assignment 3 by DEV YADAV

orderlist=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
totalcostoforder=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
total=0
menu={}
i=0
j=0

#print()
noc=int(input("Enter the number of customers:"))
if noc>20:
    print("Sorry, no more than 20 customers at a time")
else:
    print("if there is no order please enter:  nothing  ")
    print("\nIn Today's Menu: the special is..")
    menu["elg soup"]=9.99
    menu["wild duck"]=18.99
    menu["oat porrige"]=0.59
    menu["coffee"]=3.19
    menu["fried carrots"]=1.79

    for key,value in menu.items():
        print(key,value)
    print()


    while i<noc:
        '''for key,value in menu.items():
            print(key,value)'''
        total=0
        while True:
            key=str(input("what would you like to have Sir/Madam:"))
            if key=="nothing":
                break
            elif key in menu:
                print(key,menu[key])
                orderlist[i].extend([key,menu[key]])
                total+=menu[key]
                #print(total)               #in case you want to know how much you ordered
            else:
                print("this is not in the menu, anything else or nothing")
        totalcostoforder[i].extend([total])
        print("the order of : ",i+1,orderlist[i])
        i+=1
        print()
    while j<noc:
        print("the order for cutomer ",j+1,orderlist[j])
        print("Total Cost of Order",j+1,totalcostoforder[j])
        j+=1
print("*******end*****")
    
