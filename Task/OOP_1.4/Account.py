
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

    def list_id(self):
        list_id = []
        for i in self.list_acc:
            list_id.append(i.id)
        return list_id

    def quanity_acc(self):
        return self.list_acc.__len__()
    
    def deposit_money(self,id, money):
        try:
            if self.quanity_acc() > 0:
                if id not in self.list_id() == True:
                    print('None')
                else:
                    c = self.list_id().index(id)
                    if money >= 0:
                        self.get_acc()[c].amount = self.get_acc()[c].amount + money
                        print('Ban vua nap:',money,'d')
                        print('So du hien tai cua ban: ', self.get_acc()[c].amount, 'd')
            else:
                print('none')
        except ValueError:
            print('chua co tk')
        
    def withdrawal_money(self, money,id):
        if self.quanity_acc(ManagementAcc) > 0:
            for i in self.get_acc(ManagementAcc):
                if i.id == id:
                    if money >= 0 and money < i.amount:
                        i.amount = i.amount - money
                        print('Ban vua rut: ', money, 'd, o stk: ', i.id)
                        print('So tien hien tai cua ban: ', i.amount, 'd')
                    else:
                        print('Khong hop le')
        
                    
    def add_account(self):
        try:
            check = True
            while check:
                id = int(input('Nhap so tai khoan: '))
                if id not in self.list_id(ManagementAcc):
                    check = False
            amount = float(input('Nhap so du: '))
        except ValueError:
            print('Khong hop le')
        else:
            acc = Account(id, amount)
            self.list_acc.append(acc)
        return acc

class SavingAcc(ManagementAcc):
    list = []
    def list_saving(self):
        return self.list
    def quanity_list_saving(self):
        return self.list.__len__()
    
    def add_account(self):
        acc = super().add_account(SavingAcc)
        self.list.append(acc)
        return acc


    def show_acc(self, id):
        for i in self.list_saving(SavingAcc):
            if id == i.id:
                print('TKTK: So tai khoan: ', i.id, ' co so du: ', i.amount, ' voi lai suat 8% nam:', i.amount * 8 / 100)
    def withdrawal_money(self, money, id):
        super().withdrawal_money(SavingAcc, money, id)
        
    def show_list(self):
        if self.quanity_acc() > 0:
            for i in self.list_saving():
                print(' {:<18} {:<18} '.format(i.id, i.amount))

        
class CurrentAcc(ManagementAcc):
    list = []
    def list_curr(self):
        return self.list
    
    def quanity_list_curr(self):
        return self.list.__len__()
    
    def add_account(self):
        acc = super().add_account(CurrentAcc)
        self.list.append(acc)
        return acc
    
    def show_acc(self,id):
        for i in self.list_curr(CurrentAcc):
            if id == i.id:
                print('TKVL: So tai khoan: ', i.id, ' co so du: ', i.amount)
                
    def withdrawal_money(self, money, id):
        super().withdrawal_money(CurrentAcc, money, id)
        