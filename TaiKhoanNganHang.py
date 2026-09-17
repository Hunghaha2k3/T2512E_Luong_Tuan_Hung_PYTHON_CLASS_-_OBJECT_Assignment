class TaiKhoanNganHang:
    def __init__(self, chu_tai_khoan, so_du):
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du 

    def nap_tien(self, so_tien):
        if (so_tien <= 0):
            print(f"Loi!! So tien khong hop le")
        else: 
            self.so_du += so_tien
        
    def xem_so_du(self):
        print(f"So du hien tai la : {self.so_du}")  


