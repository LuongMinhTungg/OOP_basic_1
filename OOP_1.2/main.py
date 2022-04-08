from Bill import Management_Bill
from Product import Management_Pro
from Customer import Management_Cus
import datetime
check = True
MP = Management_Pro()
MC = Management_Cus()
MB = Management_Bill()
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
            MP.Add_Pro()
        if key == 2:
            MP.Show_Pro(MP.Get_list_Pro())
        if key == 3: 
            MC.Add_Cus()
        if key == 4: 
            MC.Show_Cus(MC.Get_list_Cus())
        if key == 5:
            cus = input('Nhap ten KH: ')
            pro = input('Nhap ten sp muon mua hang: ')
            MB.Sell(cus, pro)
        if key == 6: 
            cus = input('Nhap ten kh muon xem hoa don: ')
            MB.Show_Bill(cus)
        if key == 7:
            MB.Sort()
            MB.Selled()
        if key == 100:
            check = False
    
        


