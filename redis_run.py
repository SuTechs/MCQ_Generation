from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
import redis

from app.mcq_generation import MCQGenerator

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mcq = MCQGenerator()

redis_client = redis.Redis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)
REDIS_EXPIRY_TIME = 60 * 60 * 24 * 7  # 7 day


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

        count = data.get('count', 9)

        # Check if the generated questions are already cached in Redis
        cached_questions = redis_client.get(text)
        if cached_questions:
            return jsonify(cached_questions)

        questions = mcq.generate_mcq_questions(text, count)

        # Cache the generated questions in Redis
        redis_client.set(text, jsonify([q.__dict__ for q in questions]), ex=REDIS_EXPIRY_TIME)

        result = [q.__dict__ for q in questions]
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
