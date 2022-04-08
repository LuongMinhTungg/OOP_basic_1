
from ssl import SO_TYPE


class Account:
    def __init__(self, ID, Amount):
        self.ID = ID
        self.Amount = Amount
    def getSTK(self):
        return self.stk
    def getSD(self):
        return self.sd
    
class Management_Acc:
    list_acc = []
    def Get_Acc(self):
        return self.list_acc
    def Quanity_Acc(self):
        return self.list_acc.__len__()
    
    def Deposit_Money(self,ID, money):

        if self.Quanity_Acc() > 0:
            for i in self.Get_Acc():
                if i.ID == ID  and  money >= 0:
                    i.Amount = i.Amount + money
                    print('Ban vua nap:',money,'d')
                    print('So du hien tai cua ban: ',i.Amount,'d')

        
    def Withdraws_Money(self, money,ID):
        if self.Quanity_Acc(Management_Acc) > 0:
            for i in self.Get_Acc(Management_Acc):
                if i.ID == ID:
                    if money >= 0 and money < i.Amount:
                        i.Amount = i.Amount - money
                        print('Ban vua rut: ', money, 'd, o stk: ',i.ID)
                        print('So tien hien tai cua ban: ', i.Amount,'d')
                    else:
                        print('Khong hop le')
        
                    
    def Add_Account(self):
        try:
            ID = int(input('Nhap so tai khoan: '))
            amount = float(input('Nhap so du: '))
        except ValueError:
            print('Khong hop le')
        else:
            acc = Account(ID,amount)
            self.list_acc.append(acc)
        return acc

class Saving_Acc(Management_Acc):
    list_saving = []
    def Get_list_Saving(self):        
        return self.list_saving
    def Quanity_list_Saving(self):
        return self.list_saving.__len__()
    
    def Add_Account(self):
        acc = super().Add_Account(Saving_Acc)
        self.list_saving.append(acc)
        return acc


    def Show_Acc(self, ID):
        for i in self.Get_list_Saving(Saving_Acc):
            if ID == i.ID:
                print('TKTK: So tai khoan: ',i.ID,' co so du: ',i.Amount,' voi lai suat 8% nam:', i.Amount*8/100)
    def Withdraws_Money(self, money, ID):
        super().Withdraws_Money(Saving_Acc,money,ID)
        
    def Show_List(self):
        if self.Quanity_Acc() > 0:
            for i in self.Get_list_Saving():
                print(' {:<18} {:<18} '.format(i.ID, i.Amount))

        
class Current_Acc(Management_Acc):
    list_curr = []
    def Get_list_Curr(self):
        return self.list_curr
    
    def Quanity_list_Curr(self):
        return self.list_curr.__len__()
    
    def Add_Account(self):
        acc = super().Add_Account(Current_Acc)
        self.list_curr.append(acc)
        return acc
    
    def Show_Acc(self,ID):
        for i in self.Get_list_Curr(Current_Acc):
            if ID == i.ID:
                print('TKVL: So tai khoan: ',i.ID,' co so du: ',i.Amount)

    def Search_Cus_Name(self, cus_name):
        cus = None
        if self.soluongKH() > 0:
            for i in self.getlistKH():
                if i.tenKH == cus_name:
                    kh = i
        return cus
    
                
    def Withdraws_Money(self, money,ID):

        super().Withdraws_Money(Current_Acc,money,ID)
        