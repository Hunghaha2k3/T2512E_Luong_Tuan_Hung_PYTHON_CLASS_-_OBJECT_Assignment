class NhanVien:
    cong_ty = "TechCorp"
    def __init__(self, ten, luong):
        self.ten = ten
        self.luong = luong

    def __str__(self):
        return f"Ten nhan vien {self.ten} | Luong: {self.luong} | Cong ty: {NhanVien.cong_ty}"
