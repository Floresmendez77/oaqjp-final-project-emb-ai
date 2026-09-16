# Emotion Detection Application

Repository for the final project of the course **Developing AI Applications with Python and Flask** (IBM).

## Project Name: Emotion Detection

This project implements an AI-based web application that detects emotions (anger, disgust, fear, joy, sadness) from a given text statement, using the **Watson NLP library**. The application identifies the dominant emotion in the input text and returns a formatted response to the user.

## Features

- Emotion detection using the Watson NLP Embeddable AI library
- Output formatting to return anger, disgust, fear, joy, sadness scores and the dominant emotion
- Packaged as a reusable Python module: `EmotionDetection`
- Unit tests to validate the application's behavior
- Web deployment using the **Flask** framework
- Error handling for blank or invalid input (HTTP 400)
- Static code analysis using **PyLint**

## Project Structure

oaqjp-final-project-emb-ai/
├── EmotionDetection/
│ ├── init.py
│ └── emotion_detection.py
├── static/
├── templates/
├── server.py
├── test_emotion_detection.py
└── README.md


## How to Run

1. Clone this repository.
2. Install dependencies: `pip install flask requests`
3. Run the server: `python server.py`
4. Open the application in your browser at `http://localhost:5000`

## Author

Andrew Estheven Flores Méndez
