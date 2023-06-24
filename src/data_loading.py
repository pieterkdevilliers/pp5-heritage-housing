import streamlit as st
import pandas as pd
import numpy as np
import joblib

# House Price Data
@st.cache_data()
def load_house_price_data():
    df = pd.read_csv("outputs/datasets/collection/house_prices_records.csv")
    return df

# load pkl file
def load_pkl_file(file_path):
    return joblib.load(filename=file_path)

