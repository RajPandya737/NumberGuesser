# Handwritten Digit Recognition using Neural Network

This repository contains a program that allows users to draw digits on a screen using Pygame, and then uses a trained neural network (TensorFlow) to guess the drawn digit with up to 99.8% accuracy. The program also utilizes OpenCV and Tkinter for handling image processing and graphical user interface, respectively.

![ezgif com-gif-maker](https://github.com/RajPandya737/NumberGuesser/assets/99134716/913e43d8-96f6-4130-ab5e-68de0aa66e6b)


## Prerequisites

Before running the program, ensure you have the following libraries installed:

- Pygame
- TensorFlow
- OpenCV
- Numpy
- Tkinter (usually comes with Python)

You can install these libraries using `pip`, make sure python is installed on your machine:

```bash
pip install pygame tensorflow opencv-python numpy
```

## Getting Started

1. Clone this repository to your local machine:
```bash
git clone https://github.com/RajPandya737/NumberGuesser.git
```
2. Change to the project directory:
```bash
cd NumberGuesser/NumberGuesser
```
3. Run the program:
```bash
python main.py
```

## Usage

1. Upon running the program, a window will appear, displaying an empty drawing canvas.

2. Draw a single digit (0-9) using your mouse on the drawing canvas.

3. Press the enter key to let the neural network analyze the drawn digit, 'saved' will appear within the terminal to notify you if the image was saved.

4. A pop up will tell you what digit the model thinks you drew.

## Neural Network Model

The neural network model used for handwritten digit recognition is trained on the MNIST dataset, which is a large database of handwritten digits

The trained model is already included in the repository and will be loaded automatically when you run the program.
