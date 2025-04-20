import streamlit as st
from PIL import Image
import pickle
import numpy as np
import pandas as pd

# Page config
st.set_page_config(page_title="Laptop Price Prediction", layout="wide")

@st.cache_resource
def load_model():
    return pickle.load(open('xgboost.pkl', 'rb'))

df1 = load_model()

# Extract categories
company_name = df1.named_steps['columntransformer'].named_transformers_['onehotencoder'].categories_[0]
laptop_type = df1.named_steps['columntransformer'].named_transformers_['onehotencoder'].categories_[1]
laptop_processor = df1.named_steps['columntransformer'].named_transformers_['onehotencoder'].categories_[2]
laptop_card = df1.named_steps['columntransformer'].named_transformers_['onehotencoder'].categories_[3]
laptop_os = df1.named_steps['columntransformer'].named_transformers_['onehotencoder'].categories_[4]
laptop_cardcompany = df1.named_steps['columntransformer'].named_transformers_['onehotencoder'].categories_[5]

# Map GPU brand → model
gpu_mapping = {}
for gpu in laptop_card:
    for brand in laptop_cardcompany:
        if brand.lower() in gpu.lower():
            gpu_mapping.setdefault(brand, []).append(gpu)
            break

# --- Header ---
col1, col2 = st.columns([1, 4])
with col1:
    st.image("download.jpeg", width=100)
with col2:
    st.title("Laptop Price Prediction")

# --- Inputs ---
st.subheader("Enter Laptop Specifications")

col1, col2 = st.columns(2)

with col1:
    company = st.selectbox("Company", company_name)
    type_laptop = st.selectbox("Laptop Type", laptop_type)
    inch = st.number_input("Screen Size (Inches)", min_value=10.0, max_value=20.0, step=0.1)
    cpu_laptop = st.selectbox("CPU", laptop_processor)
    ram_laptop = st.selectbox("RAM (GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64])
    gpubrand_laptop = st.selectbox("GPU Brand", laptop_cardcompany)
    gpu_options = gpu_mapping.get(gpubrand_laptop, [])
    gpu_laptop = st.selectbox("GPU Model", gpu_options)

with col2:
    opsys_laptop = st.selectbox("Operating System", laptop_os)
    weight_laptop = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, step=0.1)
    touch_laptop = st.selectbox("Touchscreen", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    res_laptop = st.text_input("Screen Resolution (e.g., 1920x1080)", value="1920x1080")
    ips_laptop = st.selectbox("IPS Panel", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    hdd_laptop = st.number_input("HDD (GB)", min_value=0, max_value=2000, step=500, value=0)
    ssd_laptop = st.number_input("SSD (GB)", min_value=0, max_value=2000, step=500, value=0)

# --- Predict Button ---
# --- Predict Button ---
if st.button("Predict Price", key="predict_btn"):
    try:
        x_res, y_res = map(int, res_laptop.lower().split('x'))
        input_data = [[company, type_laptop, float(inch), cpu_laptop, int(ram_laptop),
                       gpu_laptop, opsys_laptop, float(weight_laptop), touch_laptop,
                       x_res, y_res, ips_laptop, int(hdd_laptop), int(ssd_laptop), gpubrand_laptop]]

        prediction = df1.predict(pd.DataFrame(input_data, columns=[
            'Company', 'TypeName', 'Inches', 'Cpu', 'Ram', 'Gpu', 'OpSys',
            'Weight', 'touchscreen', 'y_res', 'x_res', 'IPS', 'HDD', 'SSD', 'Gpu_Brand'
        ]))

        predicted_price = np.exp(prediction[0])
        st.success(f"💰 Predicted Laptop Price: ₹{predicted_price:,.2f}")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# --- Custom Styling for Smaller Button ---
st.markdown("""
<style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 6px 12px;  /* Smaller padding */
        border: none;
        border-radius: 4px;
        font-size: 14px;     /* Smaller font */
        width: 150px;        /* Optional: smaller width */
        margin-top: 10px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)
