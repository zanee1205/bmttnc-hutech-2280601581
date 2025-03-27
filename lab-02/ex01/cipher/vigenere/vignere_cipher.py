class VigenereCipher:
    @staticmethod
    def encrypt_text(plain_text, key):
        key = key.upper()
        encrypted_text = ""
        key_index = 0

        for char in plain_text:
            if char.isalpha():
                shift = ord(key[key_index]) - ord('A')
                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                key_index = (key_index + 1) % len(key)
            else:
                encrypted_text += char
        return encrypted_text

    @staticmethod
    def decrypt_text(cipher_text, key):
        key = key.upper()
        decrypted_text = ""
        key_index = 0

        for char in cipher_text:
            if char.isalpha():
                shift = ord(key[key_index]) - ord('A')
                if char.isupper():
                    decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                key_index = (key_index + 1) % len(key)
            else:
                decrypted_text += char
        return decrypted_text
