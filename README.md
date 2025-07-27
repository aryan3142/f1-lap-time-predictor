# F1 Lap Time Predictor

An F1 Lap Time Predictor is a machine learning or statistical model that predicts the total time a Formula 1 car/driver will take to complete a full lap of a racing circuit (A machine learning project to predict Formula 1 lap times using sector times and tire data).

# Purpose / Why It's useful ?
F1 teams, engineers, and data scientists use lap time prediction for:
- Race Strategy: Predict lap time with different tires, fuel loads or weather
- Qualifying sim: Estimate weather the next lap will be faster/slower
- Setup evaludation: See impact of car changes (e.g., downforce) on lap time.
- Driver comparison: Predict time based on driving style or telemetry

## Overview

This project uses the FastF1 Python package to access official Formula 1 timing data and builds a linear regression model to predict lap times based on:

- Sector times (S1, S2, S3)
- Tire compound 
- Tire life

## Requirements

- Python 3.8+
- FastF1
- pandas
- scikit-learn
- matplotlib
- seaborn

## Installation

```bash
git clone https://github.com/yourusername/f1-lap-time-predictor.git
cd f1-lap-time-predictor
pip install -r requirements.txt
```

## Project Structure

```
f1-lap-time-predictor/
├── src/
│   ├── preprocess.py    # Data preprocessing functions
│   └── model.py         # ML model implementation
├── notebooks/
│   └── lap_time_exploration.ipynb    # EDA and model evaluation
├── cache/               # FastF1 cache directory
└── README.md
```

## Usage

The main script can be run to train and evaluate the model:

```bash
python lap_time_predictor.py
```

For exploratory analysis, check out the Jupyter notebook in the `notebooks` directory.

## Model Performance

Current model metrics using 2023 Silverstone qualifying data:
- R² Score: ~0.99
- Mean Absolute Error: ~0.1 seconds

## License

MIT

## Contributing

Pull requests are welcome. For major changes, please open an issue first to

