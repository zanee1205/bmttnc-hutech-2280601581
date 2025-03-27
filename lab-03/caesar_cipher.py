import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow  
import requests

class MyApp(QMainWindow):
    def __init__(self):  
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)  
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.plaintext_txt.toPlainText(),
            "key": self.ui.key_txt.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)  
            if response.status_code == 200:  
                data = response.json()
                self.ui.cipher_txt.setPlainText(data["encrypted_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API: ", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.cipher_txt.toPlainText(),
            "key": self.ui.key_txt.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)  # Fixed syntax here: 'requests.post'
            if response.status_code == 200:  # Corrected the comparison operator
                data = response.json()
                self.ui.plaintext_txt.setPlainText(data["decrypted_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API: ", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

if __name__ == "__main__":  # Fixed the if statement for main block
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
