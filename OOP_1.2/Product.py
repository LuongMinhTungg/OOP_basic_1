class Product:
    def __init__(self, pro_id, pro_name, pro_brand_name, pro_cate, pro_price):
        self.pro_id = pro_id
        self.pro_name = pro_name
        self.pro_brand_name = pro_brand_name
        self.pro_cate = pro_cate
        self.pro_price = pro_price


class ManagementPro:
    list_pro = []

    def quanity_pro(self):
        return self.list_pro.__len__()

    def get_list_pro(self):
        return self.list_pro

    def id(self):
        max_id = 1
        if self.quanity_pro() > 0:
            max_id = self.list_pro[0].pro_id
            for i in self.get_list_pro():
                if max_id < i.pro_id:
                    max_id = i.pro_id
            max_id = max_id + 1
        return max_id

    def add_pro(self):
        pro_id = self.id()
        pro_name = input('Nhap ten SP: ')
        pro_brand_name = input('Nhap ten thuong hieu: ')
        c = True
        while c:
            pro_cate = input('Nhap loai sp: ')
            if pro_cate.upper() == 'do dien'.upper() or pro_cate.upper() == 'do gia dung'.upper():
                c = False
        pro_price = float(input('gia: '))
        if pro_price > 0:
            pro = Product(pro_id, pro_name, pro_brand_name, pro_cate, pro_price)
            self.list_pro.append(pro)
        else:
            print('Gia tien khong dc am')

    def Show_Pro(self, list):
        f = open('ListPro.txt.txt', 'w+')
        print('{:<8} {:<18} {:<18} {:<12}{:<8}'.format('MaSP', 'TenSP', 'Thuong Hieu', 'LoaiSP', 'Gia'))
        f.write('{:<8} {:<18} {:<18} {:<12}{:<8} \n'.format('MaSP', 'TenSP', 'Thuong Hieu', 'LoaiSP', 'Gia'))
        if list.__len__() > 0:
            for i in list:
                print('{:<8} {:<18} {:<18} {:<12}{:<8} \n'.format(i.pro_id, i.pro_name, i.pro_brand_name, i.pro_cate,
                                                                  i.pro_price))
                f.write('{:<8} {:<18} {:<18} {:<12}{:<8}'.format(i.pro_id, i.pro_name, i.pro_brand_name, i.pro_cate,
                                                                 i.pro_price))
        else:
            print('chua co sp nao')

        f.close()

    def search_pro_name(self, pro_name):
        pro = None
        if self.quanity_pro() > 0:
            for i in self.get_list_pro():
                if pro_name == i.pro_name:
                    pro = i
        else:
            print('chua co sp')
        return pro
