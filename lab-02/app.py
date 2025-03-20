from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher


app = Flask(__name__)

# Khởi tạo đối tượng Cipher
Caesar = CaesarCipher()
Vigenere = VigenereCipher()

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

@app.route('/vigenere_encrypt', methods=['POST'])
def vigenere_encrypt():
    text = request.form['plain_text']
    key = request.form['vigenere_key']
    encrypted_text = Vigenere.encrypt_text(text, key)
    return render_template('vigenere.html', encrypted_text=encrypted_text, plain_text=text, vigenere_key=key)

@app.route('/vigenere_decrypt', methods=['POST'])
def vigenere_decrypt():
    text = request.form['cipher_text']
    key = request.form['vigenere_key']
    decrypted_text = Vigenere.decrypt_text(text, key)
    return render_template('vigenere.html', decrypted_text=decrypted_text, cipher_text=text, vigenere_key=key)

# Trang Rail Fence Cipher
@app.route("/railfence")
def rail_fence():
    return render_template("railfence.html")


@app.route("/rail_fence_encrypt", methods=["POST"])
def rail_fence_encrypt():
    text = request.form["plain_text"]
    key = int(request.form["rail_fence_key"])
    rail_fence = RailFenceCipher()
    encrypted_text = rail_fence.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/rail_fence_decrypt", methods=["POST"])
def rail_fence_decrypt():
    text = request.form["cipher_text"]
    key = int(request.form["rail_fence_key"])
    rail_fence = RailFenceCipher()
    decrypted_text = rail_fence.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Chạy server Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
