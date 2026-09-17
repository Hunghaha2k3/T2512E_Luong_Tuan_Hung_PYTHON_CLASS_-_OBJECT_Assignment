# Hãy viết một class HinhChuNhat gồm:
# Constructor nhận vào chieu_dai và chieu_rong.
# Một phương thức tinh_dien_tich() trả về diện tích hình chữ nhật.
class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

#Tạo hai đối tượng: hcn_1 (dài 5, rộng 3) và hcn_2 (dài 10, rộng 4).
hcn_1 = HinhChuNhat(5,3)
hcn_2 = HinhChuNhat(10,4)

#Gọi phương thức tinh_dien_tich() cho cả hai đối tượng và in kết quả ra màn hình.
print(f"Diện tích Hình chữ nhật 1: {hcn_1.tinh_dien_tich()}")
print(f"Diện tích Hình chữ nhật 2: {hcn_2.tinh_dien_tich()}")



