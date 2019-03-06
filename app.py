from flask import Flask, request, jsonify

from run_squad import answer_question, load_default_prediction_model


model = load_default_prediction_model()
app = Flask(__name__)


@app.route('/answer', methods=['POST'])
def answer():
    request_json = request.get_json()
    return jsonify({
        'answer': answer_question(**request_json, model=model)
    })


if __name__ == '__main__':
    app.run()
