number = int(input())
time = int(input())
sqr = number ** 0.5
startTime = time / 1000
current_time = 0

while current_time < startTime:
    current_time += 0.001

print("Square root of", number, "after", time, "is equal", sqr)
