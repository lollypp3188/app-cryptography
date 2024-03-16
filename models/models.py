from framework.models import Model


class CaesarCipher(Model):


    @staticmethod
    def encrypt(text, shift):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                else:
                    encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += char
        return encrypted_text

    @staticmethod
    def decrypt(text, shift):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                else:
                    decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_text += char
        return decrypted_text
