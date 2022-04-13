
class Account:
    def __init__(self, acc_name, acc_number, amount):
        self.acc_name = acc_name
        self.acc_number = acc_number
        self.amount = amount
    def get_acc_name(self):
        return self.acc_name
    def get_acc_number(self):
        return self.acc_number
    def get_amount(self):
        return self.amount
    
    def Fees(self, fees):
        return fees * 1/100
 
    def deposit(self):
        a = float(input('Nhap so tien muon nap: '))       
        if(a >= 0):           
            fees = self.Fees(a)
            if fees > 1000:
                fees = fees
            else:
                fees = 1000
            self.amount = self.amount + a - fees
            print('Ban vua nap:',a,'d')
            print('phi DV nap tien la: ', fees, 'd')
            print('So du hien tai cua ban(da tru phi DV): ',self.amount,'d')
        else:
            print('Khong hop le')
        return a
    
    def withdrawal(self):
        a = float(input('Nhap so tien muon rut: '))
        if a >= 0 and a < self.get_amount():
            fees = self.fees(a)
            if fees > 1000:
                fees = fees
            else:
                fees = 1000
            self.amount = self.amount - a - fees
            print('Ban vua rut: ', a, 'd')
            print('Phi DV rut tien la: ', fees,'d')
            print('So tien hien tai cua ban(da tru phi DV): ', self.amount,'d')
        else:
            print('Khong hop le')
        return a
    
    def show(self):
        print('Ten tk:',Account.get_acc_name(),'Ma TK:',Account.get_acc_number(),'So Du:',Account.get_amount())

acc_name = 'tung'
acc_number = '1'
amount = 50000
acc = Account(acc_name,acc_number,amount)

check = True
while check:
    try:
        print('---')
        print('1-nap tien')
        print('2-rut tien')
        print('3-show')
        print('---')
        k = int(input('Nhap k: '))
    except ValueError:
        check = True
    else:
        if k == 1:
            Account.deposit()
            
        if k == 2:
            acc.withdrawal()
        if k == 3:
           acc.show()




    
