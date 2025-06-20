# 1. Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 310
}

portfolio = {}
total_investment = 0

print("📈 Welcome to the Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

# 2. User input loop
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("⚠️ Invalid stock symbol. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity < 0:
            raise ValueError
    except ValueError:
        print("⚠️ Please enter a valid positive integer.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_investment += stock_prices[stock] * quantity

# 3. Display results
print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock} - {qty} shares @ ${stock_prices[stock]} = ${value}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# 4. Optional: Save to file
save = input("Do you want to save this report to a file? (y/n): ").lower()
if save == "y":
    filename = "portfolio_report.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("📊 Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            f.write(f"{stock} - {qty} shares @ ${stock_prices[stock]} = ${value}\n")
        f.write(f"\n💰 Total Investment Value: ${total_investment}\n")
    print(f"✅ Report saved to {filename}")
