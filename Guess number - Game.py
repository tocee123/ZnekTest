import random
play = "y"
while play == "y":
    number_to_guess = random.randint(1,100)
    print("I thought a number.")
    
    for i in range(1, 11):
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
        
        match (number_to_guess,user_guess):
            case (x,y) if x < y:
                print(user_guess, "is too big.")
            case (x,y) if x > y:
                print(user_guess,"is too small.")
            case (x,y) if x == y:
                print("Correct! You guessed", number_to_guess,".")
                break
            case _:
                print("Unexpected input")
        
    print("")
    
    play = ""
    
    while play != "y" or play != "n":
        play = input("Do you want to play again?   Yes [y]   No [n]")
        match play:
            case play if play == "n":
                print("")
                print ("end")
                print("")
                break
            case play if play == "y":
                play = "y"
                print("")
                print ("Let's play again!")
                print("")
                break
            case play if play != "y" or play != "n":
                play = input("Do you want to play again?   Yes [y]   No [n]")

        

print("")