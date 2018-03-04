
### IMPORTS ###
from flask import Flask, url_for,render_template,request,redirect
import tweepy

### FLASK APP STARTS HERE $$$
app = Flask(__name__)

## Routing    
@app.route("/")
def index():
    return render_template("index.html")