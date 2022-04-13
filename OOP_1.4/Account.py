
class Account:
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount
    def get_id(self):
        return self.id
    def get_amount(self):
        return self.amount
    
class ManagementAcc:
    list_acc = []
    def get_acc(self):
        return self.list_acc
    def quanity_acc(self):
        return self.list_acc.__len__()
    
    def deposit_money(self,id, money):

        if self.quanity_acc() > 0:
            for i in self.get_acc():
                if i.id == id  and  money >= 0:
                    i.amount = i.amount + money
                    print('Ban vua nap:',money,'d')
                    print('So du hien tai cua ban: ', i.amount, 'd')

        
    def withdrawal_money(self, money,ID):
        if self.quanity_acc() > 0:
            for i in self.get_acc(ManagementAcc):
                if i.id == ID:
                    if money >= 0 and money < i.amount:
                        i.amount = i.amount - money
                        print('Ban vua rut: ', money, 'd, o stk: ', i.id)
                        print('So tien hien tai cua ban: ', i.amount, 'd')
                    else:
                        print('Khong hop le')
        
                    
    def add_account(self):
        try:
            id = int(input('Nhap so tai khoan: '))
            amount = float(input('Nhap so du: '))
        except ValueError:
            print('Khong hop le')
        else:
            acc = Account(id, amount)
            self.list_acc.append(acc)
        return acc

class SavingAcc(ManagementAcc):
    list_saving = []
    def get_list_saving(self):
        return self.list_saving
    def quanity_list_saving(self):
        return self.list_saving.__len__()
    
    def add_account(self):
        acc = super().add_account()
        self.list_saving.append(acc)
        return acc


    def show_acc(self, id):
        for i in self.get_list_saving():
            if id == i.id:
                print('TKTK: So tai khoan: ', i.id, ' co so du: ', i.amount, ' voi lai suat 8% nam:', i.amount * 8 / 100)
    def withdrawal_money(self, money, ID):
        super().withdrawal_money(SavingAcc, money)
        
    def show_list(self):
        if self.quanity_acc() > 0:
            for i in self.get_list_saving():
                print(' {:<18} {:<18} '.format(i.id, i.amount))

        
class CurrentAcc(ManagementAcc):
    list_curr = []
    def get_list_curr(self):
        return self.list_curr
    
    def quanity_list_curr(self):
        return self.list_curr.__len__()
    
    def add_account(self):
        acc = super().add_account()
        self.list_curr.append(acc)
        return acc
    
    def show_acc(self,id):
        for i in self.get_list_Curr(CurrentAcc):
            if id == i.id:
                print('TKVL: So tai khoan: ', i.id, ' co so du: ', i.amount)
                
    def withdrawal_money(self, money, id):
        super().withdrawal_money(CurrentAcc, money)
        