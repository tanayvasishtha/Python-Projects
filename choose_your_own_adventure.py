name=input("What is your name? ")
print("Hello, "+name+"! Welcome to the Choose Your Own Adventure game!")

answer=input("You are on a dirt road, it has come to a fork. Do you go left or right? ").lower()

if answer == "left":
    answer=input("You come across a river. Do you swim across or go around? Type walk to walk and swim to swim across: ").lower()
    
    if answer == "swim":
        print("You swam across the river and were eaten by an alligator. You Lose.")
    elif answer == "walk":
        print("You walk around the river and walk for miles due to which your water is finished. You Lose.")
    else:
        print("That is not a valid option. You Lose.") 

elif answer == "right":
    answer=input("You come to a bridge, it looks unstable. Do you cross or go back? ").lower()
    
    if answer == "cross":
        answer=input("You cross the bridge and meet the stranger. Do you talk to them(yes/no)? ").lower()
        if answer == "yes":
            print("The stranger was a wizard and gave you a magic wand. You Win!")
        elif answer == "no":
            print("The stranger was a wizard and turned you into a frog. You Lose.")
        else:
            print("That is not a valid option. You Lose.")    
         

    elif answer == "go back":
        print("You go back and are eaten by a bear. You Lose.")
    
    else:
        print("That is not a valid option. You Lose.")

else:
    print("That is not a valid option. You Lose.")

print("Thank you for playing the Choose Your Own Adventure game!",name)