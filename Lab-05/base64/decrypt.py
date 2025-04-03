import base64

def main():
    try:
        with open("data.txt", "r") as file:
            encodeded_string = file.read().strip()

        decoded_bytes = base64.b64decode(encodeded_string)
        decoded_string = decoded_bytes.decode("utf-8")

        print("Chuoi sau khi giai ma: ", decoded_string)
    except Exception as e:
        print("Loi: ", e) 

if __name__ == "__main__":
    main()