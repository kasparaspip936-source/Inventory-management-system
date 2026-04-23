from item import Item

class Electronics(Item):
    def __init__(self, id, name, price, stock, warranty_years):
        super().__init__(id, name, price, stock)
        self.warranty_years=warranty_years

    def display_info(self):
        return super().display_info() + f" Warranty: {self.warranty_years}"

class Vehicle(Item):
    def __init__(self, id, name, price, stock, year, fuel_type, mileage):
        super().__init__(id, name, price, stock)
        self.year = year
        self.fuel_type = fuel_type
        self.mileage = mileage
    
    def display_info(self):
        return super().display_info() + f" Year: {self.year} Fuel: {self.fuel_type} Mileage: {self.mileage}"

class Furniture(Item):
    def __init__(self, id, name, price, stock, material, weight):
        super().__init__(id, name, price, stock)
        self.material = material
        self.weight = weight
    
    def display_info(self):
        return super().display_info() + f" Material: {self.material} Weight: {self.weight} kg"

class Tool(Item):
    def __init__(self, id, name, price, stock, tool_type):
        super().__init__(id, name, price, stock)
        self.tool_type = tool_type
    
    def display_info(self):
        return super().display_info() + f" Type: {self.tool_type}"