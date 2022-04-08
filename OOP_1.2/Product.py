class Product:
    def __init__(self, Pro_ID, Pro_Name, Pro_BrandName, Pro_Cate, Pro_Price):
        self.Pro_ID = Pro_ID
        self.Pro_Name = Pro_Name
        self.Pro_BrandName = Pro_BrandName
        self.Pro_Cate = Pro_Cate
        self.Pro_Price = Pro_Price

        
class Management_Pro:
    list_pro = []
    
    def Quanity_Pro(self):
        return self.list_pro.__len__()

    def Get_list_Pro(self):
        return self.list_pro

    def ID(self):
        maxID = 1
        if self.Quanity_Pro() > 0:
            maxID = self.list_pro[0].Pro_ID
            for i in self.Get_list_Pro():
                if(maxID < i.Pro_ID):
                    maxID = i.Pro_ID
            maxID = maxID + 1
        return maxID
        
    def Add_Pro(self):
        pro_ID = self.ID()
        pro_name = input('Nhap ten SP: ')
        pro_brandname = input('Nhap ten thuong hieu: ')
        c = True
        while c:    
            pro_cate = input('Nhap loai sp: ')
            if pro_cate.upper() == 'do dien'.upper() or pro_cate.upper() == 'do gia dung'.upper() :
                c = False            
        pro_price = float(input('gia: '))
        if(pro_price > 0):
            pro = Product(pro_ID, pro_name, pro_brandname, pro_cate, pro_price)
            self.list_pro.append(pro)
        else:
            print('Gia tien khong dc am')

    
    def Show_Pro(self,list):
        f = open('DSSP.txt','w+')
        print('{:<8} {:<18} {:<18} {:<12}{:<8}'.format('MaSP', 'TenSP', 'Thuong Hieu', 'LoaiSP', 'Gia'))
        f.write('{:<8} {:<18} {:<18} {:<12}{:<8} \n'.format('MaSP', 'TenSP', 'Thuong Hieu', 'LoaiSP', 'Gia'))
        if list.__len__() > 0:
            for i in list:
                print('{:<8} {:<18} {:<18} {:<12}{:<8} \n'.format(i.Pro_ID, i.Pro_Name, i.Pro_BrandName, i.Pro_Cate, i.Pro_Price))
                f.write('{:<8} {:<18} {:<18} {:<12}{:<8}'.format(i.Pro_ID, i.Pro_Name, i.Pro_BrandName, i.Pro_Cate, i.Pro_Price))
        else:
            print('chua co sp nao')      
                    
        f.close()
        
    def Search_Pro_Name(self, pro_name):
        pro = None
        if self.Quanity_Pro(Management_Pro) > 0:
            for i in self.Get_list_Pro(Management_Pro):
                if pro_name == i.Pro_Name:
                    pro = i
        else:
            print('chua co sp')
        return pro
        

    