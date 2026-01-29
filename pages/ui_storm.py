import streamlit as st
from st_aggrid import AgGrid

import pandas as pd
# strom = pd.read_csv('Historical_Tropical_Storm_V3.csv', encoding='utf-8')
path = 'D:/work/study_python/ryan/storm/Historical_Tropical_Storm_V3.csv'
strom = pd.read_csv(path)

st.set_page_config(layout="wide")
AgGrid(strom, height=600,)