# Word Prediction using LSTM:
The model will predict the next n words of a movie title given a starting word, using Long Short Term Memory.
Keras pre-defined model is used.
## Installing Keras:
To install keras follow the given link of tutorialspoint: 
https://www.tutorialspoint.com/keras/keras_installation.htm
## About Dataset:
The dataset is uploaded in the contents folder. It contains information about around 5000 movies. Names of movies are extracted to feed to the model.
## About Model:
Model is using the following layers of the sequential model: Dense,LSTM,Embedding.<br>
The details of each layer is given in the notebook.

## Training Model:

The model was first trained on 100 epoch and default leaning rate of adam optimizer giving accuracy of around 30 percent. On changing the epochs to 150 the accuracy increased to 35 percent. The changing the learning rate of adam optimizer to 0.004(after a few tries) the accuracy increased upto 63 percent


# Stock Price Prediction using LSTM:
The model will predict the stock price for the next day.Keras pre-defined model is used.

## About Dataset:
The dataset is uploaded in the contents folder. It contains testing and training datasets which contains the opening, closing and other related attributes required for the model
## About Model:
Model is using the following layers of the sequential model: Dense,LSTM.<br>
The details of each layer is given in the notebook.

## Training Model:
The model is trained at 100 epochs with a batch size of 32




