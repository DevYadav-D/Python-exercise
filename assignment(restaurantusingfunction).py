#Restaurantmenu  using the function/methods/subroutines

#Assignment 5 by DEV YADAV

def printmenu(menu):
        for key,value in menu.items():
                print(key,value)



def takeorder(menu):
        key=str(input("what would like to have Sir/Madam: \n Enter no for nothing\n"))
        total=0
        orderlist=[]
        while True:
                if key=="no":
                        break
                elif key in menu:
                        print(key,menu[key])
                        orderlist.extend([key,menu[key]])
                        total+=menu[key]
                        key=str(input("anything else:\n "))
                else:
                        print("this is not in the menu")
                        key=str(input("anything else: "))
        return(orderlist,total)

def main():
        menu={"elgsoup":9.99,"coffee":3.19,"tea":2.0,"wild duck": 18.99,"fried carrots":1.79}
        noc=int(input("Enter the number of customer:\n"))
        for i in range(noc):
                printmenu(menu)                                 #calling printmenu function here
                orderlist,total=takeorder(menu)                 #calling takeorder function
                print("order for customer",i+1," is: ",orderlist)
                print("Total bill for customer",i+1,"is: ",total,"\n")
        print("Thank you for your visit")
                
main()
                
        
