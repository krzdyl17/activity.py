class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Year: {self.year}")

car1 = Car("Honda", "Civic SiR", 1998)
car2 = Car("Nissan", "R34 GT-R", 1999)

car1.display_info()
print()
car2.display_info()
