def unique_list(list1):
    list1.sort()
    uniq_list=[]
    for i in range(len(list1)-1):
        if(list1[i]!=list1[i+1]):
            uniq_list.append(list1[i])
    uniq_list.append(list1[-1])
    return uniq_list        
            
            
x=int(input())
a=[]
for i in range(x):
    a.append(int(input()))    
ans=unique_list(a)
print(ans)