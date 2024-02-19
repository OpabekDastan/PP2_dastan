def square(N):
    for i in range(N):
        if i**2<=N:
            yield i**2
N=int(input())
for num in square(N):
    print(num)

                