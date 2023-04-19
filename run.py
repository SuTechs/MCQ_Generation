from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
import json

from app.mcq_generation import MCQGenerator

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mcq = MCQGenerator()


@app.route('/')
@cross_origin()
def index():
    return send_from_directory('static', 'index.html')


@app.route('/<path:path>')
@cross_origin()
def static_files(path):
    return send_from_directory('static', path)


@app.route("/generate_question", methods=["POST"])
@cross_origin()
def generate():
    try:
        data = request.json
        text = data.get('text')

        if not text:
            return jsonify({'error': 'Text is required'}), 400

        # Load cached questions from a JSON file
        try:
            with open('cached_questions.json', 'r') as f:
                cached_questions = json.load(f)
        except FileNotFoundError:
            cached_questions = {}

        # Check if the questions are already cached for this text
        if text in cached_questions:
            questions = cached_questions[text]
        else:
            count = data.get('count', 9)
            generated_questions = mcq.generate_mcq_questions(text, count)

            # Cache the generated questions for future use
            questions = [q.__dict__ for q in generated_questions]
            cached_questions[text] = questions

            with open('cached_questions.json', 'w') as f:
                json.dump(cached_questions, f, indent=4)

        return jsonify(questions)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
