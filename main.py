
from TaiKhoanNganHang import TaiKhoanNganHang
from python_class.Nhan_vien import NhanVien


if __name__ == "__main__":
    acc1 = TaiKhoanNganHang("Nguyen Van A", 10000)
    acc2 = TaiKhoanNganHang("Nguyen Van B", 20000)
    acc1.nap_tien(20000)
    acc2.nap_tien(15000)
    print(f"So du tk1: acc1.xem_so_du()")
    print(f"So du tk2: acc2.xem_so_du()")

    nv1 = NhanVien("Luong Hung", 10)
    print(f"{nv1.__str__()}")

    nv2 = NhanVien("Ngo Nam", 15)
    print(f"{nv2.__str__()}")
