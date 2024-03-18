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



class PermutationCipher(Model):
    def __init__(self, permutation):
        """
        Initialize the permutation cipher with a given permutation.

        :param permutation: A list of integers representing the permutation.
        """
        self.permutation = permutation
        self.inverse_permutation = [0] * len(permutation)
        for i, j in enumerate(permutation):
            self.inverse_permutation[j] = i

    def encrypt(self, plaintext):
        """
        Encrypt a given plaintext using the permutation.

        :param plaintext: A string representing the plaintext.
        :return: A string representing the ciphertext.
        """
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                offset = ord('a') if char.islower() else ord('A')
                index = ord(char) - offset
                encrypted_char = chr(self.permutation[index] + offset)
                ciphertext += encrypted_char
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        """
        Decrypt a given ciphertext using the inverse permutation.

        :param ciphertext: A string representing the ciphertext.
        :return: A string representing the plaintext.
        """
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                offset = ord('a') if char.islower() else ord('A')
                index = ord(char) - offset
                decrypted_char = chr(self.inverse_permutation[index] + offset)
                plaintext += decrypted_char
            else:
                plaintext += char
        return plaintext
