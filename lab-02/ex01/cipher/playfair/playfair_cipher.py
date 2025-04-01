class PlayfairCipher:
    def __init__(self):
        pass

    def generate_key_matrix(self, key):
        key = key.upper().replace("J", "I")  # Thay 'J' bằng 'I'
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key_matrix = []
        used_chars = set()

        # Thêm key vào matrix
        for char in key:
            if char not in used_chars and char in alphabet:
                key_matrix.append(char)
                used_chars.add(char)

        # Thêm các ký tự còn lại
        for char in alphabet:
            if char not in used_chars:
                key_matrix.append(char)

        # Chuyển thành ma trận 5x5
        return [key_matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_position(self, char, key_matrix):
        for row in range(5):
            for col in range(5):
                if key_matrix[row][col] == char:
                    return row, col
        return None

    def preprocess_text(self, text):
        text = text.upper().replace("J", "I").replace(" ", "")
        processed_text = ""
        i = 0

        while i < len(text):
            char1 = text[i]
            char2 = text[i + 1] if i + 1 < len(text) else "X"

            if char1 == char2:  # Nếu hai chữ giống nhau, chèn 'X' vào giữa
                processed_text += char1 + "X"
                i += 1
            else:
                processed_text += char1 + char2
                i += 2

        if len(processed_text) % 2 != 0:
            processed_text += "X"  # Nếu số ký tự lẻ, thêm 'X' vào cuối

        return processed_text

    def encrypt(self, text, key):
        key_matrix = self.generate_key_matrix(key)
        text = self.preprocess_text(text)
        encrypted_text = ""

        i = 0
        while i < len(text):
            char1, char2 = text[i], text[i + 1]
            row1, col1 = self.find_position(char1, key_matrix)
            row2, col2 = self.find_position(char2, key_matrix)

            if row1 == row2:  # Cùng hàng, lấy ký tự bên phải
                encrypted_text += key_matrix[row1][(col1 + 1) % 5]
                encrypted_text += key_matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột, lấy ký tự bên dưới
                encrypted_text += key_matrix[(row1 + 1) % 5][col1]
                encrypted_text += key_matrix[(row2 + 1) % 5][col2]
            else:  # Hình chữ nhật, đổi chéo góc
                encrypted_text += key_matrix[row1][col2]
                encrypted_text += key_matrix[row2][col1]

            i += 2

        return encrypted_text

    def decrypt(self, text, key):
        key_matrix = self.generate_key_matrix(key)
        text = text.upper().replace(" ", "")
        decrypted_text = ""

        i = 0
        while i < len(text):
            char1, char2 = text[i], text[i + 1]
            row1, col1 = self.find_position(char1, key_matrix)
            row2, col2 = self.find_position(char2, key_matrix)

            if row1 == row2:  # Cùng hàng, lấy ký tự bên trái
                decrypted_text += key_matrix[row1][(col1 - 1) % 5]
                decrypted_text += key_matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột, lấy ký tự bên trên
                decrypted_text += key_matrix[(row1 - 1) % 5][col1]
                decrypted_text += key_matrix[(row2 - 1) % 5][col2]
            else:  # Hình chữ nhật, đổi chéo góc
                decrypted_text += key_matrix[row1][col2]
                decrypted_text += key_matrix[row2][col1]

            i += 2

        return decrypted_text


# **Test mã hóa và giải mã**
if __name__ == "__main__":
    cipher = PlayfairCipher()
    
    # Test Case 1
    plain_text = "HELLO WORLD"
    key = "KEYWORD"
    encrypted = cipher.encrypt(plain_text, key)
    decrypted = cipher.decrypt(encrypted, key)

    print(f"Plain Text  : {plain_text}")
    print(f"Key         : {key}")
    print(f"Encrypted   : {encrypted}")
    print(f"Decrypted   : {decrypted}")
