# heads or tails 

from random import choice #randomly chooses from a list

while True:

    print ("welcome to our heads or tails game!")
    print ("please choose either heads or tails.")
    while True: 
        user_input = input("User's choice: ")
        user_input = user_input.lower() #this makes everything lowercased

        if user_input in {"heads", "tails", "head", "tail"}:
            # user input was valid, we can exit the infinite loop 
            break #allows us to exit a looping strcture
        else: 
            print("please type in heads or tails. :) ")
    #end of while
    flip_result = choice (["heads", "tails"])
    print(f"The computer flipped:  {flip_result}")
    if user_input in {"heads", "head"} and flip_result == "heads":
        print("The user guessed correctly!")
    elif  user_input in {"tails", "tail"} and flip_result == "tails":
        print("The user guessed correctly!")
    else: 
        print("you lost hehe")
    
    user_input = input("do you want to leave the game? yes/no: ")
    if user_input.lower() == "yes":
        print("bye!!")
        break
