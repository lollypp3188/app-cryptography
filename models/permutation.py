class PermutationCipher():
    def __init__(self, permutation):
        """
        Initialize the permutation cipher with a given permutation.

        :param permutation: A list of integers representing the permutation.
        """
        if len(permutation) < 1 or not all(0 <= i < len(permutation) for i in permutation):
            raise ValueError("Invalid permutation")
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
                if index < 0 or index >= len(self.permutation):
                    raise ValueError("Invalid character in plaintext")
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
                if index < 0 or index >=len(self.inverse_permutation):
                    raise ValueError("Invalid character in ciphertext")
                decrypted_char = chr(self.inverse_permutation[index] + offset)
                plaintext += decrypted_char
            else:
                plaintext += char
        return plaintext