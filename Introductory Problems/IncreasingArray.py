import math
def convIncreasing(l):
    ans=0
    prev=l[0]
    for i in range(len(l)):
        if (prev-l[i])>0:
            ans+=prev-l[i]
            l[i]+=prev-l[i]
        prev=l[i]    
    return ans
    
 
n=int(input())
nums=[int(x) for x in input().split(' ')]
print(convIncreasing(nums))