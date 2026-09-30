stock_prices = {
    "TCS": 4000,
    "INFY": 2000,
    "RELIANCE": 2500,
    "HDFCBANK": 1600,
    "ITC": 400
}

total_investment = 0

print("="*30)
print("     STOCK PORTFOLIO TRACKER")
print("="*30)

print("\nAvailable stocks:")

for stock, price in stock_prices.items():
    print(stock, "-", price)

while True:
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]
    investment = price * quantity

    total_investment += investment

    print(stock_name, ":", quantity, "x", price, "=", investment)

    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("="*30)
print("Total investment:", total_investment)
print("="*30)