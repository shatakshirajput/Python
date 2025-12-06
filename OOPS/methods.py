# instance methods, class methods, static methods

class Laptop:
    st = "ssd"
    
    def __init__(self,RAM,s):
        self.RAM =RAM
        self.s =s

    def get_info(self):   # instance method
        print(f"Laptop has {self.RAM} RAM & {self.s} {self.st}")
    
    @classmethod          # class method
    def get_storage_type(cls):
        print(f"Storage type: {cls.st}")

    @staticmethod         # static method
    def calc_discount(price,discount):
        final_price = price - (discount * price)/100
        print(f"Final price after discount is {final_price}")

l1 = Laptop("16gb","512gb")
l2 = Laptop("8gb","256gb")

l1.get_info()
l2.get_info()

Laptop.get_storage_type()
l1.get_storage_type()
l2.get_storage_type()

l1.calc_discount(40000,10)