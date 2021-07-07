import random
import time

print("Rock, Paper, Sissers")
time.sleep(3)
print('''
Here are the keys:

For rock: r
For paper: p
For sissers: s

''')

i = True

while i == True:
    
    time.sleep(3)
    operations = ["rock", "paper", "sissers"]
    operation_choice = random.choice(operations)
    input_ = input("Choose: ")
    if input_ == "r":
        if operation_choice == "rock":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("Looks like its a tie!")
        if operation_choice == "paper":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("I won, HAHA")
        if operation_choice == "sissers":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("I lost, I will defeat you next time!")

    elif input_ == "p":
        if operation_choice == "rock":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("I lost, I will defeat you next time!")
        if operation_choice == "paper":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("Looks like its a tie!")
        if operation_choice == "sissers":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("I won! HAHA")

    elif input_ == "s":
        if operation_choice == "rock":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("I won! HAHA")
        if operation_choice == "paper":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("I lost! I will defeat you next time!")
        if operation_choice == "sissers":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("Looks like its a tie!")
    else:
        print("Hmm... I dont get what you are saying")
        time.sleep(2)
        print('''
    Here are the keys:

    For rock: r
    For paper: p
    For sissers: s

    ''')