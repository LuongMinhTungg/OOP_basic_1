from turtle import right
from Account import Management_Acc as MA
from Account import Saving_Acc as SA
from Account import Current_Acc as CA
class Customer:
    def __init__(self,Cus_Name, Acc, Num_Acc):
        self.Cus_Name = Cus_Name
        self.Acc = Acc
        self.Num_Acc = Num_Acc
    
class Management_Cus:
    list_cus = []

    def Quanity_Cus(self):
        return self.list_cus.__len__()

    def Get_list_Cus(self):
        return self.list_cus
    
    def Num_Acc(self,cus_name):
        num = 1
        if self.Quanity_Cus() > 0:
            for i in self.Get_list_Cus():
                if i.Cus_Name == cus_name:
                    num = num + 1
        return num
    

    
    def Add_Cus(self):
        count = 0
        check = True
        while check:
            c = True
            cus_name = input('TenKH: ')
            for i in self.Get_list_Cus():
                if cus_name == i.Cus_Name:
                    count = count+1
            if count >=9:
                print('Ban ko the them tai khoan nua')
                break
            
            while c:
                Cate_Acc = input('nhap loai tk: ')
                if Cate_Acc.upper() == 'TKTK':
                    acc = SA.Add_Account(SA)
                    c = False
                if Cate_Acc.upper() == 'TKVL':
                    acc = CA.Add_Account(CA)
                    c = False
            
            num_acc = self.Num_Acc(cus_name)
            
            cus = Customer(cus_name, acc, num_acc)
            self.list_cus.append(cus)
            check = False
    

    def BinarySearchRecursive(self,list,left,right, ID):       
        try:
            if right>=left:
                mid = left + (right-left)//2
                if list[mid].ID == ID:
                    return mid
                if list[mid].ID > ID:
                    return self.BinarySearchRecursive(list, left, mid-1, ID)
                else:
                    return self.BinarySearchRecursive(list, mid+1, right , ID)
            return -1
        except IndexError:
            return -1
        


    def Check_CA(self,cus_name,ID):
        c = False        
        for i in self.Get_list_Cus():
            if i.Cus_Name == cus_name and i.Acc.ID == ID:
                list = sorted(CA.Get_list_Curr(CA),key = lambda i:(i.ID), reverse=False)
                right = CA.Quanity_list_Curr(CA)
                if self.BinarySearchRecursive(list,0,right,ID) != -1:
                        c = True    
                               
        return c      
    def Check_SA(self,cus_name,ID):
        c = False
        for i in self.Get_list_Cus():
            if i.Cus_Name == cus_name and i.Acc.ID == ID:
                list = sorted(SA.Get_list_Saving(SA),key = lambda i:(i.ID), reverse=False)
                right = SA.Quanity_list_Saving(SA)
                if self.BinarySearchRecursive(list, 0, right, ID) != -1:
                        c = True  
                         
        return c   
     
    def Check_Con(self,cus_name, ID_CA, ID_SA):
        c = False                   
        if self.Check_CA(cus_name, ID_CA) == True and self.Check_SA(cus_name,ID_SA) == True:
            c = True
        return c
    
    def Sum_Amount_SA(self,cus_name):
        sum = 0
        for i in self.Get_list_Cus():
            if i.Cus_Name == cus_name:
                if self.Check_SA(cus_name,i.Acc.ID) == True:
                    sum = sum + i.Acc.Amount
        return sum
    
    def Show_Acc(self,cus_name):
        if self.Quanity_Cus() > 0:
            print('Ten Khach Hang: ', cus_name)
            if MA.Quanity_Acc(MA) > 0:
                for i in self.Get_list_Cus():
                    if i.Cus_Name == cus_name:
                        SA.Show_Acc(SA,i.Acc.ID)
                        CA.Show_Acc(CA,i.Acc.ID)

                print('Khach hang co tat ca ',i.Num_Acc,' tk')
                print('Tong So Du trong tat ca tk tiet kiem: ', self.Sum_Amount_SA(cus_name))
                                  
    def Withdraws_Money_CA(self,cus_name,money,ID_CA,ID_SA):
        gift_money = 0     
        if self.Check_Con(cus_name,ID_CA,ID_SA) == True:
            for i in SA.Get_list_Saving(SA):
                if i.ID == ID_SA:
                    print('So tien o tk khong du can chuyen them tu tktk')
                    gift_money = float(input('Nhap so tien can chuyen: '))
                    i.Amount = i.Amount - gift_money
            for i in CA.Get_list_Curr(CA):
                if i.ID == ID_CA:
                    i.Amount = i.Amount + gift_money
                    CA.Withdraws_Money(CA,money,ID_CA)
        else:
            print('Khong tim thay tk lien ket')
    
    def Check_Amount(self,ID,money):
        if self.Quanity_Cus() > 0:
            for i in self.Get_list_Cus():
                if ID == i.Acc.ID:
                    if money > i.Acc.Amount: 
                        return 1
                    else:
                        return 0
                    
    def Cus_Withdraws_Money(self,cus_name,ID, money):
        if self.Quanity_Cus() > 0:
            """for i in self.Get_list_Cus():
                if i.Cus_Name == cus_name and i.Acc.ID == ID :"""
            if self.Check_SA(cus_name,ID) == True:
                SA.Withdraws_Money(SA,money,ID)
                
            if self.Check_CA(cus_name,ID) == True:
                if self.Check_Amount(ID, money) == 0:
                    CA.Withdraws_Money(CA,money,ID)
                elif self.Check_Amount(ID, money) == 1:
                    print('So tien rut lon hon hien co can phai su dung tktk')
                    try:
                        ID_SA = int(input('Nhap stk tiet kiem lien ket:'))
                    except ValueError:
                        print('Khong hop le')
                    else:
                        print('Chuyen tien tu tktk sang tkvl')
                        self.Withdraws_Money_CA(cus_name,money,ID,ID_SA)
        else:
            print('Chua co tai khoan trong he thong')            
                
                                        
            
        
                  