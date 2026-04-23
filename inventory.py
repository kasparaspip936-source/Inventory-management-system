class Inventory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.items = []
        return cls._instance

    def add_item(self, item):
        self.items.append(item)

    def display(self):
        if not self.items:
            return "Inventory is empty.\n"
        total=0
        result = ""
        for item in self.items:
            result += item.display_info() + "\n"
            result += f"Value: {item.total_value}\n"
            total+=item.total_value
        result += f"Total inventory value: {total}\n\n"
        return result


inv1 = Inventory()
inv2 = Inventory()

print(inv1 is inv2)