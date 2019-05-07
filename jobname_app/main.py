from flask import Flask, jsonify, request
import json

app = Flask(__name__)
LABELS_BY_INPUT = json.load(open('labels_by_input.json'))

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "JobName App is live"}), 200 

@app.route('/predict/', methods=['GET'])
def predict():
    user_input = request.args.get('input')
    if user_input in LABELS_BY_INPUT:
        return jsonify({"labels": LABELS_BY_INPUT[user_input]['Label']}), 200
    else:
        return jsonify({"message": "No recommendations for user input"}), 404

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)