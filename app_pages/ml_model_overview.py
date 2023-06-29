import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from src.data_loading import load_pkl_file
from src.model_evaluation import regression_performance, regression_evaluation, regression_evaluation_plots


def ml_model_overview():

    # loadind house price pipeline files
    version = 'v1'
    pipeline = load_pkl_file(f"outputs/predict_price/{version}/best_regressor_pipeline_updated.pkl")
    house_price_feat_importance = plt.imread(f"outputs/predict_price/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/predict_price/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/predict_price/{version}/X_test.csv")
    y_train =  pd.read_csv(f"outputs/predict_price/{version}/y_train.csv").squeeze()
    y_test =  pd.read_csv(f"outputs/predict_price/{version}/y_test.csv").squeeze()

 

    st.write("### ML Sale Price Estimator Pipeline")

    # model performance
    st.info(
        f"* We agreed with the client on an R2 score of at least 0.75 on both train and test "
        f"set.  \n"
        f"* Our pipeline achieves 0.86 and 0.79 on the train set and test set respectively  \n"    
    )
    st.write("---")

        # showing features and their importance for the ML model
    st.write("* **Training Features based on Feature Importance Study**")
    st.info("The Features identified as most important for estimating the sale price is 'OverallQual', followed by 'GrLivArea'.")
    st.write(X_train.columns.to_list())
    st.image(house_price_feat_importance)
    st.write("---")

    # # show pipeline steps
    # # Convert pipeline to dictionary
    # pipeline_dict = {
    #     'steps': [
    #         (step_name, step) for step_name, step in pipeline.steps
    #     ]
    # }

    # pipeline_info = [(step_name, step) for step_name, step in pipeline.steps]

    # # # Render pipeline steps
    # # st.write("* **ML Pipeline Steps Overview**")
    # # st.write(pipeline_info)
    # # st.write("---")

    # evaluate performance on train and test sets
    regression_performance(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, pipeline=pipeline)
    
    st.write("---")
     
    # Plot predicted versus actual sale price for train and test sets
    st.write("* **Estimated vs Actual Sale Price Scatterplot**")
    st.info("* For prices below $400000, the estimated prices and actual \n"
    " prices match closely, indicated by the data points following the red line closely.  \n"
    "* For higher prices, the model estimates of the Sale Price of a property becomes less accurate. "
    "On the scatterplot showing the estimates on the train set (left plot below), "
    "the Sale Prices above $400000 are underestimated (data points below the red line)"
    )
    regression_evaluation_plots(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, pipeline=pipeline, alpha_scatter=0.5)
