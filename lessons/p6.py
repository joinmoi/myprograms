# snakes and ladders game 

square = 1
print("welcome to the snakes and ladders game! ")

while True:
    dice_roll = int(input("Enter dice roll (2-12), or 0 to quit: "))

    if dice_roll == 0:
        print ("You quit!")
        break     

    if square+ dice_roll <= 100:
        new_position = square + dice_roll
        
        game_dict = {
            9 : 34, 
            54 : 19,
            40 : 64,
            90 : 48,
            67 : 86,
            99 : 77
        }

        if new_position in game_dict: 
            square = game_dict[new_position]
        else:
            square = new_position
   
        print (f"You are now on square {square}")
    else: 
            print (f"You rolled too high! Stay on {square}")

    if square == 100:
        print("You win!")
        break
    