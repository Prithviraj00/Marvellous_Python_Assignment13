class Arithmetic:
    
    def __init__(self,A):
        self.value = A
        
    def ChkPrime(self):
        for i in range(2,self.value):
            if(self.value % i == 0):
                return False
        return True
        
    def ChkPrfect(self):
        sum_of_factors = self.SumFactors()
        if sum_of_factors == self.value:
            return True
        return False
    
    def SumFactors(self):
        return sum(self.getFactors())
        
    def getFactors(self):
        factors = []
        for i in range(1, self.value):
            if self.value % i == 0:
                factors.append(i)
        return factors

def main():
    obj = Arithmetic(6)
    print("sum of factors ",obj.SumFactors())
    print( "Is number Perfect: ",obj.ChkPrfect())
    print( "Is number Prime: ",obj.ChkPrime())
    print(obj.getFactors())

if __name__ == "__main__":
    main()
