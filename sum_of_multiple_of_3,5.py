#1. find the sum of all the multiples of 3 or 5 below 1000  (Project Euler)

#if we list all the natural below 10 that are multiples of 3 or 5,
#we get 3,5,6 and 9. The sum of these multiples of 23.
#Find the sum of all the the multiples of 3 or 5 below 1000.

def divisibleby3or5(n):
    x=[];
    for i in range (int(n)):
        i+=1;
        if i%3==0:
            x+=[i];
            #print(i, 'is divisible by 3');  #to know the multiple of 3
        elif i%5==0:
            x+=[i];
            #print(i,'is divisible by 5');  #to know the multiple of 5.
    #print(x);
    return x
print('Enter the number below which you want to know the sum of multiples of 3 or 5');
x=float(input());
y=divisibleby3or5(x);
#print('the y is',y);
ans=0;
for i in range (len(y)):
    ans=ans + y[i];
print('the sum is: ', ans);
