import pandas as pd
import numpy as np
import string
import re
import string
import contractions
from cleantext import clean
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.pipeline import Pipeline
import nltk
import pickle
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')



def count_punc(mystr):
    return len([c for c in mystr if c in string.punctuation])

df = pd.read_csv('datasets/SMSSpamCollection', sep='\t', header=None, names=['label', 'text'])
df['length'] = df['text'].apply(len)
df['punc'] = df['text'].apply(lambda x: count_punc(x))

df.to_csv('datasets/sms1.csv', index=False)
df = pd.read_csv('datasets/sms1.csv')



stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
wn = WordNetLemmatizer()

def text_preprocessing(mystr):
    mystr = mystr.lower()                                               # case folding
    mystr = re.sub('\w*\d\w*', '', mystr)                               # remove digits
    mystr = re.sub('\n', ' ', mystr)                                    # replace new line characters with space
    mystr = re.sub('[‘’“”…]', '', mystr)                                # removing double quotes and single quotes
    mystr = re.sub('<.*?>', '', mystr)                                  # removing html tags 
    mystr = re.sub(r'\[.*?\]', '', mystr)                               # remove text in square brackets
    mystr = re.sub('https?://\S+|www.\.\S+', '', mystr)                 # removing URLs
    mystr = re.sub('\n', ' ', mystr)                                    # replace new line characters with space
    mystr = ''.join([c for c in mystr if c not in string.punctuation])  # remove punctuations
    mystr = ' '.join([contractions.fix(word) for word in mystr.split()])# expand contractions
    
    tokens = word_tokenize(mystr)                                       # tokenize the string
    mystr = ''.join([c for c in mystr if c not in string.punctuation])  # remove punctuations
    tokens = [token for token in tokens if token not in stop_words]     # remove stopwords
    tokens = [wn.lemmatize(token) for token in tokens]                   # lemmatization
    new_str = ' '.join(tokens)
    return new_str

df['processed_text'] = df['text'].apply(lambda x: text_preprocessing(x))
cv = CountVectorizer() 
bow = cv.fit_transform(df['processed_text']) 
pickle.dump(cv, open('cv-transform.pkl', 'wb'))
X = bow
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5, shuffle=True)
model = MultinomialNB()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

filename = 'NaiveModel.pkl'
pickle.dump(model, open(filename, 'wb'))
    