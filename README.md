# Lagos Weather ML

A machine learning project for analyzing historical weather patterns in Lagos, Nigeria, and developing models for precipitation forecasting.

The project progresses from exploratory weather analysis and baseline modeling to monthly precipitation forecasting using machine learning. A key objective is to evaluate whether aggregating weather observations at the monthly level improves the ability to predict precipitation compared with daily-level modeling.

---

## Project Objective

The objective of this project is to investigate whether historical atmospheric conditions can provide useful predictive signals for future precipitation in Lagos.

The project explores:

- Historical weather patterns
- Daily versus monthly aggregation
- Precipitation forecasting
- Feature engineering
- Machine learning model performance
- Model evaluation using MAE, RMSE and R²
- The effect of changing the temporal resolution of the data
- The use of atmospheric variables as predictors of future precipitation

The project is also designed as a practical example of an environmental intelligence pipeline, where raw environmental observations are transformed into structured features and predictive insights.

---

# Project Progression

The project evolved through several modeling stages.

## Model 0 — Baseline / Initial Analysis

The initial stage established the data pipeline and baseline understanding of the Lagos weather dataset.

The raw weather observations were extracted from the Open-Meteo API and prepared for analysis.

The data included variables such as:

- Temperature
- Relative humidity
- Dew point
- Surface pressure
- Wind speed
- Cloud cover
- Precipitation

The data was validated, transformed and prepared for machine learning.

---

## Model 1 — Initial Precipitation Forecast

The first machine learning model attempted to predict precipitation at the daily level.

### Approach

The model used historical weather observations to predict precipitation.

The initial model achieved an R² of approximately:

**R² = 0.07**

This indicated that the model had limited explanatory/predictive power.

Although the predictions captured some general movement in precipitation, the model struggled particularly with larger precipitation events. Predicted peaks were substantially lower than observed peaks.

### Key observation

The daily modeling approach suggested that precipitation contains substantial variability that was difficult for the model to capture using the available predictors.

This motivated an investigation into whether aggregating the data to a monthly temporal resolution would produce a more stable forecasting problem.

---

# Model 2 — Monthly Precipitation Forecasting

The second stage changed the temporal resolution from daily observations to monthly observations.

Instead of attempting to predict individual daily precipitation values, the data was aggregated by month.

### Monthly aggregation

Weather variables were aggregated to produce monthly statistics, while precipitation was treated as a monthly total.

This produced a substantially more stable target variable for forecasting.

### Model

A **Random Forest Regressor** was used for the monthly precipitation forecasting task.

Random Forest was selected because it can model nonlinear relationships between atmospheric variables and precipitation without requiring a linear relationship between the predictors and target.

### Evaluation

The monthly model produced a substantial improvement compared with the initial daily model.

**Initial R²: ~0.07**

**Improved R²: ~0.48**

This represents an improvement of approximately **0.41 R² points**.

The improvement suggests that monthly aggregation provided a more useful representation of the underlying precipitation signal than the initial daily formulation.

### Important finding

The improvement should not be interpreted as meaning that the model suddenly explains 48% of all precipitation behavior.

Rather, it indicates that under the revised monthly formulation and evaluation setup, the model achieved substantially better predictive performance than the initial daily model.

---

# Model 3 — Weather-Only Next-Month Forecast

The third stage investigates a more challenging and operationally useful question:

> Can next month's precipitation be predicted using only the current month's atmospheric conditions?

Unlike a model that uses current precipitation as a predictor, Model 3 deliberately excludes current-month precipitation from the feature set.

## Target

The target variable is:

```text
next_month_precipitation