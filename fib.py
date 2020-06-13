n=int(input('How many terms should be displayed?'))

if n<=0:
    print('Please input a positive integer')

else:
    count=0
    n1=0
    n2=1
    
    while count<n:
        print(n1)
        count+=1
        temp=n1+n2
        n1=n2
        n2=temp
    
