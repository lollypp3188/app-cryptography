import string


MODE_NOQ = "MODE_NOQ"
MODE_IJSWAP = "MODE_IJSWAP"


class PlayfairSquare:

    def __init__(self, keyword, mode=MODE_NOQ):
        self.square = []
        self.mode = mode
        self.build_translation_tables(keyword)
        self.build_square(PlayfairSquare.build_alphabet(keyword))

    def __str__(self):
        line = ""
        for row in range(0, 5):
            for column in range(0, 5):
                line += self.square[row][column] + " "
            line += "\n"
        return line

    def build_translation_tables(self, keyword):
        raw = "".join(string.ascii_uppercase)
        ciphered = "".join(PlayfairSquare.build_alphabet(keyword))
        self.cipher_transtable = str.maketrans(raw, ciphered)
        self.decipher_transtable = str.maketrans(ciphered, raw)

    def raw_to_ciphered(self, message):
        return message.upper().translate(self.cipher_transtable)

    def ciphered_to_raw(self, message):
        return message.upper().translate(self.decipher_transtable)

    @staticmethod
    def build_alphabet(keyword):
        alphabet = keyword.upper() + string.ascii_uppercase
        return [x for i, x in enumerate(alphabet) if x not in alphabet[:i]]

    def build_square(self, alphabet):
        self.square = []
        count = 0
        if self.mode == MODE_NOQ:
            alphabet.remove('Q')
        elif self.mode == MODE_IJSWAP:
            alphabet.remove('J')
        for y in range(0, 5):
            self.square.append([x for i, x in enumerate(alphabet) \
                                if i >= y * 5 and i < (y + 1) * 5])

        # Now build a lookup table for performance
        self.build_lookup_table()

    def build_lookup_table(self):
        self.lookup = {}
        for row in range(0, 5):
            for column in range(0, 5):
                self.lookup[self.square[row][column]] = (row, column)

    def get_column(self, letter):
        return self.lookup[letter][1]

    def get_row(self, letter):
        return self.lookup[letter][0]

    def cipher_pair(self, pair):
        return self.translate_pair(pair, 1)

    def decipher_pair(self, pair):
        return self.translate_pair(pair, -1)

    # 1 for ciphering, -1 for solving
    def translate_pair(self, pair, ciphering=1):
        # Assuming they cannot be the same
        result = ""
        i = 0
        for letter in pair:
            other = pair[(i + 1) % 2]
            # On same column, so slide downward
            if self.get_column(letter) == self.get_column(other):
                result += self.slide_row(letter, ciphering)
            # On same row, so slide to the right
            elif self.get_row(letter) == self.get_row(other):
                result += self.slide_column(letter, ciphering)
            else:
                result += self.square[self.get_row(other)] \
                    [self.get_column(letter)]
            i += 1
        return result

    def slide_row(self, letter, step):
        column = self.get_column(letter)
        row = self.get_row(letter) + step
        if row >= 5:
            row = 0
        elif row < 0:
            row = 4
        return self.square[row][column]

    def slide_column(self, letter, step):
        column = self.get_column(letter) + step
        row = self.get_row(letter)
        if column >= 5:
            column = 0
        elif column < 0:
            column = 4
        return self.square[row][column]

    def prepare_message(self, raw):
        cleaned = ""
        for letter in raw:
            if self.mode == MODE_NOQ and letter in ["q", "Q"]:
                continue
            elif self.mode == MODE_IJSWAP and \
                    letter in ["j", "J"]:
                letter = "i"

            if letter.isalpha():
                cleaned += letter

        cleaned = cleaned.upper()
        i = 0
        pairs = []
        while(i < len(cleaned)):
            if i + 1 >= len(cleaned):
                cleaned = cleaned + "X"
            elif cleaned[i] == cleaned[i + 1]:
                cleaned = cleaned[:i + 1] + "X" + cleaned[i + 1:]
            pairs.append(cleaned[i] + cleaned[i + 1])
            i += 2
        return " ".join(pairs)

    def encrypt(self, message):
        message = self.prepare_message(message)
        result = ""
        for pair in message.split(" "):
            result += self.cipher_pair(pair) + " "
        return result

    def decrypt(self, message):
        result = ""
        for pair in message.split(" "):
            result += self.decipher_pair(pair)
        return result



