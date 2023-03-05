import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(page_title="contries",
                   page_icon=":gem:",
                   layout="wide"
                   )

data = pd.read_csv('./countries.csv')


st.sidebar.header("please filter here:")

year = st.sidebar.multiselect(
    "select the year",
    options=data["year"].unique(),
    default=data["year"].unique()
)

country = st.sidebar.multiselect(
    "select the country",
    options=data["country"].unique(),
    default=data["country"].unique()
)


data_selection = data.query(
    "country == @country &  year == @year"
)

# =============== mainpage ===============
st.title(":bar_chart: population Dashboard")
st.markdown("##")
st.markdown("---")


st.dataframe(data)

# ===========
us = data_selection[data.country == 'United States']
Mo = data_selection[data.country == 'Morocco']
China = data_selection[data.country == 'China']
st.header('Plot of Data')

fig, ax = plt.subplots(1, 1)
ax.plot(us.year, us.population / us.population.iloc[0] * 10)
ax.plot(Mo.year, Mo.population / Mo.population.iloc[0] * 10)
ax.plot(China.year, China.population / China.population.iloc[0] * 10)
ax.set_xlabel('year')
ax.set_ylabel('population growth (first year =10)')
ax.legend(['United States', 'China', 'Morocco'])


st.pyplot(fig)


# css code =============

hide = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
'''
st.markdown(hide, unsafe_allow_html=True)
