from tkinter import *
from get import filter_matchups, get_rows
import tkinter as tk


def createNewWindow(matchup):
    root = Tk()
    root.title(matchup)
    data = get_rows(matchup)
    processed_data = []
    indexes = ["", "NAME", "MIN", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FTP", "OREB", "DREB", "REB", "AST", "STL", "BLK", "TO", "PF", "PTS", "+/-"]
    processed_data.append(indexes)
    for i, column in enumerate(data):
        player_data = []
        for j, (key, value) in enumerate(column.items()):
            player_data.append(value)

        processed_data.append(player_data)

    for i in range(len(data)): #Rows
        for j in range(1, 22): #Columns
            if j == 1 or j == 2:
                mwidth = 20
            else:
                mwidth = 5
            b = Entry(root, width=mwidth, font=('Arial',8))
            b.grid(row=i, column=j)
            b.insert(END, f"{processed_data[i][j]}")

    root.mainloop()  

master = Tk() 

master.geometry("500x500") 

def getGameInfo(event):
    # get selected list box item
    matchup=listbox.get(ANCHOR)
    createNewWindow(matchup)

games = filter_matchups()
# create listbox 
listbox = Listbox(master , font=('times 12 bold'), height=300,width=300)
# insert items into listbox
for index, game in enumerate(games):
    listbox.insert(index, game)

listbox.grid(pady=30)
# bind the click event with listbox and
# call changecolor() function
listbox.bind('<<ListboxSelect>>', getGameInfo)


# mainloop, runs infinitely 
mainloop() 
