from turtle import right
from Account import ManagementAcc as MA
from Account import SavingAcc as SA
from Account import CurrentAcc as CA


class Customer:
    def __init__(self,cus_name, acc, num_acc):
        self.cus_name = cus_name
        self.acc = acc
        self.num_acc = num_acc
    
class ManagementCus:
    list = []

    def quanity_cus(self):
        return self.list.__len__()

    def list_cus(self):
        return self.list
    
    def num_acc(self, cus_name):
        num = 1
        if self.quanity_cus() > 0:
            for i in self.list_cus():
                if i.cus_name == cus_name:
                    num = num + 1
        return num
    
    def add_cus(self):
        count = 0
        check = True
        while check:
            c = True
            cus_name = input('TenKH: ')
            for i in self.list_cus():
                if cus_name == i.cus_name:
                    count = count+1
            if count >= 9:
                print('Ban ko the them tai khoan nua')
                break
            
            while c:
                cate_acc = input('nhap loai tk: ')
                if cate_acc.upper() == 'TKTK':
                    acc = SA.add_account(SA)
                    c = False
                if cate_acc.upper() == 'TKVL':
                    acc = CA.add_account(CA)
                    c = False
            
            num_acc = self.num_acc(cus_name)
            
            cus = Customer(cus_name, acc, num_acc)
            self.list.append(cus)
            check = False

    def binary_search_recursive(self, list, left, right, id):
        try:
            if right>=left:
                mid = left + (right-left)//2
                if list[mid].id == id:
                    return mid
                if list[mid].id > id:
                    return self.binary_search_recursive(list, left, mid - 1, id)
                else:
                    return self.binary_search_recursive(list, mid + 1, right, id)
            return -1
        except IndexError:
            return -1
        


    def check_ca(self,cus_name,ID):
        c = False        
        for i in self.list_cus():
            if i.cus_name == cus_name and i.acc.id == ID:
                list = sorted(CA.list_curr(CA), key = lambda i:(i.id), reverse=False)
                right = CA.quanity_list_curr(CA)
                if self.binary_search_recursive(list, 0, right, ID) != -1:
                        c = True    
                               
        return c

    def check_sa(self,cus_name,id):
        c = False
        for i in self.list_cus():
            if i.cus_name == cus_name and i.acc.id == id:
                list = sorted(SA.list_saving(SA), key = lambda i:(i.id), reverse=False)
                right = SA.quanity_list_saving(SA)
                if self.binary_search_recursive(list, 0, right, id) != -1:
                        c = True
                         
        return c   
     
    def check_con(self,cus_name, id_ca, id_sa):
        c = False                   
        if self.check_ca(cus_name, id_ca) == True and self.check_sa(cus_name, id_sa) == True:
            c = True
        return c
    
    def sum_amount_sa(self,cus_name):
        sum = 0
        for i in self.list_cus():
            if i.cus_name == cus_name:
                if self.check_sa(cus_name, i.acc.id) == True:
                    sum = sum + i.acc.amount
        return sum
    
    def show_acc(self,cus_name):
        if self.quanity_cus() > 0:
            print('Ten Khach Hang: ', cus_name)
            if MA.quanity_acc(MA) > 0:
                for i in self.list_cus():
                    if i.cus_name == cus_name:
                        SA.show_acc(SA, i.acc.id)
                        CA.show_acc(CA, i.acc.id)

                print('Khach hang co tat ca ', i.num_acc, ' tk')
                print('Tong So Du trong tat ca tk tiet kiem: ', self.sum_amount_sa(cus_name))
                                  
    def withdrawal_money_ca(self,cus_name,money,id_ca,id_sa):
        gift_money = 0     
        if self.check_con(cus_name, id_ca, id_sa) == True:
            for i in SA.list_saving(SA):
                if i.id == id_sa:
                    print('So tien o tk khong du can chuyen them tu tktk')
                    gift_money = float(input('Nhap so tien can chuyen: '))
                    i.amount = i.amount - gift_money
            for i in CA.list_curr(CA):
                if i.id == id_ca:
                    i.amount = i.amount + gift_money
                    CA.withdrawal_money(CA, money, id_ca)
        else:
            print('Khong tim thay tk lien ket')
    
    def check_amount(self, id, money):
        if self.quanity_cus() > 0:
            for i in self.list_cus():
                if id == i.acc.id:
                    if money > i.acc.amount:
                        return 1
                    else:
                        return 0
                    
    def cus_withdrawal_money(self,cus_name,id, money):
        if self.quanity_cus() > 0:
            """for i in self.Get_list_Cus():
                if i.Cus_Name == cus_name and i.Acc.ID == ID :"""
            if self.check_sa(cus_name, id) == True:
                SA.withdrawal_money(SA, money, id)
                
            elif self.check_ca(cus_name, id) == True:
                if self.check_amount(id, money) == 0:
                    CA.withdrawal_money(CA, money, id)
                elif self.check_amount(id, money) == 1:
                    print('So tien rut lon hon hien co can phai su dung tktk')
                    try:
                        id_sa = int(input('Nhap stk tiet kiem lien ket:'))
                    except ValueError:
                        print('Khong hop le')
                    else:
                        print('Chuyen tien tu tktk sang tkvl')
                        self.withdrawal_money_ca(cus_name, money, id, id_sa)
                else:
                    print('None')
        else:
            print('Chua co tai khoan trong he thong')            
                
                                        
            
        
                  