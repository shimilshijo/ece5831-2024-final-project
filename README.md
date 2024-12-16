# Emotion Recognition System with Adaptive User Interface

## Project Overview

This repository contains the code and resources for the "Final Project" in the ECE 5831 course. 

The project focuses on to dvelop an emotion recognition system that accurately classifies facial expressions into seven categories and integrates a dynamic, adaptive user interface to enhance human-computer interaction. It includes key aspects like model development, data processing, and interactive visualization. 

This project uses FER-2013 [dataset](https://www.kaggle.com/datasets/msambare/fer2013)  that contains facial images (grayscale JPEG file with a size of 48x48 pixels.) classified into seven emotion categories:` Angry`, `Disgust`, `Fear`, `Happy`, `Neutral`, `Sad`, and `Surprise`. 


## Technologies Used:
- Python
- Tkinter - for GUI creation (file dialogs and interface components).
- PIL (Pillow) - for image processing and manipulation.
- OpenCV - for image handling and pre-processing.
- TensorFlow & Keras - for building and training deep learning models.
- NumPy - for numerical operations and array handling.
- Matplotlib & Seaborn - for data visualization (plots, confusion matrix).
- Scikit-learn - for evaluation metrics like confusion matrix and classification report


## Resources

Here are the relevant links for the project:

- **[Pre-recorded Presentation Video](https://youtu.be/yIKpY96RJtY)**: A pre-recorded video explaining the entire project from start to end. It covers the background research, dataset selection, model development, training, and validation, interpretation as well as the results of the graphical user interface (GUI).
- **[Presentation Slides](https://drive.google.com/drive/folders/1sXu-DHwk_76k78Q_WjYL3fn7D12Xc0SS?usp=drive_link)**: Slides used during the presentation summarizing the project work and key findings.
- **[Project Report](https://drive.google.com/drive/folders/1G-4KfnO0YXj56paMbyoTQLu9rM22XvUU?usp=drive_link)**: A detailed report describing the technical aspects of the project, the methods employed, and results obtained.
- **[Dataset](https://drive.google.com/drive/folders/13l-hbD04MyyVuNdMY7zn0aQXTCq7yCDs?usp=drive_link)**: The FER-2013 dataset used for this project.
- **[Demo Video](lhttps://youtu.be/Bn2F2MgZJJE?si=pQTqJKkPE8lSb6q0)**: A demo showcasing the functionality and features of the developed application.

## Repository Structure

* **final-project.ipynb:**
    * Contains jupyter notebook code for the complete project with output.
* **best_model.keras:**
    * This is the saved keras model after training.
* **run.py:**
    * File to load the adaptive UI,upload test image and perform prediction.

    This file can be executed with the command

    ```bash
    python run.py
    ```
* **dataset**
    * This directory contains sample test images for each class(2 images per class). This can be used while code execution(both jupyter notebook and run.py file)

