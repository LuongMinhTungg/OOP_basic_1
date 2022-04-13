from Bill import ManagementBill
from Product import ManagementPro
from Customer import ManagementCus
import datetime
check = True
MP = ManagementPro()
MC = ManagementCus()
MB = ManagementBill()
while check:
    try:
        print('---')
        print('1 - nhap san pham')
        print('2 - hien thi ds sp')
        print('3 - nhap khach hang')
        print('4 - xuat thong tin kh')
        print('5 - mua san pham')
        print('6 - xem hoa don')
        print('7 - danh san pham da ban')
        print('---')
        key = int(input('Nhap tuy chon: '))
    except ValueError:
        check = True
    else:
        if key == 1:
            MP.add_pro()
        if key == 2:
            MP.Show_Pro(MP.GetlistPro())
        if key == 3:
            MC.add_cus()
        if key == 4:
            MC.show_cus(MC.get_list_cus())
        if key == 5:
            cus = input('Nhap ten KH: ')
            pro = input('Nhap ten sp muon mua hang: ')
            MB.sell(cus, pro)
        if key == 6: 
            cus = input('Nhap ten kh muon xem hoa don: ')
            MB.show_bill(cus)
        if key == 7:
            MB.sort()
            MB.selled()
        if key == 100:
            check = False
    
        


