import sys
import os
sys.path.append(os.path.abspath('lab-03'))
import subprocess

from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayfairCipher
from cipher.railfence import RailFenceCipher

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template('index.html')

# Caesar Cipher
@app.route("/caesar")
def caesar():
    filename = request.args.get("file", "caesar_cipher.py")  # Mặc định chạy script.py nếu không có file

    # Định nghĩa đường dẫn thư mục chứa file
    script_dir = r"C:\Users\Zanee\bmttnc-hutech-2280601581\lab-03"
    
    # Ghép đường dẫn đúng
    script_path = os.path.join(script_dir, filename)

    # Kiểm tra file có tồn tại không
    if not os.path.isfile(script_path):
        return f"File {script_path} không tồn tại!", 404

    # Chạy file Python
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    return render_template('index.html')

@app.route("/vigenere")
def vigenere():
    filename = request.args.get("file", "vigenere_cipher.py")  # Mặc định chạy script.py nếu không có file

    # Định nghĩa đường dẫn thư mục chứa file
    script_dir = r"C:\Users\Zanee\bmttnc-hutech-2280601581\lab-03"
    
    # Ghép đường dẫn đúng
    script_path = os.path.join(script_dir, filename)

    # Kiểm tra file có tồn tại không
    if not os.path.isfile(script_path):
        return f"File {script_path} không tồn tại!", 404

    # Chạy file Python
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    return render_template('index.html')

@app.route("/railfence")
def railfence():
    filename = request.args.get("file", "railfence_cipher.py")  # Mặc định chạy script.py nếu không có file

    # Định nghĩa đường dẫn thư mục chứa file
    script_dir = r"C:\Users\Zanee\bmttnc-hutech-2280601581\lab-03"
    
    # Ghép đường dẫn đúng
    script_path = os.path.join(script_dir, filename)

    # Kiểm tra file có tồn tại không
    if not os.path.isfile(script_path):
        return f"File {script_path} không tồn tại!", 404

    # Chạy file Python
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    return render_template('index.html')

@app.route("/playfair")
def playfair():
    filename = request.args.get("file", "playfair_cipher.py")  # Mặc định chạy script.py nếu không có file

    # Định nghĩa đường dẫn thư mục chứa file
    script_dir = r"C:\Users\Zanee\bmttnc-hutech-2280601581\lab-03"
    
    # Ghép đường dẫn đúng
    script_path = os.path.join(script_dir, filename)

    # Kiểm tra file có tồn tại không
    if not os.path.isfile(script_path):
        return f"File {script_path} không tồn tại!", 404

    # Chạy file Python
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    return render_template('index.html')


# Run Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
