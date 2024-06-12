import csv
import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from matplotlib import pyplot as plt

# --- Definitions -------

#categorical_crossentropy anstelle von mean_squared_error????
def nn_model():
    model = Sequential()
    model.add(Dense(81, input_shape=(9,), kernel_initializer='normal', activation='tanh'))
    model.add(Dense(729, kernel_initializer='normal', activation='tanh'))
    model.add(Dense(81, kernel_initializer='normal', activation='tanh'))
    model.add(Dense(9, kernel_initializer='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Funktion zum Laden der gefilterten Daten
def load_data(file):
    x = []
    y = []
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 10:
                x.append([int(i) for i in row[:-1]])
                y.append(int(row[-1]))
    return np.array(x), np.array(y)

# ---- main programm  ------

#Daten Laden
trainX, trainY = load_data("updated_bretter.csv")

# Zusammenfassung des geladenen Datensets
print('Train: X=%s, y=%s' % (trainX.shape, trainY.shape))

#Werte normieren, damit sie besser verarbeitet werden können (0, 0.5 oder 1) (Fragen ob das nötig ist)
#trainX = trainX /2 + 0.5

# y-Werte one hot encoden
#Was macht das bruh Stimmt das? vorallem das [1]
trainY = to_categorical(trainY)
num_classes = trainY.shape[1]

# Modell erstellen
model = nn_model()

# Modell trainieren
history = model.fit(trainX, trainY, epochs=150, batch_size=32, verbose=1)

# Modell speichern
model.save('tictactoe_model_trained.keras')

# Modell evaluieren
scores = model.evaluate(trainX, trainY, verbose=1)
print("Accuracy: %.2f%%" % (scores[1] * 100))
print("Loss: %.2f%%" % (scores[0] * 100))

# Modell evaluieren
figure, axis = plt.subplots(1, 2)
axis[0].plot(history.history['accuracy'])
axis[0].set_title('model accuracy')
axis[0].set_ylabel('accuracy')
axis[0].set_xlabel('epoch')
axis[0].legend(['train'], loc='upper left')
axis[1].plot(history.history['loss'])
axis[1].set_title('model loss')
axis[1].set_ylabel('loss')
axis[1].set_xlabel('epoch')
axis[1].legend(['train'], loc='upper left')
plt.show()





