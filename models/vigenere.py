class VigenereCipher:
    """
    A class to perform Vigenere encryption and decryption.

    Attributes:
        None
    """

    @staticmethod
    def encrypt(key, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher with the provided key.

        Args:
            key (str): The key for encryption.
            plaintext (str): The plaintext to be encrypted.

        Returns:
            str: The encrypted ciphertext.

        Raises:
            ValueError: If the key is empty.
        """
        original_plaintext = plaintext
        plaintext = plaintext.upper().replace(" ", "")
        key = key.upper().replace(" ", "")
        cipher = ""
        
        if not key:
            raise ValueError("Key cannot be empty")
        
        for i, char in enumerate(plaintext):
            shift = ord(key[i % len(key)]) - 65
            new_val = ord(char) - 65
            update = (shift + new_val) % 26
            cipher += chr(update + 65)
        
        return cipher

    @staticmethod
    def decrypt(key, ciphertext):
        """
        Decrypts the ciphertext using the Vigenere cipher with the provided key.

        Args:
            key (str): The key for decryption.
            ciphertext (str): The ciphertext to be decrypted.

        Returns:
            str: The decrypted plaintext.

        Raises:
            ValueError: If the key is empty.
        """
        original_ciphertext = ciphertext
        ciphertext = ciphertext.upper().replace(" ", "")
        key = key.upper().replace(" ", "")
        plaintext = ""
        
        if not key:
            raise ValueError("Key cannot be empty")
        
        for i, char in enumerate(ciphertext):
            shift = ord(key[i % len(key)]) - 65
            new_val = ord(char) - 65
            update = (new_val - shift) % 26
            plaintext += chr(update + 65)
        
        return plaintext