from app import app  # Make sure you have the app instance defined in app.py
from flask import request, render_template, jsonify
from models.des import TripleDES

@app.route('/des', methods=['GET', 'POST'])
def des():
    if request.method == 'POST':
        try:
            key = request.form['key']
            text = request.form['text']
            action = request.form['action']

            if not key or not text or not action:
                return jsonify(result="Missing form data: key, text, or action")

            des = TripleDES(key)
            if action == 'encrypt':
                encrypted_text = des.encrypt(text)
                return jsonify(result=encrypted_text)
            elif action == 'decrypt':
                decrypted_text = des.decrypt(text)
                return jsonify(result=decrypted_text)
            else:
                return jsonify(result="Invalid action specified")
        except ValueError as e:
            return jsonify(result=str(e))
        except Exception as e:
            return jsonify(result="An unexpected error occurred: {}".format(str(e)))

    return render_template('des.html')
