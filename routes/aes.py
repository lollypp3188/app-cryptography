from app import app  
from flask import request, render_template, jsonify
from models.aes import AESCipher

@app.route('/aes', methods=['GET', 'POST'])
def aes():
    if request.method == 'GET':
        return render_template('aes.html')
    elif request.method == 'POST':
        try:
            action = request.form['action']
            key = request.form['key']
            
            aes_cipher = AESCipher(key.encode())
            
            if action == 'encrypt':
                plaintext = request.form['plaintext']
                encrypted_text = aes_cipher.encrypt(plaintext)
                return jsonify({'result': 'success', 'text': encrypted_text.hex()})
            elif action == 'decrypt':
                encrypted_text = bytes.fromhex(request.form['text'])
                decrypted_text = aes_cipher.decrypt(encrypted_text)
                return jsonify({'result': 'success', 'text': decrypted_text})
            else:
                return jsonify({'result': 'Invalid action'})
        except KeyError:
            return jsonify({'result': 'Key, action, or text not provided'})
        except Exception as e:
            return jsonify({'result': str(e)})