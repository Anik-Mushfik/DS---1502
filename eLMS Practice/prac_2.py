#(b)
class Pastry:
    def __init__(self, weight, per_kg_price, type):
        self.weight = weight
        self.per_kg_price = per_kg_price
        self.type = type
        self.total_price = 0

#(c)
    def add_frosting(self, type):
        if (type == "Butter Cream"):
            self.total_price += 400
        elif (type == "Whipped Cream"):
            self.total_price += 200
        else:
            print(f"Frosting not available!!!")

    def total_cost(self):
        self.total_price += self.weight*self.per_kg_price

class Chocolate(Pastry):
    def __init__(self, weight, per_kg_price):
        self.type = "Chocolate"
        super().__init__(weight, per_kg_price, self.type)

class Vanilla(Pastry):
    def __init__(self, weight, per_kg_price):
        self.type = "Vanilla"
        super().__init__(weight, per_kg_price, self.type)


class Order:
    def __init__(self, type, quantity, weight):
        self.pastry_type = type
        self.quantity = quantity
        self.weight = weight
        self.total_price = 0
        