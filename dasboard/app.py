import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("./models/crop_yield_model.pkl")

st.set_page_config(
    page_title="AgriIntel Dashboard",
    layout="wide"
)

# -------------------------
# Custom Styling
# -------------------------

st.markdown("""
<style>
/* Modern Font & Deep Dark Background */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

/* Force dark background on the app container */
.stApp {
    background-color: #0b0e0f;
}

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
    color: #e0e0e0;
}

/* Main Title - Glow Effect */
.main-title {
    font-size: 72px;
    font-weight: 800;
    background: linear-gradient(to right, #00ff88, #00bdff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 0px;
    letter-spacing: -2px;
    filter: drop-shadow(0px 4px 10px rgba(0, 255, 136, 0.2));
}

.sub-title {
    font-size: 24px;
    color: #94a3b8;
    text-align: center;
    margin-bottom: 50px;
    font-weight: 300;
    letter-spacing: 1px;
}

/* Section Headers - Modern Border-left style */
.section-header {
    font-size: 38px;
    font-weight: 700;
    color: #00ff88;
    margin-top: 60px;
    margin-bottom: 25px;
    padding-left: 15px;
    border-left: 5px solid #00ff88;
}

/* Sub-headings (h3) */
h3 {
    font-size: 28px !important;
    color: #00bdff !important;
    font-weight: 600 !important;
    margin-top: 30px !important;
}

/* Refined Text for Dark Mode */
p, li {
    font-size: 21px !important;
    color: #cbd5e1 !important;
    line-height: 1.8;
}

/* Glassmorphism Result Box */
.result-box {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    padding: 40px;
    border-radius: 24px;
    font-size: 32px;
    color: #ffffff;
    font-weight: 700;
    text-align: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.5);
    border: 1px solid rgba(0, 255, 136, 0.3);
    margin: 30px 0;
}

/* High-Contrast Buttons */
.stButton>button {
    background: linear-gradient(90deg, #00ff88 0%, #00bdff 100%) !important;
    color: #081c15 !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    border-radius: 14px !important;
    padding: 18px 40px !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(0, 255, 136, 0.3) !important;
    transition: 0.4s ease;
}

.stButton>button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0, 255, 136, 0.5) !important;
    filter: brightness(1.1);
}

/* Input Fields - Dark Themed */
div[data-baseweb="input"], div[data-baseweb="base-input"] {
    background-color: #1a1f21 !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
    color: white !important;
}

/* Labels for inputs */
label {
    font-size: 20px !important;
    color: #00ff88 !important;
    font-weight: 600 !important;
}

/* Horizontal Rule Color */
hr {
    border: 0;
    height: 1px;
    background: #334155;
    margin: 40px 0;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------

st.markdown('<p class="main-title">🌾 AgriIntel</p>', unsafe_allow_html=True)

st.markdown(
'<p class="sub-title">AI-Driven Crop Yield Prediction & Farm Decision Support System</p>',
unsafe_allow_html=True
)

st.markdown("---")

# -------------------------
# About Project
# -------------------------

st.markdown('<p class="section-header">About the Project</p>', unsafe_allow_html=True)

st.write("""
AgriIntel is an AI-powered agricultural analytics platform designed to estimate cotton
production using machine learning.

The system analyzes environmental and economic conditions to forecast crop output and
support data-driven agricultural planning.

The model was trained on multiple agricultural datasets including crop production,
rainfall patterns, temperature data, labor cost data, and market price trends.
""")

st.write("""
### How Prediction Works

The model learns patterns between:

• Rainfall levels  
• Temperature conditions  
• Cultivation cost  
• Climate interaction features  

When a user inputs farm conditions, the system estimates expected cotton production
based on historical agricultural patterns.
""")

st.write("""
### Data Sources Used

• Crop Production Dataset  
• Rainfall Dataset  
• Temperature Dataset  
• Agricultural Labor Cost Dataset  
• Cotton Market Price Dataset
""")

st.write("""
### Benefits

• Helps farmers estimate expected crop production  
• Supports agritech platforms with predictive insights  
• Demonstrates AI-driven decision systems for agriculture
""")

st.markdown("---")

# -------------------------
# Prediction Section
# -------------------------

st.markdown('<p class="section-header"> Crop Production Prediction</p>', unsafe_allow_html=True)

st.write("Enter farm environmental conditions below to estimate cotton production.")

# Vertical Inputs

rainfall = st.number_input("🌧 Rainfall (mm)", min_value=0.0)
temperature = st.number_input("🌡 Average Temperature (°C)", min_value=0.0)
cost = st.number_input("💰 Cultivation Cost", min_value=0.0)

if st.button("Predict Production"):

    rain_temp_interaction = rainfall * temperature
    rain_efficiency = rainfall / (temperature + 1)

    features = np.array([[rainfall, temperature, cost,
                          rain_temp_interaction, rain_efficiency]])

    prediction = model.predict(features)[0]

    st.markdown(
        f'<div class="result-box">🌾 Predicted Cotton Production: <b>{prediction:.2f} thousand tons in this region</b></div>',
        unsafe_allow_html=True
    )

    st.write("### Interpretation")

    st.write(f"""
    Under the given environmental conditions:

    • Rainfall: **{rainfall} mm**  
    • Temperature: **{temperature} °C**  
    • Cultivation Cost: **{cost}**

    The model estimates cotton production around **{prediction:.2f} thousand tons in this region**.

    This estimate is derived from historical agricultural production patterns learned
    by the machine learning model.
    """)

st.markdown("---")

# -------------------------
# Advanced Section
# -------------------------

st.markdown('<p class="section-header">⚙️ Advanced Project Details</p>', unsafe_allow_html=True)

st.write("### Technologies Used")

st.write("""
• Python  
• Pandas  
• NumPy  
• Scikit-Learn  
• Streamlit
""")

st.write("### Machine Learning Models")

st.write("""
Two machine learning models were trained and evaluated:

• Linear Regression  
• Random Forest Regressor
""")

st.write("### Model Performance")

st.write("""
Linear Regression  
R² Score ≈ **0.91**

Random Forest  
R² Score ≈ **0.87**
""")

st.write("### Skills Demonstrated")

st.write("""
• Data Cleaning & Preprocessing  
• Feature Engineering  
• Machine Learning Model Development  
• Model Evaluation  
• Interactive Dashboard Development  
• Agricultural Data Analytics
""")

st.write("### Future Enhancements")

st.write("""
• Integrate satellite vegetation index data (NDVI)  
• Include soil quality datasets  
• Expand to multi-crop prediction  
• Deploy API for agritech platforms
""")

st.markdown("---")

st.write("Developed by **Devraj Choudhary** | AI for Agriculture")