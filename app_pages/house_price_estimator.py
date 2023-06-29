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
	
    # load files needed for estimating house prices 
    version = 'v1'
    pipeline = joblib.load(f"outputs/predict_price/{version}/best_regressor_pipeline_updated.pkl")
    best_features = (pd.read_csv(f"outputs/predict_price/{version}/X_train.csv")
                            .columns
                            .to_list()
                            )
    
        # estimate prices of inherited houses with ML pipeline	
    st.write("### Details of the inherited houses and their estimated sale prices")
    st.write(
        f"* Details of the inherited houses, showing all features."
    )
    st.write(df)
    df = df.filter(best_features)
    house_price_prediction = pipeline.predict(df).round(0)
    df['Estimated House Sale Price'] = house_price_prediction
    st.write(
        f"* This table shows the estimate sale prices for the inherited houses, focussing on the identified features with the strongest PPS: "
        "'Overall Quality' and 'Above Ground Living Area Square Feet'."
    )
    st.write(df)

    # estimate price of any other house in Ames, Iowa
    st.write("### Estimate house sale prices in Ames, Iowa  \n")
    st.write("* 'Above Ground Living Area Square Feet' and 'Overall Quality' are the features identified to estimate the sale price of a house. ")

    # Create input fields
    def DrawInputsWidgets():

        # load dataset
        df = load_house_price_data()
        percentageMin, percentageMax = 0.5, 1.0

        # we create input widgets only for two features	
        col1, col2 = st.columns(2)

        # We are using these features to feed the ML pipeline
            
        # create an empty DataFrame, which will be the live data
        X_live = pd.DataFrame([], index=[0]) 

        # from here on we draw the widget based on the variable type (numerical or categorical)
        # and set initial values
        with col1:
            feature = 'GrLivArea'
            st_widget = st.number_input(
                label= feature,
                min_value= df[feature].min()*percentageMin,
                max_value= df[feature].max()*percentageMax,
                value= df[feature].median()
                )
        X_live[feature] = st_widget


        with col2:
            feature = "OverallQual"
            st_widget = st.selectbox(
                label= feature,
                options= df[feature].sort_values(ascending=True).unique()
                )
        X_live[feature] = st_widget

        return X_live
    
    # create input fields for live data
    X_live = DrawInputsWidgets()
    # estimate on input data
    if st.button("Run Sale Price Estimator"):
        house_price_prediction = pipeline.predict(X_live.filter(best_features)).round(0)
        st.write(
            f"### The estimated sale price for the house is: &nbsp; &nbsp; &nbsp;{house_price_prediction[0]}  \n"
        )
            
    