import csv

def filter_winner(file, output_file):
    filtered_data = []

    with open(file, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    temp_game = []
    for row in data:
        if len(row) == 1:
            # Gewinner überprüfen
            result = int(row[0])
            if result == -1:  # Nur Spiele speichern wo -1 gewinnt
                #Extend benutzen und nicht append weil sonst eine Unterliste zur Liste hinzugefügt wird und nicht die einzelnen Elemente
                filtered_data.extend(temp_game)
            #Wenn der Spieler nicht -1 ist, wird die Liste wieder geleert.
            temp_game = []
        else:
            temp_game.append(row)

    # Gefilterten Daten in das neue CSV file schreiben
    with open(output_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(filtered_data)

filter_winner("csv_datei", "filtered_csv_datei.csv")
