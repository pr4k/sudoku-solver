import cv2
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
CATEGORIES = ["1", "2", "3", "4", "5",
	      "6", "7", "8", "9", "0",
	      ]
def prepare(file):
    IMG_SIZE = 28
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
model = tf.keras.models.load_model("CNN.model")
image = "test.jpg" #your image path
image = prepare(image)
prediction = model.predict([image])
print(prediction)
prediction = list(prediction[0])
print("Predicted Number is: ",CATEGORIES[prediction.index(max(prediction))])
