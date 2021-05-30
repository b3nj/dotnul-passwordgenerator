from flask import Flask, jsonify
from flask_cors import CORS
import string
import secrets

app = Flask(__name__)
CORS(app)

@app.route('/api/password')
def pwgen():
    answer = {}
    alphabetfull = string.punctuation + string.ascii_letters + string.digits
    alphabet = string.ascii_letters + string.digits
    for pwlen in [8, 12, 16, 20, 24]:
        answer["complex_"+str(pwlen)] = ''.join(secrets.choice(alphabetfull) for i in range(pwlen))
        answer["alphanum_"+str(pwlen)] = ''.join(secrets.choice(alphabet) for i in range(pwlen))
    return jsonify(answer)
