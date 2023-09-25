'''#ship sinking using the functions/subroutines/methods and main program#
     #Assignment: 4  by DEV YADAV'''

def listoutput(mylist):
    totalelement=0
    for i in range(len(mylist)):
        print(mylist[i])
        totalelement+=len(mylist[i])
    return totalelement

def play(mylist,sinkboat,valuecount):
    hits=0
    fails=0
    while hits<valuecount:
        row=int(input("enter the row number 0 to 4:      "))
        col=int(input("enter the coloumn number 0 to 4:  "))
        if mylist[row][col]==1:
            mylist[row][col]=0
            print("YOU HAVE A HIT")
            hits+=1
            listoutput(mylist)                  #calling listoutput function
            if mylist==sinkboat:
                print("**end of the game**")
                break
        else:
            print("FAIL")
            listoutput(mylist)                  #calling listoutput function
            fails+=1
    return(hits,fails)

def main():
    mylist=[[1,0,1,0,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,0,1,1],[0,1,0,0,0]]
    sinkboat=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    valuecount=listoutput(mylist)               #calling listouput function
    print("\nTo play the sinking of ship you have to covert 1 to 0 of above matrix, \nso enter the row number and the coloumn number to convert into 0\n")
    hits,fails=play(mylist,sinkboat,valuecount) #calling "play" function
    if hits>valuecount:
        print("Sorry, you loose the game")
    else:
        print("congratulations")
    print("number of hits: ",hits)
    print("number of fail: ",fails)    
main()
