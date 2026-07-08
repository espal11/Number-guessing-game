import random

tries = 0

print("welcome to espels number gussing game!")
print("choose a difficlty")
print("(1) EASY (2) MEDIUM (3) HARD")
d = int(input("Your choice: "))

if d == 1:
    print("EASY 1-10")
    n = random.randint(1, 10)
    while True:
        a = int(input("Enter your guess: "))
        tries += 1
        if n == a:
            print("your guess was correct")
            print("your final socre was:", tries)
            break
        elif a > n:
            print("your guess was to high")
        elif n > a:
            print("your guess was to low")
elif d == 2:
    print("MEDIUM 1-50")
    n = random.randint(1, 50)
    while True:
        a = int(input("Enter your guess: "))
        tries += 1
        if n == a:
            print("your guess was correct")
            print("your final socre was:", tries)
            break
        elif a > n:
            print("your guess was to high")
        elif n > a:
            print("your guess was to low")
else:
    print("HARD 1-100")
    n = random.randint(1, 100)
    while True:
        a = int(input("Enter your guess: "))
        tries += 1
        if n == a:
            print("your guess was correct")
            print("your final socre was:", tries)
            break
        elif a > n:
            print("your guess was to high")
        elif n > a:
            print("your guess was to low")



