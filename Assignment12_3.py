class Arithematic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
    
    def Accept (self,A,B):
        self.value1 = A
        self.value2 = B
             
    def Addition(self):
        result = self.value1 + self.value2
        return result
    
    def Substraction(self):
        result = self.value1 - self.value2
        return result
    
    def Multiplication(self):
        result = self.value1 * self.value2
        return result
    
    def Division(self):
        result = self.value1 / self.value2
        return result
    
def main():
    obj1 = Arithematic()
    
    Ret = obj1.Accept(10,11)
    
    Ret = obj1.Addition()
    print("Addition is :",Ret)
    
    Ret = obj1.Substraction()
    print("Substraction is :",Ret)
    
    Ret = obj1.Multiplication()
    print("Multiplication is :",Ret)
    
    Ret = obj1.Division()
    print("Division is :",Ret)
    

if __name__ == "__main__":
    main()