def check_palindrome(str1):
    if(str1==str1[::-1]):
        return True
    else:
        return False
x=str(input())
print(check_palindrome(x))            