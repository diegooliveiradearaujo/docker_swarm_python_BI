import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
import folders.prediction.naive_bayes as naive_bayes
import folders.prediction.decision_tree as decision_tree


def start_prediction():
  st.title("Prediction")
  df = pd.read_csv("folders/dataset/diabetes.csv")
  
  #separating data
  dataset_drop_outcome = df.drop(['Outcome'],axis=1)
  outcome = df['Outcome']

  #train and test
  x_train, x_test, y_train, y_test = train_test_split(dataset_drop_outcome, outcome, test_size=0.2, random_state=1)

  #user_input
  def get_user_data():
    user_pregnancies = st.sidebar.slider("Pregnancies",0, 15, 1)
    user_glucose = st.sidebar.slider("Glucose", 0, 200, 110)
    user_blood_pressure = st.sidebar.slider("Blood pressure", 0, 122, 72)
    user_skin_thickness = st.sidebar.slider("Skin thickness", 0, 99, 20)
    user_insulin = st.sidebar.slider("Insulin", 0, 900, 30)
    user_bmi= st.sidebar.slider("BMI", 0.0, 70.0, 15.0)
    user_dpf = st.sidebar.slider("Diabetes Pedigree Function", 0.0, 3.0, 0.0)
    user_age = st.sidebar.slider ("Age", 15, 100, 21)

    #output for the dictionary
    user_data = { 'Pregnancies': user_pregnancies,
                  'Glucose': user_glucose,
                  'BloodPressure': user_blood_pressure,
                  'SkinThickness': user_skin_thickness,
                  'Insulin': user_insulin,
                  'BMI': user_bmi,
                  'DiabetesPedigreeFunction': user_dpf,
                  'Age': user_age}

    #new dataframe through the dictionary
    features = pd.DataFrame(user_data, index=[0])
    return features

  user_input_variables = get_user_data()

  options = st.sidebar.radio('Which model do you prefer to predict?',('Naive Bayes', 'Decision Tree'))
  if options == 'Naive Bayes':
    naive_bayes.start_naive_bayes(dataset_drop_outcome, outcome,  x_train, y_train, x_test, y_test, user_input_variables)
  if options == 'Decision Tree':
    decision_tree.start_decision_tree(dataset_drop_outcome, outcome,  x_train, y_train, x_test, y_test, user_input_variables)