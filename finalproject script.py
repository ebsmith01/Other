# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:45:17 2020

@author: evinb
"""


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Import Libraries Section
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dropout, Dense  
import datetime
import matplotlib.pyplot as plt
from pickle import dump
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint
import csv
import numpy as np
from sklearn.model_selection import train_test_split
start_time = datetime.datetime.now()
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Load Data Section
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
headlinesFull = [] #empty dictionary 
with open("joke.csv", "r", encoding = 'cp850') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for lines in csv_reader:
        headlinesFull.append(lines['full_joke']) #open and append lines to dictionary 
# shuffle and select 100000 headlines
np.random.shuffle(headlinesFull)
headlines = headlinesFull[:100000]

# add spaces to make ensure each headline is the same length as the longest headline
max_len = max(map(len, headlines))
headlines = [" "*(max_len-len(i)) + i for i in headlines]
# integer encode sequences of words
# create the tokenizer 
t = Tokenizer(char_level=True) 
# fit the tokenizer on the headlines 
t.fit_on_texts(headlines)
sequences = t.texts_to_sequences(headlines)
# vocabulary size
vocab_size = len(t.word_index) + 1
# separate into input and output
sequences = np.array(sequences)
X, y = sequences[:,:-1], sequences[:,-1]     
#make catagorical
y = to_categorical(y, num_classes=vocab_size)
seq_len = X.shape[1]
# split data for validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# define model
model = Sequential()
#embed model
model.add(Embedding(vocab_size, 50, input_length=seq_len))
#first LSTM layer
model.add(LSTM(30, return_sequences=True))
#first Dropout layer
model.add(Dropout(0.2))
#second LSTM
model.add(LSTM(30))
#second dropout
model.add(Dropout(0.2))
#hidden layer
model.add(Dense(30, activation='relu'))
#softmax output
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())
# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit model
# define the checkpoint
filepath="jopke-{epoch:02d}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
#create call back list
callbacks_list = [checkpoint]
#fit
history= model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=128,
                   epochs=1, callbacks=callbacks_list)
#store encoding
dump(t, open('tokenizer.pkl', 'wb'))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
test_loss, test_acc = model.evaluate(X_test, y_test)
print('test_loss:', test_loss)
print('test_acc:', test_acc)

stop_time = datetime.datetime.now()
print ("Time required for training:",stop_time - start_time)
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))



plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend()

plt.show()
