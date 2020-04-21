import numpy as np
import cv2
import scipy.ndimage
from skimage.feature import hog
from skimage import data, color, exposure
from sklearn.model_selection import  train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

knn = joblib.load('models/knn_model.pkl')
def feature_extraction(image):
    return hog(color.rgb2gray(image), orientations=8, pixels_per_cell=(4, 4), cells_per_block=(7, 7))
def predict(img):
    df = feature_extraction(img)
    predict = knn.predict(df.reshape(1,-1))[0]
    predict_proba = knn.predict_proba(df.reshape(1,-1))
    return predict, predict_proba[0][predict]

