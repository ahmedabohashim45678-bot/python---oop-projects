class BankAcount:
    def __init__(self,owner_name,balance):
        self.owner_name=owner_name
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,new_balance):
        self.__balance=new_balance
B3=BankAcount("Ahmed",1000)
print(B3.get_balance())
B3.set_balance(1500)
print(B3.get_balance())
