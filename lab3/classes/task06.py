def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

nums = []
x = int(input())
for i in range (x):
    nums.append(int(input()))
prime_numbers = list(filter(lambda x: is_prime(x), nums))
print(prime_numbers)
