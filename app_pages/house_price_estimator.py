import streamlit as st
import numpy as np
import pandas as pd
from src.data_loading import load_house_price_data, load_pkl_file

def house_price_estimator():
    st.write("This is the house price estimator page.")

    # load inherited houses file
    df = pd.read_csv("inputs/datasets/raw/inherited_houses/house-prices/inherited_houses.csv")
	
    # load files needed for predicting house prices 
    version = 'v1'
    print(version)
    pipeline = load_pkl_file(f"outputs/predict_price/{version}/best_regressor_pipeline.pkl")
    best_features = (pd.read_csv(f"outputs/predict_price/{version}/X_train.csv")
                            # .columns
                            # .to_list()
                            )
