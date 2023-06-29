import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages import house_price_data_exploration, house_price_estimator, project_hypothesis, project_summary, ml_model_overview


app = MultiPage(app_name= "House Price Estimator") # Create an instance of the app 

app.add_page("Project Summary", project_summary.project_summary)
app.add_page("Hypothesis Outline", project_hypothesis.project_hypothesis)
app.add_page("House Price Data Exploration", house_price_data_exploration.house_price_data_exploration)
app.add_page("ML Model Overview", ml_model_overview.ml_model_overview)
app.add_page("House Price Estimator", house_price_estimator.house_price_estimator)



app.run() # Run the app