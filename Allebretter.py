import csv

zahlen = [1,0,-1]

def collect_data(file,data):
    with open(file,'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def gewonnen(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != 0:
            return board[combo[0]]
    return 0

def bretter_generieren(liste, length):

    if length == 0:
        eins = liste.count(1)
        negativ = liste.count(-1)
        null = liste.count(0)

        if (eins-negativ == 1 or eins-negativ == 0) and null > 0:
            if gewonnen(liste) == 0:
                collect_data('bretter.csv', liste)
        return
    for i in zahlen:
        bretter_generieren(liste+[i], length - 1)

bretter_generieren([], 9)
