from app import app
from flask import render_template, request
from models.playfair import PlayfairSquare, MODE_IJSWAP, MODE_NOQ


@app.route('/playfair', methods=['GET', 'POST'])
def playfair():
    if request.method == 'POST':
        keyword = request.form['keyword']
        message = request.form['message']
        mode = request.form['mode']
        
        # Create PlayfairSquare object based on mode
        if mode == 'MODE_IJSWAP':
            square = PlayfairSquare(keyword, mode=MODE_IJSWAP)
        else:
            square = PlayfairSquare(keyword)
        
        # Check if encryption or decryption is requested
        if 'encrypt_button' in request.form:
            result = square.encrypt(message)
        elif 'decrypt_button' in request.form:
            result = square.decrypt(message)
        
        return render_template('playfair.html', result=result)

    # Render the playfair.html template for GET requests
    return render_template('playfair.html', result=None)
