import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# This is needed to test localy
# In the heroku tutorial this code doenst exist plz remove.
# if __name__ == "__main__":
#     app.debug = True
#     app.run()
