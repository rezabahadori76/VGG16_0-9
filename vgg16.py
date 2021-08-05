# -*- coding: utf-8 -*-
"""vgg16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rRicN44BIEO5LtqaH2xsYmt_DO-8nhsi
"""

import tensorflow as tf
from keras import callbacks
from keras import optimizers
from keras.layers import Dropout, Flatten, Dense,Conv2D
from keras.optimizers import Adam
from keras.applications.vgg16 import VGG16
from keras.datasets import cifar10
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import os
import cv2
from tensorflow.keras.utils import to_categorical
import numpy as np
from tensorflow.keras import Model
input_shape = (224, 224, 3)
#(X_train, y_train), (X_test, y_test) = cifar10.load_data()
#Y_train = to_categorical(y_train)
#Y_test = to_categorical(y_test)

data_path = '/content/drive/MyDrive/Digits'
images = []
classname = []
images_path = os.listdir(data_path)
images_path_len = len(images_path)
counter =0
while counter < images_path_len :
    pics_list = os.listdir ( data_path + "/" + images_path[counter] )
    for img in pics_list :
        pic = cv2.imread(data_path + "/" + images_path[counter] + "/" + img)
        pic = cv2.resize(pic,(224,224))
        images.append(pic)
        classname.append(images_path[counter])
    counter+=1;
images = np.array(images)
classname = np.array(classname)

from keras.applications.vgg16 import VGG16
model = VGG16(weights='imagenet')
print(model.summary())

x_train, x_validation, y_train, y_validation = train_test_split(images, classname, test_size= 0.2)
x_train = x_train.reshape(x_train.shape[0],x_train.shape[1],x_train.shape[2],3)
x_validation = x_validation.reshape(x_validation.shape[0],x_validation.shape[1],x_validation.shape[2],3)
X_train_resized=x_train
X_test_resized=x_validation

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_train = le.fit_transform(y_train)
y_validation = le.fit_transform(y_validation)
y_train = to_categorical(y_train)
y_validation = to_categorical(y_validation)

from keras.models import Sequential, load_model, Model
vgg16_model = Sequential()
for layer in model.layers[:-3]:
    vgg16_model.add(layer)

vgg16_model.summary()

for layer in vgg16_model.layers[:]:
    layer.trainable = False
    print('Layer' + layer.name + 'frozen')
vgg16_model.summary()

last = vgg16_model.output
#x = Flatten()(last)
x = Dense(500, activation='relu')(last)
x = Dropout(0.3)(x)
x = Dense(200, activation='relu')(x)
x = Dense(9, activation='softmax')(x)
t_model = Model(inputs=vgg16_model.input, outputs=x)

t_model.compile(loss="categorical_crossentropy", optimizer=optimizers.Adam(), metrics=["accuracy"])
t_model.summary()

print(X_train_resized.shape)
print(y_train.shape)
print(X_test_resized.shape)
print(y_validation.shape)

history = t_model.fit(X_train_resized,y_train ,batch_size = 25,epochs=100,validation_data=(X_test_resized,y_validation),)

import matplotlib.pyplot as plt
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()