#This program loads the model, upload the test image through UI and  handle adaptive UI based on emotion and displays the prediction
import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk
import numpy as np
import cv2
import tensorflow as tf

# Load the trained model
# model = tf.keras.models.load_model('new_model.h5')
model = tf.keras.models.load_model('best_model.keras')

# Define emotion categories
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# GUI root
root = tk.Tk()
root.title("Emotion Detection with Adaptive UI")
root.geometry("600x500")


def load_image(file_path):
    '''Function to load and preprocess image'''
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (48, 48))  # Resize to match model input
    img = img / 255.0  # Normalize
    img = np.expand_dims(img, axis=-1)  # Add color channel dimension
    img = np.expand_dims(img, axis=0)   # Add batch dimension
    return img

# Function to handle adaptive UI based on emotion
def adaptive_interface(emotion):
    if emotion == "Happy":
        root.configure(bg="yellow")
        response_label.config(text="Bright theme applied! Keep smiling!", fg="green")
    elif emotion == "Sad":
        root.configure(bg="lightblue")
        response_label.config(text="Soothing colors applied. Take it easy.", fg="blue")
    elif emotion == "Angry":
        root.configure(bg="lightgrey")
        response_label.config(text="Calm theme applied. Take a deep breath.", fg="red")
    else:
        root.configure(bg="white")
        response_label.config(text="Neutral theme applied.", fg="black")

def detect_emotion():
    '''Function to detect emotion from loaded image'''
    file_path = filedialog.askopenfilename()
    if file_path:
        img = load_image(file_path)
        
        # Make prediction
        predictions = model.predict(img)
        predicted_class_idx = np.argmax(predictions)
        predicted_emotion = emotion_labels[predicted_class_idx]
        prediction_score = predictions[0][predicted_class_idx]  # Get the score for the predicted class
        
        # Display prediction with score
        emotion_label.config(text=f"Detected Emotion: {predicted_emotion} ({prediction_score*100:.2f}%)")
        
        # Update adaptive interface
        adaptive_interface(predicted_emotion)

        # Show the selected image in the interface
        display_img = Image.open(file_path)
        display_img = display_img.resize((200, 200))
        tk_img = ImageTk.PhotoImage(display_img)
        image_label.config(image=tk_img)
        image_label.image = tk_img


# UI Components
title_label = Label(root, text="Emotion Detection with Adaptive UI", font=("Helvetica", 16))
title_label.pack(pady=10)

image_label = Label(root)
image_label.pack()

detect_button = tk.Button(root, text="Upload Image for Emotion Detection", command=detect_emotion)
detect_button.pack(pady=20)

emotion_label = Label(root, text="", font=("Helvetica", 14))
emotion_label.pack(pady=10)

response_label = Label(root, text="", font=("Helvetica", 12))
response_label.pack(pady=10)

# Run the Tkinter GUI
root.mainloop()
