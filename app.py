from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('social_networks')
def social_networks():
    return 'social_networks'

@app.route('personal_assistants')
def personal_assistants():
    return 'personal_assistants'

@app.route('alexa')
def alexa():
    return 'alexa'

@app.route('facebook')
def facebook():
    return 'facebook'