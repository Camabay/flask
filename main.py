from crypt import methods
from unittest import result
from flask import Flask,render_template,url_for,request
from flask import request as req

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("/App.html")
@app.route("/Distancia",methods=["GET","POST"])
def Distancia():
    if req.method=="POST":
        dato1=req.form["dat1"]
        dato2=req.form["dat2"]

    def cosenoS(data2,data3):
        import os
        try:
            from sklearn.metrics.pairwise import cosine_similarity
        except ModuleNotFoundError:
            os.system('pip install sklearn')
            from sklearn.metrics.pairwise import cosine_similarity

        try:
            import numpy as np
        except ModuleNotFoundError:
            os.system('pip install numpy')
            import numpy as np

        try:
            from stop_words import get_stop_words
        except ModuleNotFoundError:
            os.system('pip install stop_words')
            from stop_words import get_stop_words

        stop_words = get_stop_words ('spanish')
        data1 = []
        data1.append(data2)
        data1.append(data3)

        from sklearn.feature_extraction.text import TfidfVectorizer
        tfid = TfidfVectorizer().fit_transform(data1)

        from sklearn.metrics.pairwise import cosine_similarity
        return(cosine_similarity(tfid[1],tfid[0])[0])
        

    output=cosenoS(format(req.form['dat1']),format(req.form['dat2']))

    return render_template("/App.html",result=output)

if __name__ == '__main__':
    app.debug=True
    app.run()
