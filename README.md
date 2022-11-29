# PUCITChatBotFYP
Collection of codes related to our Final Year Project of developing AI driven chatbot application for PUCIT
<br>

## MACHINE LEARNING
The following topics are studied and implemented under the domain of Machine Learning.
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

## Spam Ham detection:

Detecting email text as Spam or Ham using Naive Bayes.

### Packages Required:
1. sklearn
2. nltk
3. pickle
4. Flask
5. Jinja

### Process
1. model.py<br>
  &emsp;- Using text processing and Naive Bayes train the dataset. <br>
  &emsp;- Second pickle these two models separately. <br>  
2. app.py<br>
  &emsp;- Get the input from user pass this text to text preprocessing pickle model. <br>
  &emsp;- Then pass this pre processed text to Naive Bayes pickle file to see if it is ham or spam. <br>
  &emsp;- By using Jinja`s syntax we can communicate from frontend to backend
  
Email filtering system deployed on Heroku developed in Flask : https://emaildetectionsystem.herokuapp.com

<br>

## DEEP LEARNING
The following topics are studied and implemented under the domain of Machine Learning.
<br>
## Introduction to Deep Learning And Artificial Neural Networks:
An Overview to what deep learning is and why it is needed, and an introduction of topics that are necassary to know about before stepping into the world of deep learning, starting from Artificial Neural Networks. The topics includes:
1. Working of Perceptron
2. Bias in Perceptron
3. What are Activation functions
4. Different Types of Activation functions
5. How to choose an Activation function
6. What are Loss functions
7. Forward Propagation
8. Backward Propagation

<br>

## Batched Gradient Descent:
Batched Gradient Descent is implemented using numpy. The working of BGD is explained step by step using toy dataset and then the implementation is done on real world dataset.
### Packages Required:
1. numpy
2. pandas
3. matplotlib

Data Sets are attached, along with the Jupyter Notebook.
The Dataset "Book1.csv" is the dataset of toy example while "GPA.csv" is the real dataset. Two different datasets are used because for BGD to give good results dataset should include atleast 30 datapoints.
<br>

## Stochastic Gradient Descent:
`SGD takes a random instance of the training data at each step and computes the gradient. This makes it much faster than BGD as it processes much less data at a time.`<br>
Stochastic Gradient Descent is implemented using numpy. The working of SGD is explained step by step using toy dataset and then the implementation is done on real world dataset.

### Packages Required:
1. numpy
2. pandas
3. matplotlib

Data Sets are attached, along with the Jupyter Notebook.
The Dataset "Book1.csv" is the dataset of toy example while "GPA.csv" is the real dataset. Two different datasets are used because for SGD to give good results dataset should include atleast 30 datapoints.
<br>
