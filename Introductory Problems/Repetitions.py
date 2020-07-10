def checkMaxRepeated(str):
    i=0
    temp=''
    ans=1
    count=0
    while (i<len(str)):
        if temp==str[i]:
           count+=1
        else:
            temp=str[i]
            count=1
        ans=max(count,ans)
        i+=1
    return ans
    
 
dnaString=input()
print(func(dnaString))