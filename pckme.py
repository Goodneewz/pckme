mport random
number = random.randint(1, 50)

tries = 0

while tries < 6:
    guess = int(input("Guess: "))
    tries = tries + 1
    if guess > number:
        print("Too High!")
    elif guess < number:
       print("Too Low")
    else:
       print("Correct")
       break
if tries == 6 and guess != number:
    print(f"Out of tries. The number was, {number}")
    
