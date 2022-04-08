from mailbox import NotEmptyError
from Product import Management_Pro as MP
from Customer import Management_Cus as MC

import datetime

class Bill:
    def __init__(self, Cus_Name, Pro_Name, Pro_Price, Time):
        self.Cus_Name = Cus_Name
        self.Pro_Name = Pro_Name
        self.Pro_Price = Pro_Price
        self.Time = Time


class Management_Bill:
    list_bill = []
    list = []
    discount = 0
    
    '''
    def banHang(self,kh,sp):
        s = None
        if QLKH.soluongKH(QLKH) > 0:
            for j in QLKH.getlistKH(QLKH):
                if kh.upper == j.tenKH.upper:       
                    if QLSP.soluongSP(QLSP) > 0:
                        for i in QLSP.getlistSP(QLSP):
                            if i.tenSP == sp:
                                s = i               
                                if s != None:
                                    QLSP.getlistSP(QLSP).remove(s)
                                    self.list.append(s)
                                    self.km = self.km + 1
                                    if self.km <= 5:
                                        tg = datetime.datetime.now()                              
                                        hd = HD(kh,sp,i.gia/2,tg)
                                        self.listHD.append(hd)
                                    else:
                                        tg = datetime.datetime.now()
                                        hd = HD(kh,sp,i.gia,tg)
                                        self.listHD.append(hd)
                            else:
                                print('Khong tim thay san pham')
                    else:
                        print('Kho rong')
                else:
                    print('Khong co khach hang tuong ung')
        else:
            print('chua co khach hang')
    '''
    def Discount(self, cus_name, pro, discount):
        discount = self.discount
        if pro!= None:
            MP.Get_list_Pro(MP).remove(pro)
            self.list.append(pro)
            self.discount = self.discount + 1
            if self.discount <= 5:
                time = datetime.datetime.now()
                bill = Bill(cus_name,pro.Pro_Name,pro.Pro_Price/2,time)
                self.list_bill.append(bill)
            else:
                time = datetime.datetime.now()
                bill = Bill(cus_name,pro.Pro_Name,pro.Pro_Price,time)
                self.list_bill.append(bill)

    def Sell(self,cus_name,pro_name):
        pro = None
        try:
            if MC.Search_Cus_Name(MC, cus_name).Cus_Name.upper() == cus_name.upper():
                if MP.Search_Pro_Name(MP, pro_name).Pro_Name.upper() == pro_name.upper():
                    pro = MP.Search_Pro_Name(MP,pro_name)
                    self.Discount(cus_name,pro,self.discount)
        except AttributeError:
            print('chua co sp hoac khach hang')
        else:
            print('Mua hang thanh cong')
                
            
                        
    def Get_list_Bill(self):
        return self.list_bill
    
    def Quanity_Bill(self):
        return self.list_bill.__len__()
    
    def Selled(self):
        if self.Quanity_Bill() > 0:
            print('Danh sach san pham da ban')
            print(' {:<18} {:<18} {:<8} {:<40}'.format('ten kh', 'ten sp', 'Gia', 'thoi gian mua'))
            for i in self.Get_list_Bill():
                print(' {:<18} {:<18} {:<8} {:<40}'.format(i.Cus_Name, i.Pro_Name, i.Pro_Name, i.Time.strftime("%m/%d/%Y, %H:%M:%S")))
        else:
            print('chua co hoa don')
        
    def Sort(self):
        self.Get_list_Bill().sort(key = lambda i:(i.Cus_Name,i.Time), reverse=True)
        
    def Show_Bill(self,cus_name):
        print(' {:<18} {:<18} {:<8} {:<40}'.format('ten kh', 'ten sp', 'Gia', 'thoi gian mua'))
        for i in self.Get_list_Bill():
            if i.Cus_Name == cus_name:
                print(' {:<18} {:<18} {:<8} {:<40}'.format(i.Cus_Name, i.Pro_Name, i.Pro_Price, i.Time.strftime("%m/%d/%Y, %H:%M:%S")))
                
            
                