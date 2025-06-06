class BankAccount:
    ROI = 10.5
    
    def __init__(self,A,B):
        self.name = A
        self.Amount = B
    
    def deposit(self,amount):
        self.Amount = self.Amount + amount 
        
    def withdraw(self,amount1):
        self.Amount =self.Amount - amount1
        
    def calculateIntrest(self):
        cal = (self.Amount * BankAccount.ROI) / 100
        print ("Rate of Interst Amount is :",cal)
        
    def display(self):
        print("User Name :",self.name)
        print("User Bank Amount :",self.Amount)
        

def main():
    obj1 = BankAccount('Shubham' , 50000)
    obj1.deposit(10000)
    obj1.withdraw(2000)
    obj1.calculateIntrest()
    obj1.display()

if __name__ == "__main__":
    main()