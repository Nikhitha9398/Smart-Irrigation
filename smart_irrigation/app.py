import streamlit as st
import numpy as np
import joblib  

# Add background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.pinimg.com/736x/80/df/9b/80df9b09537eb1452ec5c84423aee161.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

model = joblib.load("Farm_Irrigation_System.pkl")  

st.title("Smart Sprinkler System")
st.subheader("Enter scaled sensor values (0 to 1) to predict sprinkler status")

sensor_values = []
for i in range(20):
    val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    sensor_values.append(val)

if st.button("Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("### Prediction:")
    for i, status in enumerate(prediction):
        st.write(f"Sprinkler {i} (parcel_{i}): {'ON' if status == 1 else 'OFF'}")
