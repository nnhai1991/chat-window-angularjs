#!flask/bin/python
from flask import Flask, jsonify,redirect,url_for
from flask import request
from flask import make_response
from flask import abort
from flask_cors import CORS, cross_origin
import os
import time

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

messages = {}

@app.route('/api/ask', methods=['POST'])
@cross_origin()
def api_ask():
    if not request.json or not 'user_message' in request.json or not 'client_id' in request.json:
        abort(400)
    
    clientID = request.json['client_id']

    question =  request.json['user_message']

    messages[clientID] = []

    answer1 = {
        'type':"answer",
        'question' : question,
        'message' : "Please wait a while...",
        'continue' : 1
    }

    answer2 = {
        'type':"answer",
        'question' : question,
        'message' : '',
        'continue' : 0
    }
    #return a temp message and process later
    messages[clientID].append(answer2)

    return jsonify(answer1), 200

@app.route('/api/more', methods=['POST'])
@cross_origin()
def api_more():
    if not request.json or not 'client_id' in request.json:
        abort(400)
    
    clientID = request.json['client_id']


    if (clientID not in messages == 0):
        print('queue not initialized')
        abort(400)
    
    if (len(messages[clientID]) == 0):
        print('empty queue')
        abort(400)

    answer = messages[clientID][0]

    del messages[clientID][0]

    #get original question question = answer['question']
    # do processing 
    time.sleep(1)
    answer['message'] = "I'm a poor boy from a poor family. Easy come, easy go, will you let me go?"

    return jsonify(answer), 200

@app.route('/')
def index():    
    return redirect('/static/index.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(port=8080)