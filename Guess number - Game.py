import random

def getOrderedNumberWithSuffix(i : int):
    return f"{i}th" if i > 3 else f"{i}{['st', 'nd', 'rd'][i-1]}"

max = 3
play = "y"

while play == "y":
    number_to_guess = random.randint(1,100)
    print("I thought a number.")
    
    for i in range(1, max):
        if i == max:
            print (f"\nYou guessed too many time. Game over. It was {number_to_guess}\n")
            break
        
        countw = getOrderedNumberWithSuffix(i)
                
        user_guess = input(f"Make your {countw} guess between 1 and 100:")
    
        while (user_guess == ""):
            user_guess = input(f"Make your {countw} guess between 1 and 100:")
    
        user_guess = int(user_guess)

        if number_to_guess < user_guess:
            print(user_guess, "is too big.")
        if number_to_guess > user_guess:
            print(user_guess,"is too small.")
        if number_to_guess == user_guess:
            print("Correct! You guessed", number_to_guess,".")
        
    print("")
    
    play = ""
    
    while play not in ['n', 'y']:
        play = input("Do you want to play again?Yes [y]   No [n]")
        if play == "n":
            print ("\nend\n")
            break
        if play == "y":
            print ("\nLet's play again!\n")
            break
