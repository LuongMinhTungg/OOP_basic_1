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
    list = []
    list_discount = []
    num_discount = 0
    

    def discount(self, cus_name, pro, num_discount):
        num_discount = self.discount
        if pro!= None:
            MP.list_pro(MP).remove(pro)
            self.list_discount.append(pro)
            self.num_discount = self.num_discount + 1
            if self.num_discount <= 5:
                time = datetime.datetime.now()
                bill = Bill(cus_name,pro.pro_name,pro.pro_price/2,time)
                self.list.append(bill)
            else:
                time = datetime.datetime.now()
                bill = Bill(cus_name,pro.pro_name,pro.pro_price,time)
                self.list.append(bill)

    def sell(self,cus_name,pro_name):
        pro = None
        try:
            if MC.search_cus_name(MC, cus_name).cus_name.upper() == cus_name.upper():
                if MP.search_pro_name(MP, pro_name).pro_name.upper() == pro_name.upper():
                    pro = MP.search_pro_name(MP,pro_name)
                    self.discount(cus_name, pro, self.num_discount)
        except AttributeError:
            print('chua co sp hoac kh')
        else:
            print('Mua hang thanh cong')

                        
    def list_bill(self):
        return self.list
    
    def quanity_bill(self):
        return self.list.__len__()
    
    def selled(self):
        if self.quanity_bill() > 0:
            print('Danh sach san pham da ban')
            print(' {:<18} {:<18} {:<8} {:<40}'.format('ten kh', 'ten sp', 'Gia', 'thoi gian mua'))
            for i in self.list_bill():
                print(' {:<18} {:<18} {:<8} {:<40}'.format(i.cus_name, i.pro_name, i.pro_price, i.time.strftime("%m/%d/%Y, %H:%M:%S")))
        else:
            print('chua co hoa don')
        
    def sort(self):
        self.list_bill().sort(key = lambda i:(i.cus_name, i.time), reverse=True)
        
    def show_bill(self,cus_name):
        try:
            if MC.search_cus_name(MC, cus_name).cus_name.upper() == cus_name.upper():
                print(' {:<18} {:<18} {:<8} {:<40}'.format('ten kh', 'ten sp', 'Gia', 'thoi gian mua'))
                for i in self.list_bill():
                    if i.cus_name == cus_name:
                        print(' {:<18} {:<18} {:<8} {:<40}'.format(i.cus_name, i.pro_name, i.pro_price, i.time.strftime("%m/%d/%Y, %H:%M:%S")))
        except AttributeError:
            print('chua co kh')

                