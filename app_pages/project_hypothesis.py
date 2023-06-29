import streamlit as st

def project_hypothesis():
    st.write("### Project Hypothesis")

    # information from README file
    st.success(
        f"**Project Hypothesis**\n"
        f"* The sale price of a property is assumed to be correlated with the features of the house.\n"
        f" However, the hypothesis here is that not all features are created equal. Some features will be much more closely correlated with the sale price of a property.\n"
        f" In order to estimate the sale price of a property,\n"
        f"we need to determine which of the property features correlated more closely to the sale price.\n"
        f"In this project we are using Spearman and Pearson correlation to study the feature correlation to the sale price.\n"
        f"We are using Predictive Power Score to determine the features of a property most closely correlated to the sale price.\n"
        )
    
    st.write("### Feature Importance Results")
    st.write(
        f"This image shows the result of the feature importance analysis,\n"
        f"with Overall Quality and Ground Floor Living Area proving to be the stringest predictors of sale price.\n")
    st.image("outputs/predict_price/v1/features_importance.png", width=600)