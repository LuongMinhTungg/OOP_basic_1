import string
import random


class Customer:
    def __init__(self, cus_id, cus_name, cus_phone):
        self.cus_id = cus_id
        self.cus_name = cus_name
        self.cus_phone = cus_phone


class ManagementCus:
    list = []

    def quanity_cus(self):
        return self.list.__len__()

    def list_cus(self):
        return self.list

    def id(self):
        size = 6
        char = string.ascii_uppercase + string.digits
        return ''.join(random.choice(char) for _ in range(size))

    def add_cus(self):
        check = True
        while check:
            cus_id = self.id()
            for i in self.list_cus():
                if cus_id == i.cus_id:
                    check = True
            check = False
        cus_name = input('Nhap ten KH: ')
        cus_phone = input('Nhap sdt: ')
        cus = Customer(cus_id, cus_name, cus_phone)
        self.list.append(cus)

    def show_cus(self, list):
        f = open('ListAcc.txt', 'w+')
        print('{:<18} {:<18} {:<12}'.format('MaKH', 'TenKH', 'sdt'))
        f.write(('{:<18} {:<18} {:<12} \n'.format('MaKH', 'TenKH', 'sdt')))

        if list.__len__() > 0:
            for i in list:
                print('{:<18} {:<18} {:<12}'.format(i.cus_id, i.cus_name, i.cus_phone))
                f.write('{:<18} {:<18} {:<12}'.format(i.cus_id, i.cus_name, i.cus_phone))
        else:
            print('None')
        f.close()

    def search_cus_name(self, cus_name):
        cus = None
        if self.quanity_cus(ManagementCus) > 0:
            for i in self.list_cus(ManagementCus):
                if i.cus_name.upper() == cus_name.upper():
                    cus = i
        else:
            print('chua co kh')
        return cus
