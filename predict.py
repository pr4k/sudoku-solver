import cv2
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
CATEGORIES = ["1", "2", "3", "4", "5",
	      "6", "7", "8", "9", "0",
	      ]
def predict(img_array):
    model = tf.keras.models.load_model("CNN.model")
    IMG_SIZE = 28
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    new_array=new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    prediction = model.predict([new_array])
    prediction = list(prediction[0])
    number = CATEGORIES[prediction.index(max(prediction))]
    print(number)
    return number
