from inventory import Inventory

class Item:
    def __init__(self,id,name,price,stock):
        self.id=id
        self.name=name
        self.price=price
        self.stock=stock

        Inventory().add_item(self)

    @property
    def total_value(self):
        return self.price * self.stock
    
    def display_info(self):
        return f"{self.id} {self.name} Price: {self.price} Stock: {self.stock}"