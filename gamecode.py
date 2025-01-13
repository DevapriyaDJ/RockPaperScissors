import random

choices=['rock','paper','scissors']
user_score = 0
computer_score = 0
rounds = int(input("enter the number of rounds you want to play"))
for i in range(rounds):
    user_choice = input("\nEnter 'rock','paper',or 'scissors' :").lower()
    if user_choice not in choices:
        print("Invalid choice!Please enter 'rock','paper',or 'scissors'.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")
    print(f"Your choice:{user_choice}")
    if user_choice == computer_choice:
        print("it's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score +=1
    #display current scores
        print(f"Current scores - You:{user_score},Computer:{computer_score}")
print("\nGame Over!")
print(f"Final Scores - You:{user_score},Computer :{computer_score}")

if user_score > computer_score:
    print("Congrats! you are the winner")
elif user_score < computer_score:
    print("Computer is the winner. better luck next time!")
else:
    print("it's a tie match")
