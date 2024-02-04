def prime_check():
     for i in nums:
         c = 0
         for j in range(1, i):
             if i % j == 0:
                 c += 1
         if c == 1:
             primes.append(i)
     print(primes)

nums = []
primes = []
x = int(input())
for i in range (x):
    nums.append(int(input()))

prime_check()