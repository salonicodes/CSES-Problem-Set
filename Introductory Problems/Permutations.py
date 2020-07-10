import math
def beautifulPermut(n):
    l=[]
    if n%2!=0:
        k=n-1
        while (k>1):
            l.append(str(k))
            k-=2
            
        k=n
        while (k>=1):
            l.append(str(k))
            k-=2
    elif n%2==0:
        k=n-1
        while (k>=1):
            l.append(str(k))
            k-=2
        k=n
        while (k>1):
            l.append(str(k))
            k-=2
    return l
 
       
    
 
n=int(input())
if n==1:
    print(1)
elif n<=3:
    print('NO SOLUTION')
else:
    print(' '.join(beautifulPermut(n)))