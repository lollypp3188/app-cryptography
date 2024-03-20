from app import app
from flask import Flask, render_template, request, jsonify
from models.models import CaesarCipher



@app.route("/caesar", methods=['GET', 'POST'])
def caesar():
    if request.method == 'POST':
        text = request.form['text']
        offset = int(request.form['offset'])
        action = request.form['action']  

        if action == 'encrypt':
            result = CaesarCipher.encrypt(text, offset)
        elif action == 'decrypt':
            result = CaesarCipher.decrypt(text, offset)
        else:
            result = "Invalid action"

        return jsonify(result=result)
    else:
        return render_template("caesar.html")