from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher

app = Flask(__name__)

# Khởi tạo đối tượng Cipher
Caesar = CaesarCipher()
Vigenere = VigenereCipher()
RailFence = RailFenceCipher()
Playfair = PlayfairCipher()

# Trang chủ
@app.route("/")
def home():
    return render_template("index.html")

# Caesar Cipher Routes
@app.route("/caesar", methods=["GET", "POST"])
def caesar():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        key = int(request.form["shift"])
        action = request.form["action"]

        if action == "encrypt":
            result = Caesar.encrypt_text(text, key)
        elif action == "decrypt":
            result = Caesar.decrypt_text(text, key)

    return render_template("caesar.html", result=result)

# Vigenere Cipher Routes
@app.route("/vigenere", methods=["GET", "POST"])
def vigenere():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["vigenere_key"]
        action = request.form["action"]

        if action == "encrypt":
            result = Vigenere.encrypt_text(text, key)
        elif action == "decrypt":
            result = Vigenere.decrypt_text(text, key)

    return render_template("vigenere.html", result=result)

# Playfair Cipher Routes
@app.route("/playfair", methods=["GET", "POST"])
def playfair():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["playfair_key"]
        action = request.form["action"]
        
        matrix = Playfair.create_playfair_matrix(key)
        
        if action == "encrypt":
            result = Playfair.encrypt_text(text, matrix)
        elif action == "decrypt":
            result = Playfair.decrypt_text(text, matrix)
    
    return render_template("playfair.html", result=result)

# Chạy server Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)