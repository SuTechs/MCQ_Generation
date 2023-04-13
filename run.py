from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin

from app.mcq_generation import MCQGenerator

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mcq = MCQGenerator()


# @app.route('/')
# @cross_origin()
# def hello_world():
#     return 'Hello World!'


@app.route('/')
@cross_origin()
def index():
    return send_from_directory('static/web', 'index.html')


@app.route('/<path:path>')
@cross_origin()
def static_files(path):
    return send_from_directory('static/web', path)


@app.route("/generate_question", methods=["POST"])
@cross_origin()
def generate():
    try:
        data = request.json
        text = data.get('text')

        if not text:
            return jsonify({'error': 'Text is required'}), 400

        count = data.get('count', 9)

        questions = mcq.generate_mcq_questions(text, count)

        result = [q.__dict__ for q in questions]
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
