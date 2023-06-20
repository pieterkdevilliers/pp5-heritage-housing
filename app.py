import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages import house_price_data_exploration, house_price_estimator, project_hypothesis, project_summary

app = MultiPage(app_name= "House Price Estimator") # Create an instance of the app 

app.add_page("Project Summary", project_summary.project_summary) # Add the project summary page
app.add_page("Hypothesis Outline", project_hypothesis.project_hypothesis) # Add the project hypothesis outline page
app.add_page("House Price Data Exploration", house_price_data_exploration.house_price_data_exploration) # Add the house price data exploration page
app.add_page("House Price Estimator", house_price_estimator.house_price_estimator) # Add the house price estimator page



app.run() # Run the app