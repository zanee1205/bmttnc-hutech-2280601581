class RailFenceCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        rail = [['\n' for _ in range(len(text))] for _ in range(self.key)]
        
        direction_down = False
        row, col = 0, 0
        
        for char in text:
            if row == 0 or row == self.key - 1:
                direction_down = not direction_down
            
            rail[row][col] = char
            col += 1
            row += 1 if direction_down else -1
        
        return ''.join([''.join(row) for row in rail if row])
    
    def decrypt(self, cipher):
        rail = [['\n' for _ in range(len(cipher))] for _ in range(self.key)]
        
        direction_down = None
        row, col = 0, 0
        
        for _ in cipher:
            if row == 0:
                direction_down = True
            elif row == self.key - 1:
                direction_down = False
            
            rail[row][col] = '*'
            col += 1
            row += 1 if direction_down else -1
        
        index = 0
        for i in range(self.key):
            for j in range(len(cipher)):
                if rail[i][j] == '*' and index < len(cipher):
                    rail[i][j] = cipher[index]
                    index += 1
        
        result = []
        row, col = 0, 0
        for _ in range(len(cipher)):
            if row == 0:
                direction_down = True
            elif row == self.key - 1:
                direction_down = False
            
            result.append(rail[row][col])
            col += 1
            row += 1 if direction_down else -1
        
        return ''.join(result)
