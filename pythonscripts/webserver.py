import flask
from flask import jsonify, request
from flask_cors import CORS
import blenderinvoker
import json
from pygltflib import GLTF2

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

    return "done"


app.run()
