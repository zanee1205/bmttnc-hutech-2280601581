import ecdsa
import os

# Tạo thư mục lưu trữ khóa nếu chưa tồn tại
key_dir = 'cipher/ecc/keys'
if not os.path.exists(key_dir):
    os.makedirs(key_dir)

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        # Tạo khóa riêng tư
        sk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)
        vk = sk.get_verifying_key()  # Lấy khóa công khai từ khóa riêng tư

        # Lưu khóa riêng tư
        with open(f'{key_dir}/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())

        # Lưu khóa công khai
        with open(f'{key_dir}/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        # Tải khóa riêng tư
        with open(f'{key_dir}/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        # Tải khóa công khai
        with open(f'{key_dir}/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())

        return sk, vk

    def sign(self, message, key):
        # Ký dữ liệu bằng khóa riêng tư
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        _, vk = self.load_keys()  # Load khóa công khai
        try:
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False
