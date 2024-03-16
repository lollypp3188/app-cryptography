from framework.models import Model


class CaesarCipher(Model):


    @staticmethod
    def encrypt(string, key_a, key_b):
        result = ""
        for char in string:
            if char == " ":
                result += " "
                continue
            if char.islower():
                result += chr(((ord(char) - 97) * key_a + key_b) % 26 + 97)
            elif char.isupper():
                result += chr(((ord(char) - 65) * key_a + key_b) % 26 + 65)
            else:
                result += char
        return result

    
    @staticmethod
    def decrypt(string, key_a, key_b):
        result = ""
        for char in string:
            if char == " ":
                result += " "
                continue
            if char.islower():
                mod_result = CaesarCipher.mod(key_a, 26)
                if mod_result is None:
                
                    result += char
                else:
                    result += chr(((ord(char) - 97 - key_b) * mod_result) % 26 + 97)
            elif char.isupper():
                mod_result = CaesarCipher.mod(key_a, 26)
                if mod_result is None:
                
                    result += char
                else:
                    result += chr(((ord(char) - 65 - key_b) * mod_result) % 26 + 65)
            else:
                result += char
        return result

      

  
    @staticmethod
    def mod(a, m): 
        return next((x for x in range(1, m) if (a * x) % m == 1), None)


