so_gio_lam = float(input("Nhap gio lam"))
luong_gio = float(input("Nhap thu lao moi gio"))
gio_tieu_chuan = 44 
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"so tien thuc linh:{thuc_linh}")