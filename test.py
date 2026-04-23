import unittest
from item import Item
from sub_classes import Electronics, Vehicle, Furniture, Tool
from inventory import Inventory
from kursinis2 import Selected_Item, Order, Client

class TestItem(unittest.TestCase):
    def test_item_init(self):
        item = Item(1, "Test Item", 10.0, 5)
        self.assertEqual(item.id, 1)
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.price, 10.0)
        self.assertEqual(item.stock, 5)

    def test_total_value(self):
        item = Item(1, "Test Item", 10.0, 5)
        self.assertEqual(item.total_value, 50.0)

    def test_display_info(self):
        item = Item(1, "Test Item", 10.0, 5)
        expected = "1 Test Item Price: 10.0 Stock: 5"
        self.assertEqual(item.display_info(), expected)

class TestElectronics(unittest.TestCase):
    def test_electronics_init(self):
        elec = Electronics(1, "Laptop", 1200.0, 50, 2)
        self.assertEqual(elec.id, 1)
        self.assertEqual(elec.name, "Laptop")
        self.assertEqual(elec.price, 1200.0)
        self.assertEqual(elec.stock, 50)
        self.assertEqual(elec.warranty_years, 2)

    def test_display_info(self):
        elec = Electronics(1, "Laptop", 1200.0, 50, 2)
        expected = "1 Laptop Price: 1200.0 Stock: 50 Warranty: 2"
        self.assertEqual(elec.display_info(), expected)

class TestVehicle(unittest.TestCase):
    def test_vehicle_init(self):
        veh = Vehicle(4, "Car", 20000.0, 10, 2022, "Petrol", 5000)
        self.assertEqual(veh.id, 4)
        self.assertEqual(veh.name, "Car")
        self.assertEqual(veh.price, 20000.0)
        self.assertEqual(veh.stock, 10)
        self.assertEqual(veh.year, 2022)
        self.assertEqual(veh.fuel_type, "Petrol")
        self.assertEqual(veh.mileage, 5000)

    def test_display_info(self):
        veh = Vehicle(4, "Car", 20000.0, 10, 2022, "Petrol", 5000)
        expected = "4 Car Price: 20000.0 Stock: 10 Year: 2022 Fuel: Petrol Mileage: 5000"
        self.assertEqual(veh.display_info(), expected)

class TestFurniture(unittest.TestCase):
    def test_furniture_init(self):
        furn = Furniture(7, "Chair", 50.0, 200, "Wood", 5.0)
        self.assertEqual(furn.id, 7)
        self.assertEqual(furn.name, "Chair")
        self.assertEqual(furn.price, 50.0)
        self.assertEqual(furn.stock, 200)
        self.assertEqual(furn.material, "Wood")
        self.assertEqual(furn.weight, 5.0)

    def test_display_info(self):
        furn = Furniture(7, "Chair", 50.0, 200, "Wood", 5.0)
        expected = "7 Chair Price: 50.0 Stock: 200 Material: Wood Weight: 5.0 kg"
        self.assertEqual(furn.display_info(), expected)

class TestTool(unittest.TestCase):
    def test_tool_init(self):
        tool = Tool(10, "Hammer", 25.0, 300, "Hand Tool")
        self.assertEqual(tool.id, 10)
        self.assertEqual(tool.name, "Hammer")
        self.assertEqual(tool.price, 25.0)
        self.assertEqual(tool.stock, 300)
        self.assertEqual(tool.tool_type, "Hand Tool")

    def test_display_info(self):
        tool = Tool(10, "Hammer", 25.0, 300, "Hand Tool")
        expected = "10 Hammer Price: 25.0 Stock: 300 Type: Hand Tool"
        self.assertEqual(tool.display_info(), expected)

class TestInventory(unittest.TestCase):
    def setUp(self):
        Inventory._instance = None

    def test_singleton(self):
        inv1 = Inventory()
        inv2 = Inventory()
        self.assertIs(inv1, inv2)

    def test_add_item(self):
        inv = Inventory()
        item = Item(1, "Test", 10.0, 1)
        inv.add_item(item)
        self.assertIn(item, inv.items)

    def test_display_empty(self):
        inv = Inventory()
        self.assertEqual(inv.display(), "Inventory is empty.\n")

    def test_display_with_items(self):
        inv = Inventory()
        item1 = Item(1, "Item1", 10.0, 2)
        item2 = Item(2, "Item2", 20.0, 1)
        expected = ("1 Item1 Price: 10.0 Stock: 2\nValue: 20.0\n"
                    "2 Item2 Price: 20.0 Stock: 1\nValue: 20.0\n"
                    "Total inventory value: 40.0\n\n")
        self.assertEqual(inv.display(), expected)

class TestSelectedItem(unittest.TestCase):
    def test_selected_item_init(self):
        item = Item(1, "Test", 10.0, 5)
        sel_item = Selected_Item(item, 3)
        self.assertEqual(sel_item.item, item)
        self.assertEqual(sel_item.quantity, 3)

    def test_sub_total(self):
        item = Item(1, "Test", 10.0, 5)
        sel_item = Selected_Item(item, 3)
        self.assertEqual(sel_item.sub_total, 30.0)

class TestOrder(unittest.TestCase):
    def test_order_init(self):
        order = Order()
        self.assertEqual(order.selected_items, [])

    def test_add_item(self):
        order = Order()
        item = Item(1, "Test", 10.0, 5)
        order.add_item(item, 2)
        self.assertEqual(len(order.selected_items), 1)
        self.assertEqual(order.selected_items[0].item, item)
        self.assertEqual(order.selected_items[0].quantity, 2)

    def test_total_price(self):
        order = Order()
        item1 = Item(1, "Test1", 10.0, 5)
        item2 = Item(2, "Test2", 20.0, 5)
        order.add_item(item1, 1)
        order.add_item(item2, 2)
        self.assertEqual(order.total_price, 50.0)

class TestClient(unittest.TestCase):
    def test_client_init(self):
        client = Client("John")
        self.assertEqual(client.name, "John")

    def test_name_setter(self):
        client = Client("John")
        client.name = "Jane"
        self.assertEqual(client.name, "Jane")

    def test_order_item(self):
        client = Client("John")
        item = Item(1, "Test", 10.0, 5)
        client.order_item(item, 3)
        self.assertEqual(len(client._order.selected_items), 1)

    def test_view_order_empty(self):
        client = Client("John")
        self.assertEqual(client.view_order(), "Empty cart\n")

    def test_view_order_with_items(self):
        client = Client("John")
        item = Item(1, "Test", 10.0, 5)
        client.order_item(item, 2)
        expected = "Order of John contains:\nTest Price: 10.0 Quantity: 2\n"
        self.assertEqual(client.view_order(), expected)

    def test_complete_order(self):
        client = Client("John")
        item = Item(1, "Test", 10.0, 5)
        client.order_item(item, 2)
        expected = "John order final price: 20.0\n"
        self.assertEqual(client.complete_order(), expected)

if __name__ == '__main__':
    unittest.main()