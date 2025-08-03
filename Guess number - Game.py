import random
play = "y"
while play == "y":
    number_to_guess = random.randint(1,100)
    print("I thought a number.")
    
    for i in range(1, 3):
        match i:   
            case i if i==1:
                countw=f"{i}st"
            case i if i==2:
                countw=f"{i}nd"
            case i if i==3:
                countw=f"{i}rd"
            case i if 2<i<10:
                countw=str(i+1)+"th"
            case i if i == 10:
                print("")
                print ("You guessed too many time. Game over. It was",number_to_guess)
                print("")
                break
                
        user_guess = input("Make your "+countw+" guess between 1 and 100:")
    
        while (user_guess == ""):
            user_guess = input("Make your "+countw+" guess between 1 and 100:")
    
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
        

print("")