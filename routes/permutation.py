from app import app
from flask import Flask, render_template, request, jsonify
from models.models import PermutationCipher




@app.route("/permutation", methods=['GET', 'POST'])
def permutation():
    if request.method == 'POST':
        text = request.form['text']
        permutation = list(map(int, request.form['permutation'].split(',')))
        cipher = PermutationCipher(permutation)

        action = request.form['action']
        if action == 'encrypt':
            result = cipher.encrypt(text)
        elif action == 'decrypt':
            result = cipher.decrypt(text)
        else:
            result = "Invalid action"

        return jsonify(result=result)
    else:
        return render_template("permutation.html")




