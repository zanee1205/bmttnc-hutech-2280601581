class PlayfairCipher:

    def __init__(self, key):
        if not key:
            raise ValueError("Key cannot be empty")
        self.matrix = self.create_playfair_matrix(key)

    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")
        key_set = []

        for char in key:
            if char.isalpha() and char not in key_set:
                key_set.append(char)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in key_set:
                key_set.append(char)

        return [key_set[i:i + 5] for i in range(0, 25, 5)]

    def find_letter_coords(self, letter):
        for row in range(5):
            if letter in self.matrix[row]:
                return row, self.matrix[row].index(letter)
        raise ValueError(f"Letter '{letter}' not found in matrix")

    def prepare_text(self, text):
        text = text.upper().replace("J", "I")
        text = ''.join(filter(str.isalpha, text))  
        prepared_text = ""
        i = 0

        while i < len(text):
            prepared_text += text[i]
            if i < len(text) - 1 and text[i] == text[i + 1]:
                prepared_text += "X"
            i += 1  

        if len(prepared_text) % 2 != 0:
            prepared_text += "X"

        return prepared_text

    def encrypt_text(self, plain_text):
        plain_text = self.prepare_text(plain_text)
        encrypted_text = ""

        for i in range(0, len(plain_text), 2):
            row1, col1 = self.find_letter_coords(plain_text[i])
            row2, col2 = self.find_letter_coords(plain_text[i + 1])

            if row1 == row2:  
                encrypted_text += self.matrix[row1][(col1 + 1) % 5] + self.matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  
                encrypted_text += self.matrix[(row1 + 1) % 5][col1] + self.matrix[(row2 + 1) % 5][col2]
            else:  
                encrypted_text += self.matrix[row1][col2] + self.matrix[row2][col1]

        return encrypted_text

    def decrypt_text(self, cipher_text):
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            row1, col1 = self.find_letter_coords(cipher_text[i])
            row2, col2 = self.find_letter_coords(cipher_text[i + 1])

            if row1 == row2:  
                decrypted_text += self.matrix[row1][(col1 - 1) % 5] + self.matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  
                decrypted_text += self.matrix[(row1 - 1) % 5][col1] + self.matrix[(row2 - 1) % 5][col2]
            else:  
                decrypted_text += self.matrix[row1][col2] + self.matrix[row2][col1]

        # Loại bỏ 'X' padding khi cần
        return decrypted_text.replace("X", "")

