import random

random_num = random.randint(1, 20)
name = input("Hello! What is your name?\n")
print("Well, {fname}, I am thinking of a number between 1 and 20.\nTake a guess.\n".format(fname=name))
num = int(input())
try1 = 1

def game(guess, try_count):
    if guess < random_num:
        print("Your guess is too low.\n")
        print("Take a guess.\n")
        return False
    elif guess > random_num:
        print("Your guess is too more.\n")
        print("Take a guess.\n")
        return False
    else:
        print("Good job, " + name + "! You guessed my number in " + str(try_count) + " guesses!")
        return True

while not game(num, try1):
    num = int(input())
    try1 += 1

