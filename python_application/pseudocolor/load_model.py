# utils/colorize_model.py
import tensorflow as tf
from tensorflow import keras

MODEL_PATH = "pseudocolor\colorization_model_faces.keras"

def perceptual_loss(y_true, y_pred):
    mse = tf.reduce_mean(tf.square(y_true - y_pred))
    mae = tf.reduce_mean(tf.abs(y_true - y_pred))
    return 0.7 * mse + 0.3 * mae

print("📥 Loading colorization model...")
model = keras.models.load_model(MODEL_PATH, custom_objects={'perceptual_loss': perceptual_loss})
print("✅ Model loaded once!")
