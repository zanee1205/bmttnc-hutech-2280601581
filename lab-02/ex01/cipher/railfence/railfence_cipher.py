class RailFenceCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        rail = [['\n' for _ in range(len(text))] for _ in range(key)]
        direction_down = False
        row, col = 0, 0

        for char in text:
            if row == 0 or row == key - 1:
                direction_down = not direction_down
            rail[row][col] = char
            col += 1
            row += 1 if direction_down else -1

        encrypted_text = []
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] != '\n':
                    encrypted_text.append(rail[i][j])

        return ''.join(encrypted_text)

    def decrypt(self, text, key):
        rail = [['\n' for _ in range(len(text))] for _ in range(key)]
        direction_down = None
        row, col = 0, 0

        # Mark the positions in the rail matrix
        for i in range(len(text)):
            if row == 0:
                direction_down = True
            if row == key - 1:
                direction_down = False
            rail[row][col] = '*'
            col += 1
            row += 1 if direction_down else -1

        # Fill the rail matrix with the characters from the text
        index = 0
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] == '*' and index < len(text):
                    rail[i][j] = text[index]
                    index += 1

        # Read the characters in a zigzag pattern
        decrypted_text = []
        row, col = 0, 0
        for i in range(len(text)):
            if row == 0:
                direction_down = True
            if row == key - 1:
                direction_down = False
            if rail[row][col] != '\n':
                decrypted_text.append(rail[row][col])
                col += 1
            row += 1 if direction_down else -1

        return ''.join(decrypted_text)