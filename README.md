# PUCITChatBotFYP
Collection of codes related to our Final Year Project of developing AI driven chatbot application for PUCIT
<br>

## Regression through OLS:

Linear and Mulitlinear Regression implemented using Sklearn's Ordinary Least Squares(OLS) Model

### Packages Required:
1. math
2. numpy
3. pandas
4. matplotlib
5. seaborn
6. plotly
7. sklearn

Data Sets are attached, along with the Jupyter Notebook 
<br>

## Regression through Gradient Descent:

Linear and Mulitlinear Regression implemented using Gradient Descent Algorithm

### Packages Required:
1. numpy
2. pandas
3. matplotlib

Data Sets are attached, along with the Jupyter Notebook 
<br>

## Topic Modelling through Latent Dirichlet Allocation:

Topic Modelling model implemented using Sklearn's Latent Dirichlet Allocation.

### Packages Required:
1. pandas
2. sklearn

The data set used in this model is available at https://mega.nz/file/ziIGGZYB#gO19bK5z3bajnsL9cRvZ8ztsSrwZKqLR_zTl-Qz8Aew
<br>

## Spam Ham detection

### Packages Required:
1. sklearn
2. nltk
3. pickle
4. Flask
5. Jinja

### Process
1. model.py
  &emsp;- Using text processing and Naive Bayes train the dataset. <br>
  &emsp;- Second pickle these two models separately. <br>  
2. app.py
  &emsp;- Get the input from user pass this text to text preprocessing pickle model. <br>
  &emsp;- Then pass this pre processed text to Naive Bayes pickle file to see if it is ham or spam. <br>
  &emsp;- By using Jinja`s syntax we can communicate from frontend to backend
  
Email filtering system deployed on Heroku developed in Flask : https://emaildetectionsystem.herokuapp.com

<br>
