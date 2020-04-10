class calculator():
    def __init__(self):
        self.num1=int(input("Enter number 1:"))
        self.num2 =int(input("Enter number 2:"))
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        try :
            return self.num1 // self.num2
        except ZeroDivisionError :
            print("Divide by zero not possible, swapping numbers and dividing")
            return  0
    def mod(self):
        return self.num1 % self.num2

if __name__ == '__main__':
    cal=calculator()
    print("sum=",cal.add())
    print("product =",cal.mul())
    print("modulus=",cal.mod())
    print("subtract=",cal.sub())
    print("divide=",cal.div())

