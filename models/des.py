from Crypto.Cipher import DES3
import base64

class TripleDES:
    def __init__(self, key):
        if len(key) != 16 and len(key) != 24:
            raise ValueError("Key length must be either 16 or 24 bytes.")
        self.key = key

    def pad(self, s):
        BS = DES3.block_size
        padding_len = BS - len(s) % BS
        return s + bytes([padding_len] * padding_len)

    def unpad(self, s):
        return s[:-s[-1]]

    def encrypt(self, text):
        text = self.pad(text.encode('utf-8'))
        cipher = DES3.new(self.key, DES3.MODE_ECB)
        encrypted_text = cipher.encrypt(text)
        return base64.b64encode(encrypted_text).decode('utf-8')

    def decrypt(self, encrypted_text):
        encrypted_text = base64.b64decode(encrypted_text)
        cipher = DES3.new(self.key, DES3.MODE_ECB)
        decrypted_text = cipher.decrypt(encrypted_text)
        return self.unpad(decrypted_text).decode('utf-8')
