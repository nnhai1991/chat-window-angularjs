#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask import make_response
from flask import abort
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/ask', methods=['POST'])
@cross_origin()
def api_ask():
    if not request.json or not 'user_message' in request.json:
        abort(400)

    question =  request.json['user_message'],
    answer = {
        'type':"answer",
        'question' : question,
        'message' : "I'm a poor boy from a poor family. Easy come, easy go, will you let me go?"
    }
    return jsonify(answer), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(port=8080)