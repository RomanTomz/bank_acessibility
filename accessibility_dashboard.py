import pandas as pd
import numpy as np

import plotly.express as px

import streamlit as st

st.beta_set_page_config(layout='wide')

mapbox_token = 'pk.eyJ1IjoidG9tejg0IiwiYSI6ImNrOWdzeDl2bzBuenozbHRieXp4dmo2cmUifQ.8QfuEG6pmLxa-zdroSpbrw'
px.set_mapbox_access_token(mapbox_token)

url_hsbc = 'https://raw.githubusercontent.com/RomanTomz/bank_acessibility/main/hsbc_data.csv'
url_nw = 'https://raw.githubusercontent.com/RomanTomz/bank_acessibility/main/nw_data.csv'
url_pct_hsbc = 'https://raw.githubusercontent.com/RomanTomz/bank_acessibility/main/hsbc_pct.csv'
url_pct_nw = 'https://raw.githubusercontent.com/RomanTomz/bank_acessibility/main/nw_pct.csv'

# Creating all the functions for data import.

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

hsbc_pct = load_data_pct_hsbc()
hsbc_pct.rename(columns= {'index':'type'}, inplace=True)

nw_pct = load_data_pct_nw()
nw_pct.rename(columns= {'index':'type'}, inplace=True)

# Testing first map

#HSBC Map
fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",
                        size_max=15, zoom=5,
                       text=df.Name)
fig.update_traces(marker=dict(size=8,
                              color=df.colour))
fig.update_layout(mapbox_style='open-street-map',width=1400,height=900)

# Nation Wide Map
fig_nw = px.scatter_mapbox(df_nw, lat="Latitude", lon="Longitude",
                        size_max=15, zoom=5,
                       text=df_nw.Name)
fig_nw.update_traces(marker=dict(size=8,
                              color=df_nw.colour))
fig_nw.update_layout(mapbox_style='open-street-map')

# Barchart HSBC
fig_pct_hsbc = px.bar(hsbc_pct, x='type', y='Accessibility',
                   text='Accessibility')
fig_pct_hsbc.update_traces(marker_color='#F17D0F',
                        marker_line_color='#3498DB',
                        marker_line_width=2,
                        opacity=0.8)
fig_pct_hsbc.update_layout(title_text='Percentage of HSBC Branches by Accessibility Type',width=1100)

#Barchart Nation Wide
fig_pct_nw = px.bar(nw_pct, x='type', y='Accessibility',
                   text='Accessibility')
fig_pct_nw.update_traces(marker_color='#F17D0F',
                        marker_line_color='#3498DB',
                        marker_line_width=2,
                        opacity=0.8)
fig_pct_nw.update_layout(title_text='Percentage of Nation Wide Branches by Accessibility Type')

st.title('Bank Accessibiility - Wheelchair Access and Hearing Aid')

viz = st.sidebar.radio('Select Bank',('HSBC','Nation Wide'))

if viz == 'HSBC':
    st.plotly_chart(fig_pct_hsbc)
    st.markdown('Map Visualisation')
    st.plotly_chart(fig)

if viz == 'Nation Wide':
    st.plotly_chart(fig_pct_nw)
    st.markdown('Map Visualisation')
    st.plotly_chart(fig_nw)

st.sidebar.markdown('Hi Bob, this is an example that we can showcase both to Matt and Jenny when it will be the time. This webapp pulls data from OpenBanking API and displays it')

st.sidebar.markdown('The code for the dashboard is here: https://github.com/RomanTomz/bank_acessibility. In this example, GitHub acts as container for all the packages needed and once deployed it runs independently on the TP server')