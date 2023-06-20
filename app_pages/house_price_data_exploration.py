import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
import numpy as np
from src.data_loading import load_house_price_data

def house_price_data_exploration():
    st.write("This is the house price data exploration page.")

    # object variables
    df = load_house_price_data()
 

    # copied from README file - "Business Requirements" section
    st.write("### House Sale Price study")
    st.info(
        f"* The client is interested in discovering how the house attributes correlate with the sale price."
        f" Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.")


    # display housing data dataframe
    if st.checkbox("View sample of the housing data."):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"displaying the first 15 rows of the sale price data.")
        
        st.write(df.head(15))

    st.write("---")


    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted to identify the most important variables for determining \n"
        f" the house sale price. The 6 most important variables are listed below, with descriptions  \n"
    )

    # Meaning of variables: From README file - "Dataset Content" section
    st.info(
        f"Meaning of variables:  \n"
        f"* **OverallQual**: Rates the overall material and finish of the house.  \n"
        f"* **1stFlrSF**: First Floor square feet. \n"
        f"* **GarageArea**: Size of garage in square feet. \n"
        f"* **GrLivArea**: Above grade (ground) living area square feet. \n"
        f"* **TotalBsmtSF**: Total square feet of basement area. \n"
        f"* **YearBuilt**: Original construction date. \n"
    )

    # Heatmap of Predictive Power Scores
    if st.checkbox("Heatmap showing the identified key property features."):
        st.image("outputs/house_prices_study/v1/pps_heatmap.png", width=600)

    
        
    # Scatterplots of sale price against correlated variable
    if st.checkbox("Scatterplots for the six most important attributes, showing how sale price increases with "
    "the value rating of the attribute. Ex: 'Overall Quality'"):
    
        st.write(f"* Plot Sale Price against attribute")
        scatterplot(df)

def scatterplot(df):

    for col in ['TotalBsmtSF', '1stFlrSF', 'GrLivArea', 'GarageArea', 'YearBuilt', 'OverallQual']:
        fig, axes = plt.subplots(figsize=(8, 5))
        sns.scatterplot(data=df, x=col, y='SalePrice')
        st.pyplot(fig)
        st.write("\n")



