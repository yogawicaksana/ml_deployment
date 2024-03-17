# Calories Prediction Interface

This repository contains a simple web interface for predicting calories burned based on total distance and total active minutes using a machine learning model.

## Features

- Allows users to input Total Distance (in miles) and Total Active Minutes.
- Sends a POST request to a FastAPI endpoint to get predictions.
- Displays the predicted calories burned to the user.

## Requirements

- Python 3.x
- FastAPI
- Pydantic
- Pandas

## Installation

2. Dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the FastAPI server:

    ```bash
    uvicorn ml_api:app --reload
    ```

2. Open your web browser and navigate to `http://localhost:8000` to access the interface.
   
3. Input the required information and click the "Predict Calories" button to get predictions.

## Structure

- `main.py`: Contains the FastAPI code for serving the predictions endpoint and the HTML file.
- `model/model.pkl`: Pre-trained machine learning model for predicting calories burned.
- `index.html`: HTML file containing the user interface elements.
- `requirements.txt`: List of Python dependencies.
- `notebooks/`: Contain all the required notebooks for train a simple ml models.
- `data_src`: All of data used for this project.