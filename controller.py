from flask import Flask, jsonify, request
from model import model

app = Flask(__name__)


@app.route('/calculateInterest', methods=['POST'])
def calculate_interest():
    data = request.json
    result = model.calculate_interest(data)
    return jsonify(result)


if __name__ == '__main__':
    app.run('localhost', 3000)
