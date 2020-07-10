###Helper & Solution Functions###
def weirdAlgo(n):
    if n==1:
        print(1)
        return

    print(n,end=' ')
    while (n>1):
        if n%2==0:
            n=int(n/2)
            if n!=1:
                print(n,end=' ')
        else:
            n=(n*3)+1
            if n!=1:
                print(n,end=' ')
    if (n==1):
        print(1,end='')
 
###Input & Function Call###
n=int(input())
weirdAlgo(n)