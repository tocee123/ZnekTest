import random
play = "y"

while play=="y":
    signs = ["A","E","I","O"]
    to_guess=[random.choice(signs) for _ in range (4)]
    
    while True:
        print("")
        user_guess = input(f"make your guess using {signs[0]}, {signs[1]}, {signs[2]}, {signs[3]}. Guess must be 4 characters: ").upper()
        if len(user_guess) !=4:
            print("Your guess must be exactly 4 characters.")
            continue
        if not all(char in signs for char in user_guess):
            print(f"Use only letters {signs[0]}, {signs[1]}, {signs[2]}, {signs[3]}.")
            continue
        break
    print(user_guess)

    print(to_guess)



    i = 0
    while 0 <= i < 10:
        i+=1
    play=""
