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

- **[Pre-recorded Presentation Video](link-to-video)**: A pre-recorded video explaining the project, methodology, and results.
- **[Presentation Slides](link-to-slides)**: Slides used during the presentation summarizing the project work and key findings.
- **[Project Report](link-to-report)**: A detailed report describing the technical aspects of the project, the methods employed, and results obtained.
- **[Dataset](link-to-dataset)**: The dataset used for this project, including [brief dataset description]. (If it's a large dataset, mention how to download it).
- **[Demo Video](link-to-demo-video)**: A demo showcasing the functionality and features of the developed application.

## Files

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

