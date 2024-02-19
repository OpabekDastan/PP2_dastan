def rangee(N):
    for i in range(N):
        if i%3==0 and i%4==0:
            yield i
N=int(input())
for num in rangee(N):
    print(num)

                