# In coder
# Run with `c
# Check your port (usually 8501). 
# Use the "PORTS" tab in VScode to forward the port to localhost and view it your local browser
# OR use preview browser in VScode

import streamlit as st

import pandas as pd
from autogluon.tabular import TabularPredictor
import os

# Dont use GPUS (they are usauall)
os.environ['CUDA_VISIBLE_DEVICES'] = ''

model_path = f"/home/sunil/am2/MLinMS/Hacathon_ML_model/AutogluonModels/ag-20240729_084336"
predictor = TabularPredictor.load(model_path)

def main():
    st.title("Spider Web Integrity Predictor")
    st.write('Your inputs')
    # Create an inputs or sliders; up to you
    m = st.text_input('m', key='m')
    v = st.text_input('v', key='v')
    r = st.selectbox(
    "What's the radius of the fly or dust?",
    ("1.0", "2.0"))
    st.write("You selected:", r)
    t = st.selectbox(
    "What's the timestep?",
    ("0.000000016", "0.000000008"))
    st.write("You selected:", t)
 
    # Create a button to trigger model inference
    if st.button("Predict"):
        st.subheader('This is the prediction')
        # Perform inference using the loaded model
        
        df = pd.DataFrame([[m, v, r, t]], columns=['Mass_Dust_Particle_in_gram', 'Velocity_in__(m/sec)', 'Radius_of_Dust__Sphere_(mm)', 'Timestep'])
        df
        result = predictor.predict(df)
        result


if __name__ == '__main__':
    main()
