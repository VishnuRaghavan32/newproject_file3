import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns 

st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Titanic_1912_Survivors")

titan=pd.read_csv('titanic.csv')
sum = titan.head(15)
st.table(sum)
st.header("Visualisation of the Greatest Tragedy of 1912 Using Seaborn")

st.subheader("JointPlot")
sns.jointplot(x='Pclass',y='Fare',data=titan,kind='scatter')
st.pyplot()

st.subheader("Pairplot")
sns.pairplot(titan,hue='Fare',palette='rainbow')
st.pyplot()

gender=titan.groupby('Sex')
st.subheader("Displot")
sns.displot(tips['gender'])
st.pyplot()

st.subheader("Catplot")
sns.catplot(x='Sex',y='Survived',data=titan,kind='bar')
st.pyplot()