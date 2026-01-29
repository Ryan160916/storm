import streamlit as st
from st_aggrid import AgGrid

import pandas as pd

st.set_page_config(layout='wide')

path = 'D:/work/study_python/ryan/storm/风速-v3.xlsx'
storm = pd.read_excel(path)
AgGrid(storm)


