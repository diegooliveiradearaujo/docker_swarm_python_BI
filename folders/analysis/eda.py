import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


def start_eda():
    st.title("Exploratory Data Analysis")
    st.header("Histograms")
    df = pd.read_csv("folders/dataset/diabetes.csv")
    
    #HISTOGRAMS
    #2 columns - Pregnancies and Age
    col1, col2 = st.columns(2)
    with col1:
        fig = px.histogram(df, x="Pregnancies", nbins=50, title='PREGNANCIES', labels={"Pregnancies": 'Pregnancies'},width=400, height=400)
        st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

    with col2:
        fig = px.histogram(df, x="Age", color='Age', nbins=50, title='AGE', labels={"Age": 'Age'},width=400, height=400)
        st.plotly_chart(fig, use_container_width=False, sharing='streamlit')
    
    #2 columns - BMI and Outcome
    col3, col4 = st.columns(2)
    with col3:
        fig = px.histogram(df, x="BMI", nbins=50, title='BMI', labels={"BMI": 'BMI'},width=400, height=400)
        st.plotly_chart(fig, use_container_width=False, sharing='streamlit')
    with col4:
        fig = px.histogram(df, x="Outcome", color='Outcome', nbins=50, title='OUTCOME', labels={"Outcome": 'Outcome'},width=400, height=400)
        st.plotly_chart(fig, use_container_width=False, sharing='streamlit')
    
    #ORRELATION
    st.header("Correlation")
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(df.corr(), annot=True, cmap='Blues')
    #ax.set_title('Correlation')
    fig.tight_layout()
    st.pyplot(fig)