def kiem_tra_so_nguyen_to(n):
    # Kiểm tra nếu n nhỏ hơn hoặc bằng 1 thì không phải là số nguyên tố
    if n <= 1:
        return False

    # Kiểm tra các số chia n từ 2 đến căn bậc 2 của n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Nếu tìm thấy ước, n không phải là số nguyên tố

    return True  # Nếu không có ước, n là số nguyên tố

# Kiểm tra số nguyên tố và in kết quả
number = int(input("Nhập vào số cần kiểm tra: "))

if kiem_tra_so_nguyen_to(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "không phải là số nguyên tố.")
