from tkinter import Tk
from Customer import Management_Cus
from Account import Saving_Acc,Current_Acc,Management_Acc
MC = Management_Cus()
CA = Current_Acc()
SA = Saving_Acc()
MA = Management_Acc()
check = True
while check:
    try:
        print('---')
        print('1-nhap tai khoan')
        print('2-thong tin khach hang')
        print('3-nap tien')
        print('4-rut tien')
        print('---')
        k = int(input('Nhap k: '))
    except ValueError:
        check = True
    else:
        if k == 1:
            MC.Add_Cus()
            
        if k == 2:
            n = input('nhap ten kh: ')
            MC.Show_Acc(n)
        if k == 3:
            try:
                ID = int(input('Nhap stk muon gui: '))
                money = float(input('Nhap so tien muon gui: '))
            except ValueError:
                print('Khong hop le')
            else:
                MA.Deposit_Money(ID,money)
        if k == 4:
            cus_name = input('Nhap ten KH: ')
            try:
                ID = int(input('Nhap stk: '))
                money = float(input('Nhap so tien muon rut: '))
            except ValueError:
                print('khong hop le')
            else:
                MC.Cus_Withdraws_Money(cus_name, ID, money)
        if k == 5:
            SA.Show_List()
        if k == 'Q':
            check = False