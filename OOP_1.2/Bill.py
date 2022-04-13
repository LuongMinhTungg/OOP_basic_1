from mailbox import NotEmptyError
from Product import ManagementPro as MP
from Customer import ManagementCus as MC

import datetime

class Bill:
    def __init__(self, cus_name, pro_name, pro_price, time):
        self.cus_name = cus_name
        self.pro_name = pro_name
        self.pro_price = pro_price
        self.time = time


class ManagementBill:
    list_bill = []
    list = []
    discount = 0
    

    def discount(self, cus_name, pro, discount):
        discount = self.discount
        if pro!= None:
            MP.GetlistPro(MP).remove(pro)
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

    def sell(self,cus_name,pro_name):
        pro = None
        try:
            if MC.search_cus_name(MC, cus_name).Cus_Name.upper() == cus_name.upper():
                if MP.Search_Pro_Name(MP, pro_name).Pro_Name.upper() == pro_name.upper():
                    pro = MP.Search_Pro_Name(MP,pro_name)
                    self.discount(cus_name, pro, self.discount)
        except AttributeError:
            print('chua co sp hoac khach hang')
        else:
            print('Mua hang thanh cong')
                
            
                        
    def get_list_bill(self):
        return self.list_bill
    
    def quanity_bill(self):
        return self.list_bill.__len__()
    
    def selled(self):
        if self.quanity_bill() > 0:
            print('Danh sach san pham da ban')
            print(' {:<18} {:<18} {:<8} {:<40}'.format('ten kh', 'ten sp', 'Gia', 'thoi gian mua'))
            for i in self.get_list_bill():
                print(' {:<18} {:<18} {:<8} {:<40}'.format(i.cus_name, i.pro_name, i.pro_price, i.time.strftime("%m/%d/%Y, %H:%M:%S")))
        else:
            print('chua co hoa don')
        
    def sort(self):
        self.get_list_bill().sort(key = lambda i:(i.cus_name, i.time), reverse=True)
        
    def show_bill(self,cus_name):
        print(' {:<18} {:<18} {:<8} {:<40}'.format('ten kh', 'ten sp', 'Gia', 'thoi gian mua'))
        for i in self.get_list_bill():
            if i.cus_name == cus_name:
                print(' {:<18} {:<18} {:<8} {:<40}'.format(i.cus_name, i.pro_name, i.pro_price, i.time.strftime("%m/%d/%Y, %H:%M:%S")))
                
            
                