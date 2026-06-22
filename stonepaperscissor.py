import random
choices = ["stone", "paper", "scissor"]
user_score = 0
computer_score = 0
rounds = int(input("Enter the number of rounds: "))
for i in range(rounds):
    user = input("\nEnter stone, paper or scissor: ").lower()
    computer = random.choice(choices)
    print("Computer chose:", computer)
    if user == computer:
        print("It's a Tie!")
    elif (user == "stone" and computer == "scissor") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissor" and computer == "paper"):
        print("You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1
print("\n----- Final Score -----")
print("User Score:", user_score)
print("Computer Score:", computer_score)
if user_score > computer_score:
    print("You are the Winner!")
elif computer_score > user_score:
    print("Computer is the Winner!")
else:
    print("Match Draw!")
