import rsa
import os

class RSACipher:
    def __init__(self):
        self.public_key = None
        self.private_key = None
        self.key_path = "cipher/rsa/keys"  # Thư mục lưu khóa
        self.load_keys()  # Tải khóa nếu có sẵn

    def generate_keys(self):
        """Tạo cặp khóa RSA và lưu vào file"""
        public_key, private_key = rsa.newkeys(2048)
        
        # Đảm bảo thư mục tồn tại
        os.makedirs(self.key_path, exist_ok=True)

        # Lưu khóa
        with open(f"{self.key_path}/public.pem", "wb") as f:
            f.write(public_key.save_pkcs1("PEM"))
        with open(f"{self.key_path}/private.pem", "wb") as f:
            f.write(private_key.save_pkcs1("PEM"))

        # Cập nhật khóa vào class
        self.public_key, self.private_key = public_key, private_key
        
        return {"message": "Khóa RSA đã được tạo và lưu thành công"}

    def load_keys(self):
        """Tải khóa từ file nếu tồn tại"""
        try:
            with open(f"{self.key_path}/public.pem", "rb") as f:
                self.public_key = rsa.PublicKey.load_pkcs1(f.read())

            with open(f"{self.key_path}/private.pem", "rb") as f:
                self.private_key = rsa.PrivateKey.load_pkcs1(f.read())
        except FileNotFoundError:
            pass  # Không có khóa thì giữ nguyên None

    def encrypt(self, message):
        """Mã hóa một thông điệp bằng khóa công khai"""
        if not self.public_key:
            return {"error": "Khóa công khai chưa được tạo"}
        encrypted_message = rsa.encrypt(message.encode(), self.public_key)
        return {"encrypted_message": encrypted_message.hex()}

    def decrypt(self, ciphertext):
        """Giải mã một thông điệp bằng khóa riêng"""
        if not self.private_key:
            return {"error": "Khóa riêng chưa được tạo"}
        try:
            decrypted_message = rsa.decrypt(bytes.fromhex(ciphertext), self.private_key).decode()
            return {"decrypted_message": decrypted_message}
        except Exception:
            return {"error": "Giải mã thất bại"}

    def sign(self, message):
        """Ký một thông điệp bằng khóa riêng"""
        if not self.private_key:
            return {"error": "Khóa riêng chưa được tạo"}
        signature = rsa.sign(message.encode(), self.private_key, 'SHA-256')
        return {"signature": signature.hex()}

    def verify(self, message, signature):
        """Xác minh chữ ký bằng khóa công khai"""
        if not self.public_key:
            return {"error": "Khóa công khai chưa được tạo"}
        try:
            rsa.verify(message.encode(), bytes.fromhex(signature), self.public_key)
            return {"is_verified": True}
        except Exception:
            return {"is_verified": False}
