class Manufacturer:
    def __init__(self, identity, location):
        self.identity = identity
        self.location = location
    
    def describe(self):
        print(f"Identity: {self.identity} - Location: {self.location}")
    
class Device:
    def __init__(self, name, price, identity, location):
        self.name = name
        self.price = price
        self.manufacturer = Manufacturer(identity, location)
    
    def describe(self):
        print(f"Name: {self.name} - Price: {self.price}")
        self.manufacturer.describe()  

# Tạo các thiết bị
device1 = Device(name="mouse", price=2.5, identity=9725, location="Vietnam")
device1.describe()

device2 = Device(name="monitor", price=12.5, identity=11, location="Germany")
device2.describe()
