# imports
import streamlit as st
import os
import webbrowser

# Create Header
st.markdown("# Portfolio - Silvano Ross")


# create repository of projects
projects = {
    "Blockchain Ledger": 'https://github.com/silvanoross/Block_Chain_Ledger',
    "Chicken Futures": 'https://github.com/silvanoross/Meat_Predictor',
    "AWS Robo Advisor": 'https://github.com/silvanoross/AWS_Robo_Adviser',
    "Predicting Success": 'https://github.com/silvanoross/Predicting_Success',
    "Crypto Notifier": 'https://github.com/silvanoross/Crypto_Notifier',   
}

project_list = []
for key, value in projects.items():
    project_list.append(key)

# Markdown sidebar
st.sidebar.markdown("# Past Projects")
# create sidebar to make selection
project = st.sidebar.selectbox(
    "Select project to view",
    project_list
)

# go to link associated with project
if st.sidebar.button("Go to Project"):
    webbrowser.open(projects[project])

