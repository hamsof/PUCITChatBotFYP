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
