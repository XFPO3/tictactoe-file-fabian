from random import randint
import csv
import keras.models
import numpy as np

gewonnen = False
spieler_nummer = 1
gamestate = 0
daten = []
# Definiert das Spielfeld als Liste
feld = [0, 0, 0, 0, 0, 0, 0, 0, 0]

#Funktion um das Feld visuell besser darzustellen
def printliste(feld):
    for i in range(3):
        li = [feld[i*3], feld[i*3+1], feld[i*3+2]]
        print(li)

def collect_data(file, data):
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def getMove():
    while True:
#Try macht, dass der Code bei einem Fehler nicht abgebrochen wird sondern das except ausgeführt wird
        try:
            move = int(input("Welches Feld (1-9)? ")) - 1
            if move >= 0 and move < 9:
                return move
            else:
                print("Bitte eine Zahl zwischen 1 und 9 eingeben.")
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

def getRandomMove():
    return randint(0,8)


def getMoveAI(model, board):
    inArray = np.array(board)
    inArray = inArray.reshape(1, 9)
    pred = list(model.predict(inArray))
    zahl = np.argmax(pred)

    return zahl

model = keras.models.load_model('tictactoe_model_trained.keras')


# Gib eine Eingabeaufforderung aus und lies die Eingabe des Spielers ein

printliste(feld)

while not gewonnen:
    if spieler_nummer == 1:
        feldnummer = getMove()
    else:
        feldnummer = getMoveAI(model, feld)
        print(feldnummer)

    #feldnummer = getRandomMove()


    # Überprüfe, ob das ausgewählte Feld gültig und leer ist
    if feld[feldnummer] == 0:
        feld[feldnummer] = spieler_nummer

        #Sammelt die Daten
        """if spieler_nummer == 1:
            daten = feld.copy()
        elif spieler_nummer == -1:
            daten.append(feldnummer)
            collect_data("csv_datei", daten)"""

        spieler_nummer = spieler_nummer * (-1)

    else:
        print("Feld ist bereits besetzt")

    # Horizontale und vertikale Gewinnbedingungen
    for i in range(3):
        if feld[i] == feld[i + 3] == feld[i + 6] and feld[i] != 0:
            print("Spieler " + str(feld[i]) + " hat gewonnen!")
            gewonnen = True
        if feld[i * 3] == feld[i * 3 + 1] == feld[i * 3 + 2] and feld[i * 3] != 0:
            print("Spieler " + str(feld[i * 3]) + " hat gewonnen!")
            gewonnen = True


    # Diagonale Gewinnbedingungen
    if feld[0] == feld[4] == feld[8] and feld[0] != 0:
        print("Spieler " + str(feld[0]) + " hat gewonnen!")
        gewonnen = True
    if feld[2] == feld[4] == feld[6] and feld[2] != 0:
        print("Spieler " + str(feld[2]) + " hat gewonnen!")
        gewonnen = True
    if not gewonnen and all(x != 0 for x in feld):
        print("Das Spiel ist Unentschieden")
        gewonnen = True
        spieler_nummer = 0

    """if gewonnen:
        daten = [(-1) * spieler_nummer]
        collect_data("csv_datei", daten)"""

    printliste(feld)