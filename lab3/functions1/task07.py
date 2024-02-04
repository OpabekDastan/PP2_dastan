def has_33(list1):
    for i in range(len(list1)):
        if(list1[i] == 3 and list1[i+1] == 3):
            return True
        elif(list1[i]==3 and list1[i+1] != 3):
            return False

print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3]))      
print(has_33([3, 1, 3]))