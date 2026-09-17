class XeOto:
    so_banh_xe = 4

xe_vinfast = XeOto()

print(xe_vinfast.so_banh_xe)

XeOto.so_banh_xe = 3 

print (xe_vinfast.so_banh_xe)