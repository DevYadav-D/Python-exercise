'''Assignment 2: Shinking of the ship  by DEV YADAV'''

valuecount=0
hits=0
fail=0
list1=[1,0,0,1,1]
list2=[0,0,0,1,1]
list3=[1,0,0,0,1]
list4=[0,0,1,0,0]
list5=[1,0,0,1,0]
list0=[0,0,0,0,0]
mylist=[list1,list2,list3,list4,list5]
sinkboat=[list0,list0,list0,list0,list0]

for i in range(len(mylist)):

    print(mylist[i])           #in case you want to print
    valuecount+=len(mylist[i])

print("\nTo play the sinking of ship you have to convert 1 to 0 of above matrix, \nso enter the row number and the coloumn number to convert into 0")

while hits<valuecount:
    row=int(input("enter the row number 1 to 5:      "))-1;
    col=int(input("enter the coloumn number 1 to 5:  "))-1;
    if mylist[row][col]==1:
        mylist[row][col]=0
        print("YOU HAVE A HIT\n")        #if you want to see output uncomment the for loop
        
        for i in range(len(mylist)):
            print(mylist[i])
            
    else:
        print("FAIL\n")
        fail+=1
    if mylist==sinkboat:
        print("**end of the game: you win, winner winner nice dinner**")
        break
    else:
        hits+=1
if hits>valuecount:
    print("Sorry, you loose the game")
else:
    print("congratulations")
print("number of hits: ",hits)
print("number of fail: ",fail)
