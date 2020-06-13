l1=list(map(int, input("Enter the numbers separated by space").split()))
l2=[]
for x in l1:
    if x>0:
        l2.append(x)
print(l2)
