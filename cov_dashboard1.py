import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Read the data
# deaths = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")

# df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')

# Get the countries list
clist = df['Country/Region'].unique()

# Create the streamlit sidebar
country = st.sidebar.selectbox("Select a country:",clist)

# The header of the figure
st.header("COVID-19 cases per country")


# Create a figure
fig = plt.figure()
plt.plot(df[df["location"]==country].iloc[[0]].iloc[:].values[0])

plt.title("Cumulative cases in " + country)


# Plots the chart
st.plotly_chart(fig)
