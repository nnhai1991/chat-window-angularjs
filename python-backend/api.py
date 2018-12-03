#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask import make_response
from flask import abort

app = Flask(__name__)

@app.route('/api/ask', methods=['POST'])
def api_ask():
    if not request.json or not 'user_message' in request.json:
        abort(400)

    question =  request.json['user_message'],
    answer = {
        'question' : question,
        'answer' : "i'm a poor boy from a poor family"
    }
    return jsonify(answer), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(port=8080)