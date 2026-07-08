import random

print("welcome to espels number gussing game!")
print("choose a difficlty")
print("(1) EASY (2) MEDIUM (3) HARD")
d = int(input("Your choice: "))

if d == 1:
    print("EASY")
    n = random.randint(1, 10)
    a = int(input("Your guess: "))
    if n == a:
        print("you guess was correct!")
    else:
        print("your guess were wrong :C")
        print("the right awnser was:", n)
elif d == 2:
    print("medium")
    n = random.randint(1, 25)
    a = int(input("Your guess: "))
    if n == a:
        print("your guess was correct!")
    else:
        print("your guess were wrong :C")
        print("the right awnser was:", n)
elif d == 3:
    print("HARD")
    n = random.randint(1, 50)
    a = int(input("Your guess: "))
    if n == a:
        print("you guess was correct!")
    else:
        print("your guess were wrong :C")
        print("the right awnser was:", n)