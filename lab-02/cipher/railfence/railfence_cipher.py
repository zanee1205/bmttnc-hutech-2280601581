class RailFenceCipher:
    def encrypt_text(self, text, key):
        # Kiểm tra key hợp lệ (key phải >= 2)
        if key < 2:
            return text  # Nếu key nhỏ hơn 2, không thực hiện mã hóa

        # Khởi tạo danh sách rail với key dòng, mỗi dòng là chuỗi rỗng
        rail = [''] * key
        row = 0
        step = 1

        # Duyệt từng ký tự trong text và phân bổ theo pattern "zigzag"
        for char in text:
            rail[row] += char
            row += step
            # Khi đạt đầu hoặc cuối, đổi hướng
            if row == 0 or row == key - 1:
                step = -step

        return ''.join(rail)

    def decrypt_text(self, text, key):
        if key < 2:
            return text

        n = len(text)
        # Xác định vị trí (dòng) của từng ký tự trong bản mã hóa
        pattern = [0] * n
        row = 0
        step = 1
        for i in range(n):
            pattern[i] = row
            row += step
            if row == 0 or row == key - 1:
                step = -step

        # Sắp xếp các chỉ số theo thứ tự dòng để xác định thứ tự ký tự ban đầu
        pos = [None] * n
        index = 0
        for r in range(key):
            for i in range(n):
                if pattern[i] == r:
                    pos[i] = index
                    index += 1

        # Lấy thứ tự ký tự theo vị trí đã sắp xếp
        # Giả sử bản mã hóa được tạo bằng cách nối các ký tự theo thứ tự hàng,
        # ta sẽ chia text thành các phần tương ứng với số ký tự mỗi dòng.
        # Sau đó, ghép lại theo thứ tự ban đầu.
        rail_lengths = [pattern.count(r) for r in range(key)]
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(text[start:start+length]))
            start += length

        # Tái tạo chuỗi gốc theo vị trí ban đầu
        decrypted = []
        rail_indices = [0] * key
        for r in pattern:
            decrypted.append(rails[r][rail_indices[r]])
            rail_indices[r] += 1

        return ''.join(decrypted)
