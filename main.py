import time

# Welcome the user
print ("WELCOME TO THE QUIZ GAME\n")
time.sleep(1)

# Ask  the user if he or she wants to play.
playing = input("Do you want to play? \n")
time.sleep(2)
if playing == ("yes"):
    print("Okay! Let's Play!\n ")
    time.sleep(2)
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
        score = score + 1
        time.sleep(1)
        break

# Question 2
Question_2 = print("2) How many bones are in the human body?\n(a) 118\n(b) 123\n(c) 206\n(d) 115\n ")
answer_2 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_2:
        score = score + 1
        time.sleep(1)
        break

# Question 3
Question_3 = print("3) What does CPU stand for?\n(a) Central Processing Unit\n(b) Common Prompt Unit\n(c) Central Protector Unit\n(d) Central Processor Unit\n ")
answer_3 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_3:
        score = score + 1
        time.sleep(1)
        break
    

# Question 4
Question_4 = print("4) What does GPU stand for?\n(a) Great Processing User\n(b) Graphic Processing Unit\n(c) Graphic Prevention Unit\n(d) Graphics Processing Unit\n ")
answer_4 = "d"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_4:
        score = score + 1
        time.sleep(1)
        break

# Question 5
Question_5 = print("5) What does RAM stand for?\n(a) Read Access Memory\n(b) Road Again Mace\n(c) Random Access Memory\n(d) Random Again Memory\n ")
answer_5 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_5:
        score = score + 1
        time.sleep(1)
        break

# Question 6
Question_6 = print("6) What is the capital of Ghana?\n(a) Tamale\n(b) kumasi\n(c) Accra\n(d) Techiman\n ")
answer_6 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_6:
        score = score + 1
        time.sleep(1)
        break

# Question 7
Question_7 = print("7) What is the capital of Nigeria?\n(a) lagos\n(b) Kaduna\n(c) Abuja\n(d) Ibadan\n ")
answer_7 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_7:
        score = score + 1
        time.sleep(1)
        break
    

# Question 8
Question_8 = print("8) What is the cube root of 729?\n(a) 9\n(b) 5\n(c) 7\n(d) 8\n ")
answer_8 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_8:
        score = score + 1
        time.sleep(1)
        break

# Question 9
Question_9 = print("9) I am an odd number.Take away a letter and I become even.What number am I?\n(a) seven\n(b) nine\n(c) even\n(d) two\n ")
answer_9 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_9:
        score = score + 1
        time.sleep(1)
        break

# Question 10
Question_10 = print("10) If two's is a company and three's a crowd, what are four and five?\n(a) 3\n(b) 6\n(c) 9\n(d) 11\n ")
answer_10 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_10:
        score = score + 1
        time.sleep(1)
        break

# Question 11
Question_11 = print("11) The more you take, the more you leave behind?\n(a) landmarks\n(b) Thumb\n(c) fingerprint\n(d) footsteps\n ")
answer_11 = "d"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_11:
        score = score + 1
        time.sleep(1)
        break

# Question 12
Question_812= print("12) I’m tall when I’m young, and I’m short when I’m old. What am I??\n(a) candle\n(b) book\n(c) spoon\n(d) bread\n ")
answer_12 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_12:
        score = score + 1
        time.sleep(1)
        break

# Question 13
Question_13 = print("13) What has to be broken before you can use it?\n(a) broom\n(b) egg\n(c) water\n(d) rice\n ")
answer_13 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_13:
        score = score + 1
        time.sleep(1)
        break

# Question 14
Question_14 = print("14) What is full of holes but still holds water?\n(a) Basket\n(b) seive\n(c) net\n(d) sponge\n ")
answer_14 = "d"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_14:
        score = score + 1
        time.sleep(1)
        break

# Question 15
Question_15 = print("15) I have branches, but no fruit, trunk or leaves. What am I?\n(a) tree\n(b) bank\n(c) forest\n(d) bushes\n ")
answer_15 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_15:
        score = score + 1
        time.sleep(1)
        break

# Question 16
Question_16 = print("16) The more of it there is, the less you see. What is it??\n(a) darkness\n(b) light\n(c) prism\n(d) lens\n ")
answer_16 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_16:
        score = score + 1
        time.sleep(1)
        break

# Question 17
Question_17 = print("17)  What has many keys but can’t open a single lock??\n(a) cage\n(b) door\n(c) gate\n(d) piano\n ")
answer_17 = "d"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_17:
        score = score + 1
        time.sleep(1)
        break

# Question 18
Question_18 = print("18) What is black when it’s clean and white when it’s dirty?\n(a) chalkboard\n(b) white board\n(c) white cloth\n(d) plain sheet\n ")
answer_18 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_18:
        score = score + 1
        time.sleep(1)
        break

# Question 19
Question_19 = print("19) What gets bigger when more is taken away?\n(a) rice\n(b) bread\n(c) hole\n(d) farm\n ")
answer_19 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_19:
        score = score + 1
        time.sleep(1)
        break
    

# Question 20
Question_20 = print("20)  Where does today come before yesterday?\n(a) life\n(b) dictionary\n(c) stories\n(d) novels\n ")
answer_20 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_20:
        score = score + 1
        time.sleep(1.5)
        break

# users score
while score >= 10:
    print("WELL DONE. TRY HARDER NEXT TIME.Your score was", str((score/20) * 100) + "%")
    break
while score >= 15:
    print ("BRAVO. Your score was", str((score/20) * 100) + "%" )
    break
while score < 10:
    print("BETTER LUCK NEXT TIME.Your score was", str((score/20) * 100) + "%" )
    break
time.sleep(1)

# Goodbye Message
print("Thank you for playing the quiz game")
