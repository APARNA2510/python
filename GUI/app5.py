#dashboard

import pandas as pd 
import plotly.express as px 
import streamlit as st 

# load data
def load_incident_data():
    return pd.read_csv('ui/incident.csv')

# clean data
# display
with st.spinner("Loading dataset..."):
    incident = load_incident_data()
st.dataframe(incident)    
# visualize