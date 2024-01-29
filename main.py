# Welcome the user
print ("WELCOME TO THE QUIZ GAME")

# Ask  the user if he or she wants to play.
playing = input("Do you want to play? ")
if playing == ("yes"):
    print("Okay! Let's Play! ")
else:
    quit()

# Chances
chances = 1
print ("You will have", chances, "chance to answer correctly. Please choose the correct option to the question\n")

#score
score = 0

# Question 1
Question_1 = print("1) Is the coding language Python, named after a snake?\n(a) Yes\n(b) No\n ")
answer_1 = "b"
for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_1:
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        print("The correct answer is", answer_1, "\n")

# users score
print("You got " + str(score) + " questions correct! ")

# Goodbye Message
print("Thank you for playing the quiz game")
