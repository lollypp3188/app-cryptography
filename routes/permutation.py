from app import app
from flask import Flask, render_template, request, jsonify
from models.models import PermutationCipher


@app.route("/permutation")
def permutation():
    return render_template("permutation.html")

