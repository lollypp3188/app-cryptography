from app import app
from flask import Flask, render_template, request, jsonify
from models.vigenere import VigenereCipher


@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    if request.method == 'POST':
        key = request.form['key']
        text = request.form['text']
        action = request.form['action']

        if not key:
            return jsonify(error="Key cannot be empty")
        if not text:
            return jsonify(error="Text cannot be empty")

        if action == 'encrypt':
            result = VigenereCipher.encrypt(key, text)
        elif action == 'decrypt':
            result = VigenereCipher.decrypt(key, text)
        else:
            return jsonify(error="Invalid action")

        return jsonify(result=result)

    return render_template('vigenere.html')