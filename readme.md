🌾 AgriIntel: AI-Driven Crop Yield Prediction & Farm Decision Support System

AgriIntel is a machine learning–based agricultural analytics system that predicts cotton production using environmental and economic conditions.
The system integrates multiple agricultural datasets and provides an interactive dashboard that enables users to estimate crop production under different farming conditions.

This project demonstrates how data science and machine learning can support precision agriculture and data-driven farm planning.

🚀 Project Overview

Agriculture is highly dependent on climatic and economic factors. Farmers and agritech companies often need predictive insights to estimate crop production and plan resources effectively.

AgriIntel analyzes historical agricultural data including rainfall patterns, temperature variations, labor costs, and crop production data to build a predictive model capable of estimating cotton production.

The final system includes a machine learning model and an interactive dashboard where users can input farm conditions and receive predicted crop production estimates.

🎯 Project Objectives

• Analyze agricultural datasets to understand factors affecting cotton production
• Build a machine learning model to predict crop production
• Develop a decision support system for agricultural planning
• Demonstrate how AI can support agritech platforms and smart farming solutions

📊 Datasets Used

The project integrates multiple agricultural datasets:

Crop Production Dataset

State-wise cotton production data

Cotton area and yield information

Rainfall Dataset

Historical rainfall patterns across regions

Temperature Dataset

Daily temperature data for major Indian cities

Labor Cost Dataset

Agricultural cultivation cost data

Cotton Price Dataset

Market price trends for cotton

These datasets were cleaned, processed, and merged to create a unified dataset for machine learning.

⚙️ Data Processing Pipeline

The data pipeline for the project includes the following stages:

1️⃣ Data Cleaning
2️⃣ Feature Engineering
3️⃣ Dataset Integration
4️⃣ Time Alignment of Datasets
5️⃣ Model Training and Evaluation
6️⃣ Deployment via Streamlit Dashboard

🧠 Machine Learning Models

Two models were trained and evaluated:

• Linear Regression
• Random Forest Regressor

These models learn relationships between environmental factors and cotton production.

📈 Model Performance
Model	                  -        R² Score	     |      RMSE
Linear Regression	      -        0.91	         |      187
Random Forest	          -        0.87	         |      221

The Linear Regression model achieved the best performance and was used for the final prediction system.

🤖 Prediction Logic

The model predicts cotton production based on the following inputs:

• Rainfall
• Average Temperature
• Cultivation Cost
• Rainfall–Temperature Interaction
• Rain Efficiency

The predicted value represents estimated regional cotton production under similar environmental conditions based on historical agricultural data.

🖥 Interactive Dashboard

An interactive dashboard was built using Streamlit to demonstrate the prediction system.

Users can enter environmental conditions such as rainfall, temperature, and cultivation cost to estimate cotton production.

Dashboard Features

• Clean and user-friendly interface
• Real-time prediction system
• Project explanation and methodology section
• Advanced section showcasing technologies and models used

🛠 Technologies Used

• Python
• Pandas
• NumPy
• Scikit-Learn
• Streamlit
• Matplotlib / Seaborn

🧩 Skills Demonstrated

This project demonstrates several important data science skills:

• Data Cleaning and Preprocessing
• Feature Engineering
• Dataset Integration
• Machine Learning Model Development
• Model Evaluation
• Data Visualization
• Interactive Dashboard Development

📂 Project Structure

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
│   └── data_analysis.ipynb
│
├── models
│   └── crop_yield_model.pkl
│
├── app.py
├── requirements.txt
└── README.md

Running the Dashboard

Install dependencies:
pip install -r requirements.txt

Run the Streamlit application:
streamlit run app.py

🌱 Future Improvements

Future enhancements for this system include:

• Integration of satellite-based NDVI vegetation data
• Soil quality and soil moisture datasets
• Multi-crop prediction capabilities
• Deployment as a cloud-based API for agritech platforms

💡 Potential Applications

This system can support:

• Precision agriculture systems
• Agritech analytics platforms
• Smart farming decision support tools
• Agricultural robotics planning systems

👨‍💻 Author

Devraj Choudhary
B.Tech Student – Gurukul Kangri University
AI / Machine Learning Enthusiast

GitHub: https://github.com/CodingWithDevraj

LinkedIn: https://www.linkedin.com/in/devraj-choudhary-3889412bb/