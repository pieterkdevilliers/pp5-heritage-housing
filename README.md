

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|





## Business Requirements
As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.


## Hypothesis and how to validate?
* The sale price of a property is assumed to be correlated with the features of the house. However, the hypothesis here is that not all features are created equal. Some features will be much more closely correlated with the sale price of a property.
* In order to estimate the sale price of a property, we need to determine which of the property features correlated more closely to the sale price.
* In this project we are using Spearman and Pearson correlation to study the feature correlation to the sale price.
* In this project we are using Predictive Power Score to determine the features of a property most closely correlated to the sale price.


## The rationale to map the business requirements to the Data Visualisations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.


## ML Business Case
1. What are the business requirements?
    * The client wants to identify the correlation(s) between the features of a property, and the sale price of a speciic property.
    * The client wants to be able to estimate/predict the sale price of their 4 inherited houses, or any other houses in Ames, Iowa, as a cosideration for future property investments.
2. Is there any business requirement that can be answered with conventional data analysis?
    * We can use Data Analasys to identify those property features most closely correlated to the sale price of a house.
3. Does the client need a dashboard or an API endpoint?
    * The client only needs a dashboard in this instance.
4. What does the client consider as a successful project outcome?
    * A dashboard showing the most closely correlated features of a house, to the sale price.
    * The ability to estimate/predicts the sale price for the 4 inherited houses or any other house in Ames, Iowa.
5. Can you break down the project into Epics and User Stories?
    * Gathering requirements and collecting data.
    * Datacleaning, visualization and preparation.
    * Model training and optimization.
    * Dashboard designing and development.
    * Dashboard deployment.
6. Ethical or Privacy concerns?
    * As the data is a public data set, there are not concerns.
7. Does the data suggest a particular model?
    * The data suggests a regressor where the target is the sale price.
8. What are the model's inputs and intended outputs?
    * The inputs consist of the public data set including house features and sale price.
    * The outputs are the correlation studies and visualizations, as well as the ability to estimate/predict a properties' sale price.
9. What are the criteria for the performance goal of the predictions?
    * An R2 score of at least 0.75 on the train set and  the test set.
10. How will the client benefit?
    * The client will be able to estimate the sale price of the inherited properties, based on data analysis and not just opinion.
    * The client will also be able to estimate/predict the sale price of future investment properties. This can help in deciding which properties to buy, what changes to make to properties to get a higher sale price etc...


## Dashboard Design
  ### The Dashboard consists of 5 pages:
- Project Summary
- Hypothesis Outline
- House Price Data Exploration
- ML Model Overview
- House Price Estimator
---

### Project Summary:
  Contains a brief description of the dataset and the business requirements.

### Hypothesis Outline:
  Contains a brief outline of the project hypothesis as well as the results of the Feature Importance study.

### House Price Data Exploration:
  * Contains a sample of the dataset, made visible by selecting the indicated checkbox.

  * Displays the outcome of the corrolation study and the 6 identified features, as well as explanations of those features.

  * Contains a checkbox to reveal a heatmap of the key property features.

  * Contains a checkbox to access the scatter plots for the key features.

### House Price Estimator:
  Provides details of the inherited houses data set, as well as the estimated sale price for each house.

  Provides an interactive House Price Estimator, allowing the user to set the two features identified as having the highest Predictive Power Score. (GrLivArea and OverallQual)

  Once the values are set, the user can run the data through the ML Pipeline to be presented with the estimated Sale Price.

### ML Model Overview:
  Provides an overview of the ML Model Performance. Includes a Bar Plot showing the outcome of the Feature Importance Study, followed by the Pipeline Steps.
  This page also presents a Model Evaluation by computing the R2 score, 3 key error measures and a scatterplot of Estimated vs Actual Sale Price - Sale Price is the Target.


## Unfixed Bugs
* No bugs identified on deployment.

## Deployment
### Heroku

* The App live link is: [https://whispering-hollows-22544-495a525fa4fe.herokuapp.com/](https://whispering-hollows-22544-495a525fa4fe.herokuapp.com/) 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries
#### The libraries used in this project are:
numpy==1.18.5

pandas==1.4.2

matplotlib==3.3.1

seaborn==0.11.0

pandas-profiling

plotly==5.15.0

ppscore==1.2.0

joblib==1.2.0

streamlit==1.23.1

feature-engine==1.0.2

imbalanced-learn==0.8.0

scikit-learn==0.24.2

xgboost==1.2.1

yellowbrick==1.3

Jinja2==3.1.1

MarkupSafe==2.0.1

protobuf==3.20

ipywidgets==8.0.2

altair==4.1.0


## Credits 

* Main examples and guidance came was taken from the Code Institute Churnometer walkthrough project and the Scikit-learn lesson in the Data Analysis and Machine Learning Toolkit modules.
* Most of the code was taken from the Code Institute sources and adapted for this usecase.
* Big thanks to my mentor Precious Ijege for his guidance and willingness to answer questions - and keep me looking for the answers myself.
* Being able to review and compare my growing project with the example project was especially helpful when I got stuck down rabbit holes. (https://github.com/pieterkdevilliers/Sample-PP5)

