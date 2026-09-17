

from TaiKhoanNganHang import TaiKhoanNganHang


if __name__ == "__main__":
    acc1 = TaiKhoanNganHang("Nguyen Van A", 10000)
    acc2 = TaiKhoanNganHang("Nguyen Van B", 20000)
    acc1.nap_tien(20000)
    acc2.nap_tien(15000)
    print(f"So du tk1: acc1.xem_so_du()")
    print(f"So du tk2: acc2.xem_so_du()")
