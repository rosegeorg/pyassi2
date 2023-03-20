import random
print("Welcome to Programming Principles Sample Product Inventory ")


class Product:
    def __init__(self,code, name,current_stock,manufacture_cost, sale_price, monthly_production):
        self.code = code
        self.name = name
        self.current_stock = current_stock
        self.manufacture_cost = manufacture_cost
        self.sale_price = sale_price
        self.monthly_production = monthly_production
        self.stock = 0
        self.total_units_manufactured = 0
        self.total_units_sold = 0
        self.net_profit = 0

    def simulate_production_and_sales(self, num_months):
        print("\n\n********Programming Principles Sampple Stock Statement********")
        print("\n-------------------------")
        for month in range(num_months):
            units_sold = random.randint(
                self.monthly_production - 10, self.monthly_production + 10)
            self.stock += self.monthly_production - units_sold
            self.total_units_manufactured += self.monthly_production
            self.total_units_sold += units_sold
            self.net_profit = self.total_units_sold * self.sale_price - \
                self.total_units_manufactured * self.manufacture_cost
            print(f"Month {month+1}:")
            print(
                f"  |             Units Manufactured: {self.monthly_production}")
            print(f"  |            Units Sold: {units_sold}")
            print(f"  |             Stock: {self.stock}")
            print(f"  |             Net Profit: {self.net_profit}")
            print("-------------------------")

code=int(input("please enter the product code: "))
product_name = input("Enter product name: ")
current_stock = int(input("Enter current stock: "))
manufacture_cost = float(input("Enter manufacture cost: "))
sale_price = float(input("Enter sale price: "))
monthly_production = int(input("Enter estimated monthly production: "))

product = Product(code, product_name, current_stock, manufacture_cost,
                  sale_price, monthly_production)
product.simulate_production_and_sales(12)

