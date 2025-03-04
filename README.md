# Vehicle Traffic Data Analysis

## Description
This project performs a detailed analysis of vehicle traffic data collected from two different junctions: **Elm Avenue/Rabbit Road** and **Hanley Highway/Westway**. The analysis includes vehicle types, speed limit violations, weather conditions, and traffic flow over different hours of the day. 

The analysis generates useful insights such as the peak traffic hours, the percentage of various vehicle types (trucks, electric vehicles, scooters, etc.), the number of vehicles passing through each junction, and more. The project also visualizes the data through a histogram showing the vehicle frequency per hour at both junctions.

## Features
- **Date Input:** Allows users to input a specific date for analysis in the format `DDMMYY`.
- **Data Analysis:** Analyzes data from the traffic survey, including vehicle types, speed limits, buses, rain conditions, and more.
- **Visualization:** Generates a histogram to show vehicle traffic patterns at the two junctions for each hour of the day.
- **Results Output:** Outputs key statistics such as the total number of vehicles, vehicles passing through each junction, the percentage of vehicles over the speed limit, and more.
- **Rain Condition Count:** Keeps track of how many hours had rain and identifies the number of rainy hours for the selected date.

## Setup

### Requirements:
- Python 3.x
- `graphics.py` library (for generating histograms)
- `csv` module (for reading and processing the data)

To install the necessary Python libraries, run:
```bash
pip install graphics
