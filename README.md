# HireHub AI - Candidate Matching Service

AI powered candidate matching microservice built with Python Flask and Scikit-learn.

## Tech Stack
- Python 3.13
- Flask
- Scikit-learn
- NumPy
- Pandas

## Features
- TF-IDF vectorization of candidate and job skills
- Cosine similarity matching algorithm
- Returns match score as a percentage
- REST API endpoint for integration with Spring Boot

## How it Works
1. Candidate skills and job skills are sent as text
2. TF-IDF converts text into numerical vectors
3. Cosine similarity calculates how similar the two vectors are
4. Returns a match percentage score

## How to Run
1. Create virtual environment: python3 -m venv venv
2. Activate: source venv/bin/activate
3. Install dependencies: pip install -r requirements.txt
4. Run: python3 app.py
5. Service runs on port 5001
