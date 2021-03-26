class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []
        self.count = 0

    def add_item(self, item):
        if self.count < self.__capacity:
            self.count += 1
            self.items.append(item)
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        result = ""
        result += f"Items: {', '.join(self.items)}"
        result += "."
        result += f"\nCapacity left: {self.__capacity - self.count}"
        return result


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

