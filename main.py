import random
from tkinter import *

def pick_clubs_and_nations():
    distribution = random.randint(3, 6)
    clubs_and_nations = []
    for x in range(distribution):
        pick = random.choice(clubs)
        clubs_and_nations.append(pick)
        clubs.remove(pick)
    for x in range(6 - distribution):
        pick = random.choice(nations)
        clubs_and_nations.append(pick)
        nations.remove(pick)
    return clubs_and_nations

def check():

    return True

def next_turn(row, column):
    entry = Entry(window,
                  font=("Arial", 50),
                  fg="#00FF00",
                  bg="black")
    entry.pack(side=LEFT)
    click_button = Button(window, text='ok', command=check)
    click_button.pack()
    if check() is True:
        global player
        if buttons[row][column]['text'] == "" and check_winner() is False:
            if player == players[0]:
                buttons[row][column]['text'] = player
                if check_winner() is False:
                    player = players[1]
                    label.config(text=(players[1]+" turn"))
                elif check_winner() is True:
                    label.config(text=(players[0]+" wins"))
                elif check_winner() == "Tie":
                    label.config(text="Tie!")
            else:
                buttons[row][column]['text'] = player
                if check_winner() is False:
                    player = players[0]
                    label.config(text=(players[0]+" turn"))
                elif check_winner() is True:
                    label.config(text=(players[1]+" wins"))
                elif check_winner() == "Tie":
                    label.config(text="Tie!")

def check_winner():
    for row in range(1, 4):
        if buttons[row][1]['text'] == buttons[row][2]['text'] == buttons[row][3]['text'] != '':
            return True
    for column in range(1, 4):
        if buttons[1][column]['text'] == buttons[2][column]['text'] == buttons[3][column]['text'] != '':
            return True
    if buttons[1][1]['text'] == buttons[2][2]['text'] == buttons[3][3]['text'] != '':
        return True
    elif buttons[1][3]['text'] == buttons[2][2]['text'] == buttons[3][1]['text'] != '':
        return True
    elif empty_spaces() is False:
        return 'Tie'
    else:
        return False

def empty_spaces():
    spaces = 9
    for row in range(1, 4):
        for column in range(1, 4):
            if buttons[row][column]['text'] != '':
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for row in range(1, 4):
        for column in range(1, 4):
            buttons[row][column].config(text="")

    pick_clubs_and_nations()

def right_player():
    return True
    #check through the data base if the player fits the row and column and lets to make a move

clubs = ['Barcelona', 'Real Madrid',
         'Arsenal', 'Chelsea', 'Manchester United', 'Manchester City', 'Liverpool',
         'PSG',
         'Juventus', 'AC Milan', 'Inter']
nations = ['spanish', 'english', 'french', 'italian', 'german', 'dutch', 'argentinian', 'portuguese']

clubs_and_nations = pick_clubs_and_nations()
window = Tk()
window.title('Tic-Tac-Toe')
players = ['x', 'o']
player = random.choice(players)
buttons = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]
label = Label(text=player + ' turn', font=40)
label.pack(side='top')

reset_button = Button(text='restart', font=20, command=new_game)
reset_button.pack(side='top')

frame = Frame(window)
frame.pack()

i = 0
for row in range(4):
    for column in range(4):
        if row == 0 :
            if column == 0:
                pass
            else:
                buttons[row][column] = Button(frame, text=f'{clubs_and_nations[i]}', font=40, width=10, height=4)
                buttons[row][column].grid(row=row, column=column)
                i += 1
        elif column == 0:
            buttons[row][column] = Button(frame, text=f'{clubs_and_nations[i]}', font=40, width=10, height=4)
            buttons[row][column].grid(row=row, column=column)
            i += 1
        else:
            buttons[row][column] = Button(frame, text='', font=40, width=10, height=4,
                                          command=lambda row=row, column=column: next_turn(row, column))
            buttons[row][column].grid(row=row, column=column)






window.mainloop()