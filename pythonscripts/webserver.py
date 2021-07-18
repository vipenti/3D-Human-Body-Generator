import flask
from flask import request
from flask_cors import CORS
import blenderinvoker
import json

app = flask.Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def home():

    print(request.json)
    if request.method == 'POST':
        obj = request.json
        dicti = json.loads(str(obj).replace("\'", "\""))
        print(dicti["torso"])
        blenderinvoker.execute(dicti)

    return  flask.current_app.send_static_file('..\index.html')


app.run()
