# PUCITChatBotFYP
Collection of codes related to our Final Year Project of developing AI driven chatbot application for PUCIT

- [MACHINE LEARNING](#machine-learning)
  * [SUPERVISED MACHINE LEARNING](#supervised-machine-learning)
    + [REGRESSION](#regression)
      - [REGRESSION THROUGH OLS](#regression-through-ols)
      - [REGRESSION THROUGH GRADIENT DESCENT](#regression-through-gradient-descent)
      - [BATCHED GRADIENT DESCENT](#batched-gradient-descent)
      - [STOCHASTIC GRADIENT DESCENT](#stochastic-gradient-descent)
      - [PROBLEMS OF GRADIENT DESCENT](#problems-of-gradient-descent)
    + [CLASSIFICATION](#classification)
      - [SPAM HAM DETECTION THROUGH NAIVE BAYES](#spam-ham-detection-through-naive-bayes)
  * [UNSUPERVISED MACHINE LEARNING](#unsupervised-machine-learning)
      - [TOPIC MODELLING THROUGH LATENT DIRICHLET ALLOCATION](#topic-modelling-through-latent-dirichlet-allocation)
- [DEEP LEARNING](#deep-learning)
  * [INTRODUCTION TO DEEP LEARNING](#introduction-to-deep-learning)
    + [ARTIFICIAL NEURAL NETWORKS](#artificial-neural-networks)
  * [RECURRENT NEURAL NETWORKS](#recurrent-neural-networks)
    + [LONG SHORT-TERM MEMORY](#long-short-term-memory)

# MACHINE LEARNING
The following topics are studied and implemented under the domain of Machine Learning.

## SUPERVISED MACHINE LEARNING
Supervised learning, also known as supervised machine learning, is a subcategory of machine learning and artificial intelligence. It is defined by its use of labeled datasets to train algorithms that to classify data or predict outcomes accurately. Supervised Machine Learning is further divided into Regression and Classification.<br>
### REGRESSION
Regression is a statistical method used to predict the value of the dependent variable based on the known value of the independent variable assuming the relationship between two or more variables. Regression is implemented in the following ways:
#### REGRESSION THROUGH OLS
Linear and Mulitlinear Regression implemented using Sklearn's Ordinary Least Squares(OLS) Model

#### REGRESSION THROUGH GRADIENT DESCENT
Linear and Mulitlinear Regression implemented using Gradient Descent Algorithm

#### BATCHED GRADIENT DESCENT
Batched Gradient Descent is implemented using numpy. The working of BGD is explained step by step using toy dataset and then the implementation is done on real world dataset.

#### STOCHASTIC GRADIENT DESCENT
SGD takes a random instance of the training data at each step and computes the gradient. This makes it much faster than BGD as it processes much less data at a time.
#### PROBLEMS OF GRADIENT DESCENT
This notebook explains the problems we face while implementing Gradient Descent. These problems include saddle point, vanishing gradient problem and exploding gradient problem. 

### CLASSIFICATION
classification is a predictive modeling problem where the class label is anticipated for a specific example of input data. Classification is implemented in the following ways:
#### SPAM HAM DETECTION THROUGH NAIVE BAYES
Detecting email text as Spam or Ham using Naive Bayes.
## UNSUPERVISED MACHINE LEARNING
Unsupervised learning is a type of algorithm that learns patterns from untagged data. Following topics are covered under it's domain.  
#### TOPIC MODELLING THROUGH LATENT DIRICHLET ALLOCATION
Topic Modelling model implemented using Sklearn's Latent Dirichlet Allocation.


# DEEP LEARNING
The following topics are studied and implemented under the domain of Deep Learning.
<br>

## INTRODUCTION TO DEEP LEARNING 
An Overview to what deep learning is and why it is needed
### ARTIFICIAL NEURAL NETWORKS
An introduction of topics that are necessary to know about before stepping into the world of deep learning, starting from Artificial Neural Networks.

## RECURRENT NEURAL NETWORKS
A detailed explanation of what RNNs are, what are it's applications and the vanishing gradient problem which exists in it. Following topics are covered under RNN.

### LONG SHORT-TERM MEMORY
A detailed explanantion of LSTM, how it works and it's implementation.








