class Products:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Products.count += 1

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price} ")

    @classmethod
    def get_count(cls):
        print(f"Total products in store = {cls.count}")

    @staticmethod
    def calc_discount(price,discount):
        print(f"Discounted Price = { price - (price * discount/ 100)}")

p1 = Products("Phone", 10_000)
p2 = Products("Laptop", 50_000)
p3 = Products("Pen", 5)

p1.get_info() 
Products.get_count()
p1.calc_discount(p1.price, 12)     
