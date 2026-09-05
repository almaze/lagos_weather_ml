# Lagos Weather ML

A machine learning project for analyzing historical weather patterns in Lagos, Nigeria, and developing precipitation forecasting models.

The project investigates how **temporal aggregation and feature engineering affect precipitation forecasting performance**. It progresses from an initial daily forecasting model to a monthly forecasting model, with the second formulation producing a substantial improvement in predictive performance.

The project also demonstrates how environmental observations can be transformed into structured predictive signals that could support environmental and climate-risk intelligence.

---

## Project Objective

The primary objective is to investigate whether historical weather conditions can provide useful predictive signals for precipitation in Lagos.

The project focuses on:

* Historical weather analysis
* Feature engineering
* Daily versus monthly temporal resolution
* Precipitation forecasting
* Machine learning regression
* Model evaluation using MAE, RMSE and R²
* Understanding how changes in feature design affect predictive performance
* Translating environmental observations into potentially useful intelligence signals

---

# Dataset

Historical weather data for Lagos was obtained from the **Open-Meteo Historical Weather API**.

The dataset contains atmospheric and precipitation variables including:

* Temperature
* Relative humidity
* Dew point
* Surface pressure
* Wind speed
* Precipitation

The data was validated and transformed before being used for machine learning.

---

# Modeling Approach

The project developed through two principal modeling stages.

The purpose of the progression was not simply to try different algorithms, but to investigate whether a better formulation of the environmental data could produce a more useful precipitation signal.

---

## Model 1 — Daily Precipitation Forecasting

### Data formulation

The first model worked with **daily weather observations**.

The experiment used approximately **10 years of historical data** and six weather variables as predictors.

The six input variables represented the main atmospheric conditions available in the dataset:

* Temperature
* Relative humidity
* Dew point
* Surface pressure
* Wind speed
* Precipitation

The model attempted to predict precipitation at the daily level.

### Model

Random Forest model was used to estimate precipitation from the daily weather variables.

### Result

The initial model achieved:

**R² ≈ 0.07**

This indicated relatively weak predictive performance.

The predictions were able to capture some broad movements in precipitation, but the model struggled with the magnitude of larger rainfall events. In particular, high observed precipitation values were frequently underestimated.

### Interpretation

The result suggested that the daily formulation was not capturing enough of the underlying precipitation structure.

Daily precipitation can be highly variable, and individual observations may contain substantial short-term noise. This raised an important modeling question:

> Would aggregating the weather observations over a longer temporal period produce a more stable and useful predictive signal?

This led to the development of Model 2.

---

# Model 2 — Monthly Precipitation Forecasting

Model 2 changed the formulation of the problem in two important ways:

1. The temporal resolution was changed from **daily to monthly**.
2. The weather variables were expanded into **maximum, mean and minimum statistics**.

The historical period was also extended to **20 years (2006–2025)**.

---

## Monthly Feature Engineering

Instead of using individual daily observations, the weather data was aggregated to the monthly level.

For the selected weather variables, three statistics were generated:

* Maximum
* Mean
* Minimum

This produced **15 weather-related input variables**.

### Temperature

* `temperature_2m_max`
* `temperature_2m_mean`
* `temperature_2m_min`

### Dew Point

* `dew_point_2m_max`
* `dew_point_2m_mean`
* `dew_point_2m_min`

### Relative Humidity

* `relative_humidity_2m_max`
* `relative_humidity_2m_mean`
* `relative_humidity_2m_min`

### Surface Pressure

* `surface_pressure_max`
* `surface_pressure_mean`
* `surface_pressure_min`

### Wind Speed

* `wind_speed_10m_max`
* `wind_speed_10m_mean`
* `wind_speed_10m_min`

In addition to these 15 atmospheric features, **monthly precipitation** was included as a predictor.

Therefore, Model 2 used **16 input variables in total**.

---

## Target Variable

The forecasting target was the precipitation of the following month:

```text
next_month_precipitation
```

The target was created by shifting monthly precipitation forward by one month.

Conceptually:

```text
Current month weather + precipitation
                  ↓
        Next month's precipitation
```

For example:

```text
January conditions → February precipitation
February conditions → March precipitation
March conditions → April precipitation
```

This converts the problem from describing current precipitation to forecasting precipitation in the following month.

---

## Model

A **Random Forest Regressor** was used for Model 2.

Random Forest was selected because it can capture nonlinear relationships and interactions between weather variables without requiring the relationship between the predictors and precipitation to be linear.

---

## Train/Test Strategy

Because precipitation forecasting is a time-dependent problem, the data was divided chronologically rather than randomly.

The model was trained on earlier observations and evaluated on later observations.

This avoids using future observations to train a model that is subsequently evaluated on the past.

---

# Model 1 → Model 2: Performance Improvement

The most significant result of the project was the improvement obtained after reformulating the forecasting problem.

| Model   | Historical period | Temporal resolution |                      Weather inputs |        R² |
| ------- | ----------------- | ------------------- | ----------------------------------: | --------: |
| Model 1 | ~10 years         | Daily               |                                   6 | **~0.07** |
| Model 2 | 2006–2025         | Monthly             | 15 weather features + precipitation | **~0.48** |

The R² improvement was approximately:

**0.07 → 0.48**

or approximately **+0.41 R² points**.

---

## Why Model 2 Performed Better

The improvement should not be attributed simply to the Random Forest algorithm.

The more important change was the **reformulation of the data and forecasting problem**.

Model 1 relied on individual daily observations and six relatively broad input variables. The daily formulation exposed the model to substantial short-term variability.

Model 2 instead:

1. Aggregated observations from daily to monthly resolution.
2. Captured the range of atmospheric conditions using maximum, mean and minimum values.
3. Increased the number of weather-derived predictors from 6 to 15.
4. Incorporated monthly precipitation as an additional predictor.
5. Used a longer historical period of 20 years.
6. Forecast the following month's precipitation using a chronological modeling framework.

The resulting model achieved an R² of approximately **0.48**, substantially higher than the approximately **0.07** achieved by the initial daily formulation.

This demonstrates an important machine-learning principle:

> **Model performance depends not only on the choice of algorithm, but also on how the prediction problem is formulated and how the underlying data is represented.**

---

# Model Evaluation

The models are evaluated using three standard regression metrics.

### Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted and observed precipitation.

Lower MAE indicates smaller average prediction errors.

### Root Mean Squared Error (RMSE)

RMSE gives greater weight to larger errors than MAE.

This is particularly relevant to precipitation forecasting because large rainfall events can have disproportionate operational and financial consequences.

### R²

R² measures the proportion of variation in the target that is explained by the model relative to an appropriate baseline.

A higher R² generally indicates better predictive performance, but it should be interpreted alongside MAE and RMSE.

---

# Key Finding

The central finding from the modeling experiments is that **changing the temporal resolution and feature representation substantially improved precipitation forecasting performance**.

The progression was:

```text
Daily observations
        ↓
6 weather inputs
        ↓
R² ≈ 0.07
        ↓
Feature engineering + monthly aggregation
        ↓
15 weather features
+ monthly precipitation
        ↓
20 years of data
        ↓
Random Forest
        ↓
R² ≈ 0.48
```

The result suggests that monthly aggregation provided a more stable representation of precipitation behavior for this forecasting task.

However, an R² of 0.48 also indicates that a substantial proportion of precipitation variability remains unexplained. The model should therefore be regarded as a predictive signal rather than a complete representation of the physical processes governing rainfall.

---

# Environmental Intelligence Application

The project illustrates a broader environmental intelligence workflow:

```text
Environmental observations
          ↓
Data validation
          ↓
Feature engineering
          ↓
Temporal aggregation
          ↓
Machine learning
          ↓
Forecast
          ↓
Risk / decision signal
```

A similar workflow could be applied to environmental variables to develop signals for:

* Agricultural risk
* Insurance risk
* Flood and infrastructure risk
* Water-resource planning
* Energy operations
* Climate-risk assessment
* Environmental monitoring

The objective is to move from simply collecting environmental data to transforming that data into **forward-looking intelligence that can support decisions**.

---

# Data Pipeline

The project follows an ETL-oriented workflow.

### Extract

Historical weather observations are retrieved from the Open-Meteo API.

### Transform

The raw observations are:

* Validated
* Cleaned
* Structured
* Aggregated
* Converted into machine-learning features

### Analyze

The transformed dataset is used for exploratory analysis, feature engineering, model training and evaluation.

---

# Project Structure

```text
lagos_weather_ml/
│
├── data/
│   ├── processed/
│   │   └── lagos_weather_transformed.csv
│   │
│   └── raw/
│       └── lagos_weather_raw.csv
│
├── notebooks/
│   └── weather_ml_analysis.ipynb
│
├── src/
│   ├── confg.py
│   ├── extract.py
│   ├── transform.py
│   └── validation.py
│
├── .gitignore
└── README.md
```

---

# Technology Stack

* **Python** — Data processing and machine learning
* **Pandas** — Data manipulation and feature engineering
* **Scikit-learn** — Machine learning and model evaluation
* **Jupyter Notebook** — Exploratory analysis and experimentation
* **Open-Meteo API** — Historical weather data
* **Git/GitHub** — Version control and project management

---

# Limitations

Several limitations remain.

### Limited geographic scope

The current analysis focuses on Lagos. Relationships between weather variables and precipitation may differ across geographic regions.

### Precipitation variability

Rainfall is influenced by complex atmospheric and geographical processes that cannot necessarily be captured by the available variables alone.

### Predictive performance

Although Model 2 substantially improves on Model 1, an R² of approximately 0.48 means that considerable variability remains unexplained.

### Extreme rainfall events

The model's ability to reproduce extreme precipitation events requires further investigation, particularly because these events can be more important for risk applications than average rainfall conditions.

---

# Future Improvements

Potential next steps include:

* Feature importance analysis
* Hyperparameter optimization
* Evaluation of additional machine-learning algorithms
* Incorporation of additional environmental variables
* Extreme-event detection
* Seasonal forecasting analysis
* Comparison of different historical training windows
* Spatial analysis using multiple locations
* Integration with satellite and geospatial datasets
* Conversion of precipitation forecasts into agricultural, insurance or infrastructure risk indicators

---

# Conclusion

The Lagos Weather ML project demonstrates the progression from a basic daily precipitation forecasting approach to a more structured monthly forecasting model.

The initial daily model achieved an R² of approximately **0.07**. After reformulating the problem around monthly observations, expanding the weather representation from six inputs to 15 max/mean/min weather features, incorporating monthly precipitation, and using a 20-year historical dataset, the Random Forest model achieved an R² of approximately **0.48**.

The key lesson is that useful environmental intelligence depends not only on selecting a machine-learning algorithm, but also on **understanding the temporal structure of the environmental system, engineering meaningful features, and formulating the prediction problem appropriately**.
