def missed(n,nums):
    hash={}
    for i in nums:
        hash[i]=True
    for i in range(1,n+1):
        if i in hash:
            continue
        else:
            print(i)
            return
    
 
n=int(input())
nums=[int(x) for x in input().split(' ')]
missed(n,nums)