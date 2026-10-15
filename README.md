# Task 04: Traffic Accident Data Analysis

## Objective
Analyze traffic accident data to identify patterns related to:
- Road conditions
- Weather
- Time of day
- Accident hotspots
- Contributing factors

## Project structure
```text
traffic_accident_task04/
├── analyze.py
├── data/
│   └── accident_data.csv
├── outputs/
│   ├── 01_accidents_by_time.png
│   ├── 02_accidents_by_road_condition.png
│   ├── 03_accidents_by_weather.png
│   ├── 04_city_hotspots.png
│   ├── 05_weather_road_heatmap.png
│   ├── 06_severity_by_time.png
│   └── summary.csv
├── requirements.txt
└── README.md
```

## How to run
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Run:
   `python analyze.py`

The charts will be created in the `outputs` folder.

## Dataset
The included CSV is a **demo dataset** created for this project so it can run immediately. For a real submission, replace `data/accident_data.csv` with the Accident Dataset provided by your instructor, keeping the same column names or updating the column names in `analyze.py`.

## Key analysis questions
1. Which time of day has the most accidents?
2. Which road condition is associated with more accidents?
3. Which weather condition appears most often?
4. Which city is an accident hotspot?
5. Are severe accidents more common at particular times?
6. How do weather and road conditions interact?

## Suggested conclusion
Accident frequency can vary with time of day, road condition, and weather. Poor or wet roads and reduced visibility can be important contributing factors, while city-level counts can reveal locations that deserve additional road-safety attention. Results should be interpreted from the actual dataset used for the final submission.

## Tools used
- Python
- Pandas
- Matplotlib
- CSV data
