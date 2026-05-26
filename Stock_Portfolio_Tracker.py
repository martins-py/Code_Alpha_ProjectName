#stock portfolio tracker

stock_prices ={
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOG" : 140,
    "MSFT" : 300
}
for stock in stock_prices:
    print(stock)
user_input = int(input("How many stocks do you want to add? "))
total_investment = 0
for i in range(user_input):
    stock_name=input("Enter stock name: ").upper()
    quantity = int(input("Enter Quantity: "))
    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment+=investment
        print(f"{stock_name} investment = ${investment}")
    else:
        print(f"{stock_name} not found")
    print(f"Total investment = ${total_investment}")

with open("portfolio.txt", "w") as file:
    file.write(f"Total investment = ${total_investment}")
print("result has been saved to portfolio.txt")
