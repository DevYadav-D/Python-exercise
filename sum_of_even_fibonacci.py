#2. Even fibonacci numbers  (1 1 2 3 5 ..)(Project Euler)
#other question asking for the "by considering the terms in the fibonacci sequence
#whose values do not exceed four million, find the sum of the even-valued terms
print("Enter the number of terms upto which fibonacci number is required")
def fib(n):
    l=[1,1];
    i=3;
    if n>2:
        for i in range(n-2):
            l+=[l[i+1] + l[i]]
    elif n==2:
        l
    elif n==1:
        l=[1];
    else:
        l=['null']
    return l
n=int(input());
l=fib(n);
print("The fibonacci series is:",l,'\n');
a=len(l);
def eventerms(n):
    l=n;   
    b=[];
    for i in range(len(l)):
        if l[i]%2==0:
            b+=[l[i]];
    return b
b=eventerms(l);
print("The Even fibonacci numbers are: ",b,'\n')
ans=0;
for i in range (len(b)):
    ans=ans + b[i];
print('the sum of even number in fibonacci series till ',n,'terms is: ', ans,'\n');

# second part "fibonacci sequence whose values do not exceed four million"
x=0;n=0;
print('***from here the next part starts***\n');
while True:
    if x>=4000000:
        #print("correct"); it's just to check
        break;
    else:
        y=fib(n);
        #print('length',len(y));
        if len(y)==1:
            x=1;
        else:
            x=int(y[len(y)-1]);
    #print('last term',x);
    n=n+1;
    #print(y);
    #print('goingon');
print('the fibonacci numbers till 4 million is\n',y,'\n');
b=eventerms(y);
print("The Even fibonacci numbers are: ",b,'\n')
ans=0;
for i in range (len(b)):
    ans=ans + b[i];
print('the sum of even number in fibonacci series till ',n,'terms is: ', ans,'\n');   
