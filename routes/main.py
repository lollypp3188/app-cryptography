from app import app
from flask import Flask, render_template, request, jsonify
from models.models import CaesarCipher



@app.route("/")
def main():
    return render_template("index.html")






