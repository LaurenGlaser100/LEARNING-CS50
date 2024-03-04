def get_guess():
    guess = input("What is your guess? ")
    return guess

if get_guess == 50:
    print("Correct")
else:
    print("wrong.")
print(get_guess())
