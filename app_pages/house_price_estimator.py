import streamlit as st
import numpy as np
import pandas as pd
import joblib
from src.data_loading import load_house_price_data, load_pkl_file

def house_price_estimator():
    st.write("This is the house price estimator page.")

    # load inherited houses file
    df = pd.read_csv("inputs/datasets/raw/inherited_houses/house-prices/inherited_houses.csv")

    st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"displaying the data for the inherited houses.")
        
    st.write(df)
	
    # load files needed for predicting house prices 
    version = 'v1'
    pipeline = joblib.load(f"outputs/predict_price/{version}/best_regressor_pipeline.pkl")
    best_features = (pd.read_csv(f"outputs/predict_price/{version}/X_train.csv")
                            # .columns
                            # .to_list()
                            )
    
        # predict prices of inherited houses with ML pipeline	
    st.write("### Details of the inherited houses and their predicted sale prices")
    st.write(
        f"* Details of the inherited houses, showing all features."
    )
    st.write(df)
    df = df.filter(best_features)
    house_price_prediction = pipeline.predict(df).round(0)
    df['Predicted House Sale Price'] = house_price_prediction
    st.write(
        f"* This table shows the predicted sale prices for the inherited houses, focussing on the identified features with the strongest PPS: "
        "'Overall Quality' and 'Above Ground Living Area Square Feet'."
    )
    st.write(df)
