import base64

def main():
    input_string = input("Nhap thong tin can ma hoa: ")

    encodeded_bytes = base64.b64encode(input_string.encode("utf-8"))
    encodeded_string = encodeded_bytes.decode(("utf-8"))

    with open("data.txt", "w") as file:
        file.write(encodeded_string)

    print("Da ma hoa va ghi vao tep data.txt")

if __name__ == "__main__":
    main()