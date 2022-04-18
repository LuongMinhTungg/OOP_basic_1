from tkinter import Tk
from Customer import ManagementCus
from Account import SavingAcc,CurrentAcc,ManagementAcc
MC = ManagementCus()
CA = CurrentAcc()
SA = SavingAcc()
MA = ManagementAcc()
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
            MC.add_cus()
            
        if k == 2:
            n = input('nhap ten kh: ')
            MC.show_acc(n)
        if k == 3:
            try:
                ID = int(input('Nhap stk muon gui: '))
                money = float(input('Nhap so tien muon gui: '))
            except ValueError:
                print('Khong hop le')
            else:
                MA.deposit_money(ID, money)
        if k == 4:
            cus_name = input('Nhap ten KH: ')
            try:
                ID = int(input('Nhap stk: '))
                money = float(input('Nhap so tien muon rut: '))
            except ValueError:
                print('khong hop le')
            else:
                MC.cus_withdrawal_money(cus_name, ID, money)
        if k == 5:
            SA.show_list()
        if k == 'Q':
            check = False