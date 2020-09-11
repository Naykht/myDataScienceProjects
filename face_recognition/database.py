# ИМПОРТ БИБЛИОТЕК И МОДУЛЕЙ

import os
import glob
import numpy as np
import cv2
import tensorflow as tf
from fr_utils import *
from inception_blocks_v2 import *
from keras import backend as k

# Енкодинг картинки с помощью ConvNet в 128-размерный вектор.

k.set_image_data_format('channels_first')
fr_model = faceRecoModel(input_shape=(3, 96, 96))  # Передаем картинку в виде трех размерностей RGB разрешением 96x96


# пикселей.

# ФУНКЦИОНАЛ КАЧЕСТВА


def triplet_loss(y_true, y_pred, alpha=0.3):
    anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]

    pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, positive)), axis=-1)
    neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, negative)), axis=-1)
    basic_loss = tf.add(tf.subtract(pos_dist, neg_dist), alpha)
    loss = tf.reduce_sum(tf.maximum(basic_loss, 0.0))

    return loss


# Используем Adam Optimizer для минимизациия функционала качества Triplet Loss, коимпилируя его с Keras и используя
# уже предобученную модель.


fr_model.compile(optimizer='adam', loss=triplet_loss, metrics=['accuracy'])


# БАЗА ДАННЫХ ФОТОГРАФИЙ


def prepare_database():
    database = {}

    for file in glob.glob("images_database/*"):
        identity = os.path.splitext(os.path.basename(file))[0]
        database[identity] = img_to_encoding(file, fr_model)  # с помощью данной функции преобразуем изображение в
        # вектор 128-размерностью с помощью распознающей сети

    return database

database_real = prepare_database()
print(database_real)
