import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Read the data
# deaths = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")

df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')


# Get the countries list
clist = df['Country/Region'].unique()

# Create the streamlit sidebar
country = st.sidebar.selectbox("Select a country:",clist)

# The header of the figure
st.header("GDP per Capita over time")


# Create a figure
df_usa_new_cases = df[['Country/Region', '3/31/22']].reset_index()

# use the plot function
fig = plt.figure(figsize=(15,5))
plt.plot(df_usa_new_cases['3/31/22'])
plt.legend(['Describtion for line'])
plt.title('Title goes here')


# Plots the chart
st.plotly_chart(fig)
