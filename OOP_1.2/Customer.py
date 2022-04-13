import string
import random


class Customer:
    def __init__(self, cus_id, cus_name, cus_phone):
        self.cus_id = cus_id
        self.cus_name = cus_name
        self.Cus_Phone = cus_phone


class ManagementCus:
    list_cus = []

    def quanity_cus(self):
        return self.list_cus.__len__()

    def get_list_cus(self):
        return self.list_cus

    def id(self):
        size = 6
        char = string.ascii_uppercase + string.digits
        return ''.join(random.choice(char) for _ in range(size))

    def add_cus(self):
        check = True
        while check:
            cus_id = self.id()
            for i in self.get_list_cus():
                if cus_id == i.cus_id:
                    check = True
            check = False
        cus_name = input('Nhap ten KH: ')
        cus_phone = input('Nhap sdt: ')
        cus = Customer(cus_id, cus_name, cus_phone)
        self.list_cus.append(cus)

    def show_cus(self, list):
        f = open('ListAcc.txt.txt', 'w+')
        print('{:<18} {:<18} {:<12}'.format('MaKH', 'TenKH', 'sdt'))
        f.write(('{:<18} {:<18} {:<12} \n'.format('MaKH', 'TenKH', 'sdt')))
        for i in list:
            if list.__len__() > 0:
                print('{:<18} {:<18} {:<12}'.format(i.cus_id, i.cus_name, i.cus_phone))
                f.write('{:<18} {:<18} {:<12}'.format(i.cus_id, i.cus_name, i.cus_phone))
        f.close()

    def search_cus_name(self, cus_name):
        cus = None
        if self.quanity_cus() > 0:
            for i in self.get_list_cus():
                if i.cus_name.upper() == cus_name.upper():
                    cus = i
        else:
            print('chua co kh')
        return cus
