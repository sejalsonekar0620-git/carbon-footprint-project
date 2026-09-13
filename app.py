
import streamlit as st
import pandas as pd
import joblib

st.title("Carbon Footprint Prediction & Sustainability Dashboard")

model = joblib.load('models/best_model.pkl')
train_columns = joblib.load('models/train_columns.pkl')

st.header("Enter your lifestyle details")

body_type = st.selectbox("Body Type", ["normal", "overweight", "obese", "underweight"])
sex = st.selectbox("Sex", ["male", "female"])
diet = st.selectbox("Diet", ["omnivore", "vegetarian", "vegan", "pescatarian"])
shower = st.selectbox("How Often Shower", ["daily", "twice a day", "more frequently", "less frequently"])
heating = st.selectbox("Heating Energy Source", ["coal", "natural gas", "wood", "electricity"])
transport = st.selectbox("Transport", ["private", "public", "walk/bicycle"])
vehicle_type = st.selectbox("Vehicle Type", ["None", "petrol", "diesel", "hybrid", "electric", "lpg"])
social = st.selectbox("Social Activity", ["never", "sometimes", "often"])
grocery_bill = st.slider("Monthly Grocery Bill", 50, 500, 200)
air_travel = st.selectbox("Frequency of Traveling by Air", ["never", "rarely", "frequently", "very frequently"])
vehicle_distance = st.slider("Vehicle Monthly Distance (Km)", 0, 5000, 500)
waste_size = st.selectbox("Waste Bag Size", ["small", "medium", "large", "extra large"])
waste_count = st.slider("Waste Bag Weekly Count", 0, 10, 3)
tv_hours = st.slider("How Long TV/PC Daily (Hours)", 0, 24, 5)
new_clothes = st.slider("How Many New Clothes Monthly", 0, 50, 10)
internet_hours = st.slider("How Long Internet Daily (Hours)", 0, 24, 4)
energy_eff = st.selectbox("Energy Efficiency", ["Yes", "No", "Sometimes"])

if st.button("Predict my carbon footprint"):
    input_dict = {
        'Body Type': body_type,
        'Sex': sex,
        'Diet': diet,
        'How Often Shower': shower,
        'Heating Energy Source': heating,
        'Transport': transport,
        'Vehicle Type': vehicle_type,
        'Social Activity': social,
        'Monthly Grocery Bill': grocery_bill,
        'Frequency of Traveling by Air': air_travel,
        'Vehicle Monthly Distance Km': vehicle_distance,
        'Waste Bag Size': waste_size,
        'Waste Bag Weekly Count': waste_count,
        'How Long TV PC Daily Hour': tv_hours,
        'How Many New Clothes Monthly': new_clothes,
        'How Long Internet Daily Hour': internet_hours,
        'Energy efficiency': energy_eff,
    }

    input_df = pd.DataFrame([input_dict])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=train_columns, fill_value=0)

    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Carbon Emission: {prediction:.2f} kg CO2")

    st.subheader("Recommendations")
    if transport == 'private':
        st.write("- Switching to public transport or carpooling could meaningfully reduce your footprint.")
    if diet == 'omnivore':
        st.write("- Reducing meat consumption a few days a week can lower your emissions.")
    if energy_eff == 'No':
        st.write("- Switching to energy-efficient appliances could reduce your energy-related emissions.")
    if vehicle_distance > 1000:
        st.write("- High vehicle usage detected — consider combining trips or public transport.")