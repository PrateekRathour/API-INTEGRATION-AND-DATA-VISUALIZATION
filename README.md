# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY: CODETECH IT SOLUTIONS

NAME: PRATEEK RATHOUR

INTERN ID: CT06DL752

DOMAIN: PYTHON DEVELOPEMENT

DURATION: 6 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION-

Work Progress Report: Weather Data Visualization Project
1 Project Overview
The Weather Data Visualization Project aims to develop a Python script that integrates
with a free public API to fetch weather data and generate visualizations. The chosen API,
Open-Meteo, provides global weather forecasts without requiring an API key, making it
suitable for non-commercial use. The script processes hourly forecast data for a specified
location (London) and produces individual visualizations using Matplotlib and Seaborn,
avoiding a dashboard-style layout as per requirements.
2 Objectives
The primary objectives are:
• Develop a Python script to fetch 5-day hourly weather forecast data from Open-
Meteo.
• Process data into a structured format for analysis.
• Generate three distinct visualizations: a temperature trend, weather condition frequencies,
and temperature vs. humidity correlation.
• Produce a text summary of current weather conditions.
• Ensure visualizations are saved as separate PNG files.
3 Progress
The project has achieved significant milestones:
• API Integration: Successfully implemented a function to query Open-Meteo’s forecast
endpoint, retrieving hourly data for temperature, humidity, precipitation probability,
and weather codes for London (latitude: 51.5074, longitude: -0.1278).
• Data Processing: Converted raw JSON data into a Pandas DataFrame, mapping
weather codes to descriptive labels (e.g., Clear, Light Rain) for analysis.
• Visualization Development: Created three visualizations using Matplotlib and Seaborn:
– Line plot of temperature over time, showing 5-day trends.
– Bar plot of weather condition frequencies.
– Scatter plot of temperature vs. humidity, with precipitation probability as
point sizes and weather types as hues.
• Output Generation: Saved visualizations as individual PNG files (temperaturef orecast.png, weatherconditions.4 Deliverables
The following deliverables have been completed:

• Python script (openmeteoweathervisualizations.py)integratingOpen−MeteoAP Iandgeneratingvisualizations.• Text file summarizing current weather conditions.
5 Challenges
• Weather Code Mapping: Open-Meteo’s weather codes required manual mapping
to human-readable descriptions, as the API provides numeric codes. A simplified
mapping was implemented, but some less common codes were grouped as “Other”.
• Data Volume: Hourly data for 5 days generated large datasets, requiring efficient
Pandas operations to avoid performance issues.
6 Next Steps
Future tasks include:
• Enhance the script to support multiple locations by accepting user input for coordinates.
• Add more visualizations, such as wind speed trends or precipitation probability
heatmaps.
• Improve weather code mapping to cover all possible codes provided by Open-Meteo.
• Optimize data processing for larger datasets or longer forecast periods.
7 Timeline
• Completed (by May 12, 2025): API integration, data processing, visualization generation,
and deliverable production.
• Planned (by May 19, 2025): Implement multi-location support and additional visualizations.
• Planned (by May 26, 2025): Finalize weather code mapping and performance optimizations.

OUTPUTS

![Image](https://github.com/user-attachments/assets/a07a2528-21ed-4759-854d-0247f3fda4d1)
![Image](https://github.com/user-attachments/assets/f3a21750-c18c-4045-81c8-d7bd79d8f369)
![Image](https://github.com/user-attachments/assets/40dd0d26-b9c4-4912-b30f-463be8fcc233)
![Image](https://github.com/user-attachments/assets/a60c90b4-c3f9-4294-b71f-0d8b44dc18a2)
![Image](https://github.com/user-attachments/assets/c45756d7-d502-42f0-ba36-c0d97d9ce56a)
