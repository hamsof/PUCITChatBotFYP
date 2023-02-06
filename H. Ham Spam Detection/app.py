from flask import Flask, render_template,request
import pickle


app = Flask(__name__)

data_email = ""
msg = "" 

#loading models
filename = 'NaiveModel.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('cv-transform.pkl','rb'))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    if request.method == "POST":
        
        #Request data
        data_email = request.form["email_text"]
        data = [data_email]
        
        #models
        vect = cv.transform(data).toarray()
        class_type = classifier.predict(vect)

        #return msg
        if class_type == ['spam'] :
            msg = """<h4 style="color: red">Spam email be aware !!!!</h4>"""
        else : 
            msg = """<h4 style="color: green">email looks Good<<->> </h4>"""
    return render_template("index.html" ,msg= msg, data_email = data_email )

if __name__ == "__main__":
    app.run()    