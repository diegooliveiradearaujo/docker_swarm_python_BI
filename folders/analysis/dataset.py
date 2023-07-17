import pandas as pd
import streamlit as st

def start_dataset():

    #dataset
    st.title("Dataset")
    df = pd.read_csv("folders/dataset/diabetes.csv")
    st.dataframe(df)
    rows = df.shape[0]
    columns = df.shape[1]
        
    st.write("There are %d rows and %d columns in the dataset."%(rows,columns))

    #context
    st.header("Context")
    st.write("This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective is to predict based on diagnostic measurements whether a patient has diabetes.")
    
    #content
    st.header("Content")
    st.write("Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.")
    st.write("- Pregnancies: Number of times pregnant;")
    st.write("- Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test;")
    st.write("- BloodPressure: Diastolic blood pressure (mm Hg);")
    st.write("- SkinThickness: Triceps skin fold thickness (mm);")
    st.write("- Insulin: 2-Hour serum insulin (mu U/ml);")
    st.write("- BMI: Body mass index (weight in kg/(height in m)^2);")
    st.write("- DiabetesPedigreeFunction: Diabetes pedigree function;")
    st.write("- Age: Age (years);")
    st.write("- Outcome: Class variable (0 or 1);")

    st.write("Observation:")
    st.write("Class Distribution: (class value 1 is interpreted as tested positive for diabetes, and 0 as tested negative)")




