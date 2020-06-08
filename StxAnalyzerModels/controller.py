from flask import Flask, request, jsonify
import model

app = Flask(__name__)


# @app.route('/calculateInterest', methods=['POST'])
# def calculate_interest():
#     data = request.json
#     result = model.calculate_interest(data)
#     res = {'total_return': result[0], 'monthly_return': result[1]}
#     return res


@app.route('/get_sp_500', methods=['GET'])
def calculate_interest():
    return jsonify(model.get_sp_500())


if __name__ == '__main__':
    app.run()
