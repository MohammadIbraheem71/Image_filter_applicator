from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow import keras
import cv2
from pseudocolor.luminance import apply_luminance

from pseudocolor.load_model import model

IMG_SIZE = 128

#this is the colorization function, uses the luminance function for detail transfer. 
#returns the original image and the enhanced image
def colorize_image(image_path):
    print(f"\n🎨 Colorizing: {image_path}")

    # Load grayscale
    img = Image.open(image_path)
    gray_img = img.convert('L')
    original_size = img.size

    # Resize for model
    gray_resized = gray_img.resize((IMG_SIZE, IMG_SIZE), Image.Resampling.LANCZOS)
    gray_arr = np.array(gray_resized, dtype=np.float32) / 255.0
    gray_arr = np.expand_dims(gray_arr, axis=(0, -1))  # (1, IMG_SIZE, IMG_SIZE, 1)

    # Run model prediction
    pred = model.predict(gray_arr, verbose=0)[0]  # (IMG_SIZE, IMG_SIZE, 3)
    pred = np.clip(pred, 0, 1)

    # Convert to RGB and resize to original
    color_img = Image.fromarray((pred * 255).astype(np.uint8))
    color_img = color_img.resize(original_size, Image.Resampling.LANCZOS)

    # Apply luminance enhancement
    enhanced_img = apply_luminance(color_img, gray_img)

    print("✅ Colorization complete!")
    return gray_img, enhanced_img