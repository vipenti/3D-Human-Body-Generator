import flask
from blenderinvoker import execute

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def home():

    execute()
    return


app.run()