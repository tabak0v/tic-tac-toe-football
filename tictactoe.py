import random
from tkinter import *
import openai



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

def next_turn(row, column):
    def submit():
        return None
    def delete():
        entry.delete(0, END)

    def backspace():
        entry.delete(len(entry.get()) - 1, END)

    window = Tk()
    entry = Entry(window,
                  font=("Arial", 50),
                  fg="#00FF00",
                  bg="black")
    entry.pack(side=LEFT)
    submit_button = Button(window, text="submit", command=submit)
    submit_button.pack(side=RIGHT)
    delete_button = Button(window, text="delete", command=delete)
    delete_button.pack(side=RIGHT)
    backspace_button = Button(window, text="backspace", command=backspace)
    backspace_button.pack(side=RIGHT)
    window.mainloop()

    def check(name):
        name = entry.get()
        openai.api_key = "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"
        model_engine = "text-davinci-003"
        prompt = f"Has {name} played for {buttons[0][column]}"
        # задаем макс кол-во слов
        max_tokens = 1
        # генерируем ответ
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # выводим ответ
        result_row = completion.choices[0].text
        print(result_row)
        prompt = f"Has {name} played for {buttons[row][0]} "
        # задаем макс кол-во слов
        max_tokens = 1
        # генерируем ответ
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # выводим ответ
        result_column = completion.choices[0].text
        print(result_column)
        if "Yes" in result_column and "Yes" in result_row:
            global player
            if buttons[row][column]['text'] == "" and check_winner() is False:
                if player == players[0]:
                    buttons[row][column]['text'] = player
                    if check_winner() is False:
                        player = players[1]
                        label.config(text=(players[1] + " turn"))
                    elif check_winner() is True:
                        label.config(text=(players[0] + " wins"))
                    elif check_winner() == "Tie":
                        label.config(text="Tie!")
                else:
                    buttons[row][column]['text'] = player
                    if check_winner() is False:
                        player = players[0]
                        label.config(text=(players[0] + " turn"))
                    elif check_winner() is True:
                        label.config(text=(players[1] + " wins"))
                    elif check_winner() == "Tie":
                        label.config(text="Tie!")
        else:
            next_turn(row,column)

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

'''def right_player(row, column):

   def submit():
       if right_player(row, column) is True:
           next_turn(row, column)
       else:
           print("Player doesn't fit")
   def delete():
       entry.delete(0, END)

   def backspace():
       entry.delete(len(entry.get()) - 1, END)

   window = Tk()

   entry = Entry(window,
                 font=("Arial", 50),
                 fg="#00FF00",
                 bg="black")
   entry.pack(side=LEFT)

   submit_button = Button(window, text="submit", command=submit)
   submit_button.pack(side=RIGHT)

   delete_button = Button(window, text="delete", command=delete)
   delete_button.pack(side=RIGHT)

   backspace_button = Button(window, text="backspace", command=backspace)
   backspace_button.pack(side=RIGHT)

   window.mainloop()

   name = entry.get()
   openai.api_key = "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"
   model_engine = "text-davinci-003"
   prompt = f"Has {name} played for {buttons[row][0]}"
   # задаем макс кол-во слов
   max_tokens = 1
   # генерируем ответ
   completion = openai.Completion.create(
       engine=model_engine,
       prompt=prompt,
       max_tokens=1024,
       temperature=0.5,
       top_p=1,
       frequency_penalty=0,
       presence_penalty=0
   )
   # выводим ответ
   result_row = completion.choices[0].text
   print(result_row)
   prompt = f"Has {name} played for {buttons[0][column]} "
   # задаем макс кол-во слов
   max_tokens = 1
   # генерируем ответ
   completion = openai.Completion.create(
       engine=model_engine,
       prompt=prompt,
       max_tokens=1024,
       temperature=0.5,
       top_p=1,
       frequency_penalty=0,
       presence_penalty=0
   )
   # выводим ответ
   result_column = completion.choices[0].text
   print(result_column)
   if "Yes" in result_column and "Yes" in result_row:
       result = True
       return result
   else:
       result = False
       return result'''



clubs = ['Barcelona', 'Real Madrid',
         'Arsenal', 'Chelsea', 'Manchester United', 'Manchester City', 'Liverpool',
         'PSG',
         'Juventus', 'AC Milan', 'Inter']
nations = ['Spain', 'England', 'France', 'Italy', 'German', 'Dutch', 'Argentina', 'Portugal']

clubs_and_nations = pick_clubs_and_nations()
window = Tk()
window.title('Tic-Tac-Toe')
players = ['X', 'O']
player = random.choice(players)
buttons = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]
label = Label(text=player + ' turn', font=80)
label.pack(side='top')



reset_button = Button(text='restart', font=80, command=new_game)
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
                buttons[row][column] = Button(frame, text=f'{clubs_and_nations[i]}', font=40, width=30, height=12)
                buttons[row][column].grid(row=row, column=column)
                i += 1
        elif column == 0:
            buttons[row][column] = Button(frame, text=f'{clubs_and_nations[i]}', font=40, width=30, height=12)
            buttons[row][column].grid(row=row, column=column)
            i += 1
        else:
            buttons[row][column] = Button(frame, text='', font=40, width=30, height=12,
                                          command=lambda row=row, column=column: next_turn(row, column))
            buttons[row][column].grid(row=row, column=column)
            #buttons[row][column] = Button(frame, command=lambda row=row, column=column: right_player(row, column))






window.mainloop()