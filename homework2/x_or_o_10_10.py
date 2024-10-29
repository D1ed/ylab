from tkinter import *
import random
root = Tk()
root.title("Обратные крестики-нолики")
root.geometry("850x900")
game_run = True
cross_count = 0
field  = []

def new_game():
    for row in range(10):
        for col in range(10):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 50:
            computer_move()
            check_win('O')


def check_win(smb):
    for n in range(10):
        for i in range(10):
            if n <= 5:
                check_line(field[n][i], field[n+1][i], field[n+2][i], field[n+3][i], field[n+4][i], smb)
                check_line(field[i][n], field[i][n+1], field[i][n+2], field[i][n+3], field[i][n+4], smb)
            if i <= 5 and n <= 5:
                check_line(field[n][i], field[n+1][i+1], field[n+2][i+2], field[n+3][i+3], field[n+4][i+4], smb)
            if i <= 5 and n >= 4:
                check_line(field[n][i], field[n-1][i+1], field[n-2][i+2], field[n-3][i+3], field[n-4][i+4], smb)



def check_line(a1,a2,a3,a4,a5,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = a4['background'] = a5['background'] = 'red'
        global game_run
        game_run = False

def try_win(row,col):
    res = True
    field[row][col]['text'] = 'O'
    for n in range (10):
        for i in range (10):
            if n <= 5:
                if field[n][i]['text'] == field[n+1][i]['text'] == field[n+2][i]['text'] == field[n+3][i]['text'] == field[n+4][i]['text'] == 'O':
                    res = False
                if field[i][n]['text'] == field[i][n+1]['text'] == field[i][n+2]['text'] == field[i][n+3]['text'] == field[i][n+4]['text'] == 'O':
                    res = False
                if i <= 5:
                    if field[n][i]['text'] == field[n+1][i+1]['text'] == field[n+2][i+2]['text'] == field[n+3][i+3]['text'] == field[n+4][i+4]['text'] == 'O':
                        res = False
            if i <= 5 and n >= 4:
                if field[n][i]['text'] == field[n-1][i+1]['text'] == field[n-2][i+2]['text'] == field[n-3][i+3]['text'] == field[n-4][i+4]['text'] == 'O':
                    res = False
    field[row][col]['text'] = ' '
    return res
            

def computer_move():
    i = 1
    while i <= 5000:  #определяет кол-во раз рандома, чтобы сдаться и поставить О. фактически это сложность интелекта
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if field[row][col]['text'] == ' ':
            i += 1
        if field[row][col]['text'] == ' ' and try_win(row,col) is True:
            field[row][col]['text'] = 'O'
            break

    else:
        field[row][col]['text'] = 'O'
        
        # elif field[row][col]['text'] == ' ' and try_win(row,col) is True

for row in range(10):
    line = []
    for col in range(10):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='НОВАЯ ИГРА', command=new_game)
new_button.grid(row=10, column=0, columnspan=10, sticky='nsew')
root.mainloop()