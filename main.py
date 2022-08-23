from flask import Flask, render_template
import requests

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def server_info():
    return render_template(index.html)

if __name__ == "__main__":
    app.run()
