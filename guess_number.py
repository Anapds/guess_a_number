import random 

print("welcome to Guess Number!")
choice_number = input("Enter a number")

if choice_number.isdigit():
    choice_number = int(choice_number) 
else:
    print("It's not a number")
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0

while True: 
    answer_user = input("Guess the number: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("It's not a number")
        continue

    n_choices = n_choices + 1

    if answer_user == random_number:
        print("You're right!")
        break
    elif answer_user > random_number:
        print("a little less friend")
    else:
        print("to low")

print("attempts: " + str(n_choices))