'''
str1=str(input())
upr=0
low=0
for i in range(len(str1)):
    if str1[i].islower():
        low+=1
    if str1[i].isupper():
        upr+=1
print(upr)
print(low)            
'''
str2=str(input())
print(sum(1 for char in str2 if char.islower()))
print(sum(1 for char in str2 if char.isupper()))
