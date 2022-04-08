import string
import random
class Customer:
    def __init__(self, Cus_ID ,Cus_Name,Cus_Phone ):
        self.Cus_ID = Cus_ID
        self.Cus_Name = Cus_Name
        self.Cus_Phone = Cus_Phone

class Management_Cus:
    list_cus = []
    def Quanity_Cus(self):
        return self.list_cus.__len__()

    def Get_list_Cus(self):
        return self.list_cus

    def ID(self):
        size = 6
        char = string.ascii_uppercase + string.digits
        return ''.join(random.choice(char) for _ in range(size))
    
    def Add_Cus(self):
        check = True
        while check:
            cus_ID = self.ID()
            for i in self.Get_list_Cus():
                if cus_ID == i.Cus_ID:
                    check = True
            check = False
        cus_name = input('Nhap ten KH: ')
        cus_phone = input('Nhap sdt: ')
        cus = Customer(cus_ID, cus_name, cus_phone)
        self.list_cus.append(cus)
    
    def Show_Cus(self,list):
        f = open('DSKH.txt','w+')
        print('{:<18} {:<18} {:<12}'.format('MaKH', 'TenKH', 'sdt'))
        f.write(('{:<18} {:<18} {:<12} \n'.format('MaKH', 'TenKH', 'sdt')))
        for i in list:
            if list.__len__() > 0:
                print('{:<18} {:<18} {:<12}'.format(i.Cus_ID, i.Cus_Name, i.Cus_Phone))
                f.write('{:<18} {:<18} {:<12}'.format(i.Cus_ID, i.Cus_Name, i.Cus_Phone))
        f.close()
            

    
    
    
    def Search_Cus_Name(self,cus_name):
        cus = None
        if self.Quanity_Cus(Management_Cus) > 0:
            for i in self.Get_list_Cus(Management_Cus):
                if i.Cus_Name.upper() == cus_name.upper():
                    cus = i
        else:
            print('chua co kh')
        return cus
        