from flask import Flask, request, jsonify

from app.mcq_generation import MCQGenerator

app = Flask(__name__)
mcq = MCQGenerator()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/generate_question", methods=["POST"])
def generate():
    try:
        data = request.json
        text = data.get('text')

        if not text:
            return jsonify({'error': 'Text is required'}), 400

        count = data.get('count', 10)

        questions = mcq.generate_mcq_questions(text, count)

        result = [q.__dict__ for q in questions]
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
