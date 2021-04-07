import streamlit as st
import pandas as pd
import json
from sklearn.ensemble import RandomForestClassifier

def loadJSON(filename):
    with open(filename, 'r') as file:
        return json.load(file)

dataset = loadJSON("dataset.json")
data = dataset["data"]
targets = dataset["targets"]

st.write("""
# Prediction App for Pima Indians Diabetes.
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    times_pregnant = st.sidebar.slider('Times pregnant', 0.0, 20.0, 1.0)
    plasma_glucose = st.sidebar.slider('Plasma glucose concentration a 2 hours in an oral glucose tolerance test', 0.0, 500.0, 1.0)
    diastolic_bp = st.sidebar.slider('Diastolic blood pressure (mm Hg)', 0.0, 100.0, 1.0)
    tricep = st.sidebar.slider('Triceps skin fold thickness (mm)', 0.0, 100.0, 1.0)
    serum_insulin = st.sidebar.slider('2-Hour serum insulin (mu U/ml)', 0.001, 250.0, 0.001)
    bmi = st.sidebar.slider('Body mass index (weight in kg/(height in m)^2)', 0.001, 100.0, 0.001)
    dia_pedigree = st.sidebar.slider('Diabetes pedigree function', 0.001, 100.0, 0.001)
    age = st.sidebar.slider('Age (years)', 1.0, 150.0, 1.0)

    data = {'times_pregnant': times_pregnant,
            'plasma_glucose': plasma_glucose,
            'diastolic_bp': diastolic_bp,
            'tricep': tricep,
            "serum_insulin": serum_insulin,
            "bmi": bmi,
            "dia_pedigree": dia_pedigree,
            "age": age}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

X = data
Y = targets

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)