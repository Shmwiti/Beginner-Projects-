import random

def play():
    user = input ("Whats y0ur choice..??? 'r' for rock, 'p' for paper and 's'\n for scissors")
    computer = random.choice(['r' , 'p' , 's'])


    if user == computer:
        return "IT'S A TIE"

    if is_win(user , computer):
        return "YOU WIN...!!!"

    return "YOU LOST"



def is_win(player , opponent ):
    if(player =='r' and opponent == 's') or (player =='s' and opponent == 'p') \
        or (player =='p' and opponent == 'r'):
        return True


print(play())