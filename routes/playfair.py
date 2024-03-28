from app import app
from flask import render_template, request, jsonify
from models.playfair import PlayfairSquare, MODE_IJSWAP, MODE_NOQ


@app.route('/playfair', methods=['GET', 'POST'])
def playfair():
    if request.method == 'POST':
        keyword = request.form['keyword']
        message = request.form['text']
        mode = request.form['mode']
        
        # Create PlayfairSquare object based on mode
        if mode == 'MODE_IJSWAP':
            square = PlayfairSquare(keyword, mode=MODE_IJSWAP)
        else:
            square = PlayfairSquare(keyword)
        
        action = request.form['action']
        if action == 'encrypt':
            result = square.encrypt(message)
        elif action == 'decrypt':
            result = square.decrypt(message)
        else:
            result = "Invalid action"
        
        # return render_template('playfair.html', result=result)
        return jsonify(result=result)

    # Render the playfair.html template for GET requests
    return render_template('playfair.html', result=None)
