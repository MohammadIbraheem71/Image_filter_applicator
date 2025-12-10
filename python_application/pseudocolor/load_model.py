# utils/colorize_model.py
import tensorflow as tf
from tensorflow import keras
import os
import sys


#this file was modified to make sure it works on windows, linux, and mac
#previously we had issues with this
def resource_path(relative_path):
    #if runnning from a pyinstaller bundle
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        #if not pyisntaller, then regular execution
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    return os.path.join(base_path, relative_path)


#the perceptual loss function used to load the model
def perceptual_loss(y_true, y_pred):
    mse = tf.reduce_mean(tf.square(y_true - y_pred))
    mae = tf.reduce_mean(tf.abs(y_true - y_pred))
    return 0.7 * mse + 0.3 * mae


#we resolve the modle path
MODEL_PATH = resource_path("pseudocolor/colorization_model_faces.keras")


#we load the model here
print("looading colorization model...")

try:
    model = keras.models.load_model(
        MODEL_PATH,
        custom_objects={"perceptual_loss": perceptual_loss}
    )
    print(f"Model loaded successfully:\n   {MODEL_PATH}")

except Exception as e:
    print("Failed to load model!")
    print("Path checked:", MODEL_PATH)
    raise e
