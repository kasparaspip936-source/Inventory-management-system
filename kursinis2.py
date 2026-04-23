from inventory import Inventory
from sub_classes import Electronics, Vehicle, Furniture, Tool


class Selected_Item:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity
    
    @property
    def sub_total(self):
        return self.item.price * self.quantity

class Order:
    def __init__(self):
        self.selected_items = []
    
    def add_item(self, item, quantity):
        item=Selected_Item(item, quantity)
        self.selected_items.append(item)
    
    @property
    def total_price(self):
        return sum(item.sub_total for item in self.selected_items)

    def Order_info(self):
        for item in self.selected_items:
            item.item.display_info()
            print(item.item.name, " Value:", item.item.price, " Quantity:", item.quantity, " Subtotal:", item.sub_total)
        print(" Total:", self.total_price)
    
class Client:
    def __init__(self,name):
        self.name=name
        self._order=Order()

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name=value
        
    def order_item(self,item,quantity):
        self._order.add_item(item,quantity)

    def view_order(self):
        if self._order.selected_items==[]: 
            return "Empty cart\n"
        result = f"Order of {self._name} contains:\n"
        for item in self._order.selected_items:
            result += f"{item.item.name} Price: {item.item.price} Quantity: {item.quantity}\n"
        return result

    def complete_order(self):
        return f"{self.name} order final price: {self._order.total_price}\n"

electronics_list = []
vehicle_list = []
furniture_list = []
tool_list = []
client_list = []

filer = open("data.txt","r")
for line in filer:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        t = parts[0]

        if t == "Electronics":
            obj = Electronics(int(parts[1]), parts[2], float(parts[3]), int(parts[4]), int(parts[5]))
            electronics_list.append(obj)

        elif t == "Vehicle":
            obj = Vehicle(int(parts[1]), parts[2], float(parts[3]), int(parts[4]),
                          int(parts[5]), parts[6], int(parts[7]))
            vehicle_list.append(obj)

        elif t == "Furniture":
            obj = Furniture(int(parts[1]), parts[2], float(parts[3]), int(parts[4]),
                            parts[5], float(parts[6]))
            furniture_list.append(obj)

        elif t == "Tool":
            obj = Tool(int(parts[1]), parts[2], float(parts[3]), int(parts[4]), parts[5])
            tool_list.append(obj)

        elif t == "Client":
            obj = Client(parts[1])
            client_list.append(obj)
filer.close()

client1 = client_list[0]
client2 = client_list[1]
client3 = client_list[2]

client1.order_item(electronics_list[0], 2)
client1.order_item(tool_list[1], 5)

client2.order_item(electronics_list[1], 3)
client2.order_item(furniture_list[0], 10)

client3.order_item(vehicle_list[0], 1)
client3.order_item(electronics_list[2], 1)

filew = open("rez.txt","w")
filew.write(Inventory().display())
for client in client_list:
    filew.write(client.view_order())
for client in client_list:
    filew.write(client.complete_order())    
filew.close()
