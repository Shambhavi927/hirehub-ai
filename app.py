from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

@app.route('/match', methods=['POST'])
def match_candidate():
    data = request.json
    candidate_skills = data['candidateSkills']
    job_skills = data['jobSkills']
    
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([candidate_skills, job_skills])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    percentage = round(score * 100, 2)
    
    return jsonify({
        'matchScore': percentage,
        'candidateSkills': candidate_skills,
        'jobSkills': job_skills
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'AI service is running'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001, debug=True)
