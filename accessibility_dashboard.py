import pandas as pd
import numpy as np

import plotly.express as px

import streamlit as st


url_hsbc = 'https://raw.githubusercontent.com/RomanTomz/bank_acessibility/main/hsbc_data.csv'
url_nw = 'https://raw.githubusercontent.com/RomanTomz/bank_acessibility/main/nw_data.csv'
url_pct_hsbc = 'https://raw.githubusercontent.com/RomanTomz/bank_acessibility/main/hsbc_pct.csv'
url_pct_nw = 'https://raw.githubusercontent.com/RomanTomz/bank_acessibility/main/nw_pct.csv'


@st.cache()
def load_data_hsbc():
    df = pd.read_csv(url_hsbc)
    return df

@st.cache()
def load_data_nw():
    df_nw = pd.read_csv(url_nw)
    return df_nw

@st.cache()
def load_data_pct_hsbc():
    hsbc_pct = pd.read_csv(url_pct_hsbc)
    return hsbc_pct 

@st.cache()
def load_data_pct_nw():
    nw_pct = pd.read_csv(url_pct_nw)
    return nw_pct

df = load_data_hsbc()
df_nw = load_data_nw()
pct_hsbc = load_data_pct_hsbc()
pct_nw = load_data_pct_nw()