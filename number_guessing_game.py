"""
Author :- Cyber Army
GitHub :- https://github.com/cyber-army-20
Facebook :- https://www.facebook.com/profile.php?id=61555946427371
Contact :- https://t.me/Cyber_Army_Chat_Bot
Through us, you can create 
all the Termux commands 
in your name or that 
of your group :- https://github.com/cyber-army-20/Termux_Command_Making
"""
import random
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    members = []
    member_input = input("How many members want to play? :- ")
    
    try:
        member_number = int(member_input)
        if member_number < 1:
            print("Please enter a number greater than 0.")
            time.sleep(1)
            return main()
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        time.sleep(1)
        return main()

    for i in range(1, member_number + 1):
        name = input(f"[{i}] Enter Member Name :- ")
        members.append(name)
    
    try:
        last_num = int(input("Enter your last guessing range :- "))
        real_number = random.randint(1, last_num)
        guess_game(real_number, members)
    except ValueError:
        print("Invalid range! Restarting...")
        time.sleep(1)
        main()

def guess_game(real_number, members):
    clear()
    game_over = False
    while not game_over:
        for member in members:
            try:
                inp = int(input(f'\n{member}, guess the number :- '))
                message, is_correct = check_guess(real_number, inp)
                
                if is_correct:
                    print(f"Congratulations {member}! {message}")
                    game_over = True
                    break
                else:
                    print(message)
            except ValueError:
                print("Please enter a valid number.")

def check_guess(real_number, inp):
    if real_number == inp:
        return "You won the game!", True
    elif real_number < inp:
        return f"The number is lower than {inp}.", False
    else:
        return f"The number is higher than {inp}.", False

if __name__ == '__main__':
    os.system("xdg-open https://t.me/Cyber_Army_Backup1")
    main()
    
    

