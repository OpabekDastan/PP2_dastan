def rangee(N):
    for i in range(N):
        if i<=N:
            yield i
N=int(input())
for num in rangee(N):
    print(num)

                