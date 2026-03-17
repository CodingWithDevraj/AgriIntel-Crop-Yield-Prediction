---

# AgriIntel — AI-Driven Crop Yield Prediction & Farm Decision Support System

AgriIntel is an **end-to-end machine learning system** that predicts **cotton production using environmental and economic indicators** such as rainfall, temperature, and cultivation cost.

The system integrates **multiple agricultural datasets**, performs **data preprocessing and feature engineering**, trains predictive models, and delivers results through an **interactive Streamlit dashboard** for agricultural decision support.

This project demonstrates how **data science and machine learning can support precision agriculture and data-driven farm planning.**

---

# Problem Statement

Agricultural productivity is influenced by several **dynamic environmental and economic factors**, including rainfall patterns, temperature fluctuations, and farming costs.

However, farmers and agricultural planners often lack **predictive tools that combine these factors into actionable insights**.

Without predictive analytics:

• Crop production planning becomes uncertain
• Resource allocation becomes inefficient
• Risk management becomes difficult

This project aims to build a **data-driven crop yield prediction system** that can help estimate agricultural output based on historical data.

---

# Solution Overview

AgriIntel provides a **machine learning–based decision support system** that predicts cotton production by analyzing historical agricultural data.

The solution consists of:

1️⃣ **Data Integration** from multiple agricultural datasets
2️⃣ **Feature Engineering** to capture environmental relationships
3️⃣ **Machine Learning Model Training**
4️⃣ **Prediction Interface via Streamlit Dashboard**

Users can input environmental conditions and receive **real-time predictions of expected crop production**.

---

# System Architecture

```text
      Agricultural Datasets
(Crop Production, Rainfall, Temperature, Cost)
            │
            ▼
Data Cleaning & Preprocessing
    (Pandas, NumPy)
            │
            ▼
     Feature Engineering
(Rain Efficiency, Interaction Features)
            │
            ▼
     Model Training
(Linear Regression, Random Forest)
            │
            ▼
     Model Evaluation
       (R², RMSE)
            │
            ▼
    Prediction System
   (Streamlit Dashboard)
            │
            ▼
  Farm Decision Support
```

This pipeline mirrors a **typical production-style machine learning workflow used in real data science projects.**

---

# Datasets Used

The project integrates multiple datasets to capture agricultural conditions.

### Crop Production Dataset

• State-wise cotton production data
• Area cultivated and yield metrics

### Rainfall Dataset

• Historical rainfall data across regions

### Temperature Dataset

• Daily temperature readings for major Indian cities

### Labor Cost Dataset

• Agricultural cultivation cost statistics

### Cotton Price Dataset

• Historical market price trends for cotton

These datasets were **cleaned, aligned, and merged** to create a unified machine learning dataset.

---

# Data Processing Pipeline

The data pipeline includes several stages:

#1️⃣ Data Cleaning
2️⃣ Feature Engineering
3️⃣ Dataset Integration
4️⃣ Time Alignment Across Datasets
5️⃣ Model Training
6️⃣ Model Evaluation
7️⃣ Dashboard Deployment

This workflow ensures **data quality, model reliability, and usability of predictions**.

---

# Machine Learning Models

Two machine learning algorithms were trained and evaluated.

### Linear Regression

A statistical model that captures relationships between crop production and environmental variables.

### Random Forest Regressor

An ensemble learning method capable of modeling **non-linear relationships and complex feature interactions**.

---

# Model Performance

| Model             | R² Score | RMSE |
| ----------------- | -------- | ---- |
| Linear Regression | **0.91** | 187  |
| Random Forest     | 0.87     | 221  |

The **Linear Regression model achieved the highest predictive accuracy** and was selected for deployment.

---

# Prediction Logic

The prediction system estimates cotton production using the following input features:

• Rainfall
• Average Temperature
• Cultivation Cost
• Rainfall–Temperature Interaction
• Rain Efficiency Index

These features help the model **capture environmental relationships influencing crop productivity**.

---

# Interactive Dashboard

An interactive **Streamlit web application** was built to demonstrate the prediction system.

Users can input environmental conditions and receive **real-time crop production estimates.**

### Dashboard Features

• Clean and intuitive user interface
• Real-time prediction system
• Explanation of methodology and dataset sources
• Technical section describing models and pipeline

The dashboard acts as a **prototype decision support tool for agritech applications**.

---

# Technology Stack

| Category              | Tools               |
| --------------------- | ------------------- |
| Programming Language  | Python              |
| Data Processing       | Pandas, NumPy       |
| Machine Learning      | Scikit-Learn        |
| Visualization         | Matplotlib, Seaborn |
| Application Framework | Streamlit           |
| Version Control       | GitHub              |

---

# Project Structure

```
AgriIntel
│
├── data
│   ├── crop_production.csv
│   ├── rainfall.csv
│   ├── temperature.csv
│   ├── labor.csv
│   └── cotton_price.csv
│
├── notebooks
│   └── main.ipynb
│
├── models
│   │   └── crop_yield_model.pkl
│
├── agriintel_workflow.png
│
├── app.py
├── requirements.txt
└── README.md
```

---

# Running the Project

### Install dependencies

```
pip install -r requirements.txt
```

### Run the Streamlit dashboard

```
streamlit run app.py
```

The application will launch locally in your browser.

---

# Skills Demonstrated

This project highlights key **data science and machine learning competencies**:

• Data Cleaning & Preprocessing
• Feature Engineering
• Multi-dataset Integration
• Machine Learning Model Development
• Model Evaluation & Validation
• Interactive Dashboard Development
• End-to-End ML Pipeline Design

---

# Future Improvements

Potential enhancements for the system include:

• Integration of **satellite-based NDVI vegetation indices**
• Incorporation of **soil quality and soil moisture datasets**
• **Multi-crop prediction models**
• Deployment as a **cloud API for agritech platforms**
• Integration with **real-time weather APIs**

---

# Potential Applications

AgriIntel can support several real-world use cases:

• Precision agriculture platforms
• Agritech analytics systems
• Smart farming advisory tools
• Agricultural robotics planning systems
• Government agricultural policy planning

---

# Author

**Devraj Choudhary**

B.Tech – Computer Science & Engineering
Gurukul Kangri Deemed to be University

Interests

• Data Science
• Machine Learning
• AI for Agriculture

GitHub
[https://github.com/CodingWithDevraj](https://github.com/CodingWithDevraj)

LinkedIn
[https://www.linkedin.com/in/devraj-choudhary-3889412bb/](https://www.linkedin.com/in/devraj-choudhary-3889412bb/)

Working Dashboard
[https://agriintel-crop-yield-prediction-ccthxnwd3hszspmwpx3wtp.streamlit.app/](https://agriintel-crop-yield-prediction-ccthxnwd3hszspmwpx3wtp.streamlit.app/)

---

