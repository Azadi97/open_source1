import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

@st.cache(suppress_st_warning=True) 
def loadData():
    st.write("Cache miss: Loading data")
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
    df["date"] = pd.to_datetime(df["date"])
    return df

@st.cache(suppress_st_warning=True) 
def getCountriesList(df):
    st.write("Cache miss: Getting countries list")
    # Get the countries list
    clist = df['location'].unique()

    # Define things that are not countries and remove them from the countries list
    notCountries = ['Africa', 'Asia', 'Central African Republic', 'Europe', 'European Union', 'High income', 'International', 'Low income', 'Lower middle income', 'North America', 'Oceania', 'South Africa', 'South America', 'Upper middle income', 'World']
    clist = list(clist)
    for i in notCountries:
        clist.remove(i)
    return clist

df = loadData()
clist = getCountriesList(df)

typeList = {'New cases':'new_cases', 'New cases smoothed (7-day rolling average)':'new_cases_smoothed', 'Cummulative cases': 'total_cases', 'New deaths':'new_deaths', 'New deaths smoothed (7-day rolling average)':'new_deaths_smoothed', 'Cummulative deaths': 'total_deaths'}

# Create the streamlit sidebar
country = st.sidebar.selectbox("Select a country:",clist)
dataType = st.sidebar.selectbox("Select the type of data you want to see:",typeList.keys())
dataTypeSelection = typeList[dataType]

normalized = st.sidebar.checkbox('Normalized data (per million habitants of the country)')
if normalized:
    dataType += " per million habitants of the country"
    dataTypeSelection += "_per_million"
# The header of the figure
st.header("COVID-19 cases per country")

cases = df[df['location'] == country][dataTypeSelection]
dates = list(df[df['location'] == country]['date'])

# Create a figure
fig, ax = plt.subplots()
# plot data
ax.plot( dates, cases)
ax.tick_params(axis='x',rotation=90)
ax.set_xlabel("Date")
ax.set_ylabel(dataType)
st.write(country)


# Plots the chart
st.plotly_chart(fig)
