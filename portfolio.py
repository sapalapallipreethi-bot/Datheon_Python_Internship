
import csv

# Sample prices for practice only (not live market prices)
stock_prices = {
    "AAPL": 230.00,
    "MSFT": 510.00,
    "GOOGL": 250.00,
    "AMZN": 220.00,
    "NVDA": 180.00
}

portfolio = []

print("=" * 55)
print("       STOCK PORTFOLIO PERFORMANCE TRACKER")
print("=" * 55)
print("Sample prices only — not real-time market data.\n")

while True:
    ticker = input("Enter stock ticker (or DONE to finish): ").strip().upper()

    if ticker == "DONE":
        break

    if ticker not in stock_prices:
        print("Ticker not in sample list. Choose AAPL, MSFT, GOOGL, AMZN, NVDA.")
        continue

    try:
        buy_price = float(input("Enter buy price per share ($): "))
        quantity = int(input("Enter number of shares: "))

        if buy_price <= 0 or quantity <= 0:
            print("Buy price and quantity must be positive.")
            continue

    except ValueError:
        print("Please enter a valid price and whole number of shares.")
        continue

    current_price = stock_prices[ticker]
    invested = buy_price * quantity
    market_value = current_price * quantity
    profit_loss = market_value - invested
    percent_change = (profit_loss / invested) * 100

    portfolio.append({
        "Ticker": ticker,
        "Buy Price": buy_price,
        "Quantity": quantity,
        "Sample Current Price": current_price,
        "Invested Amount": invested,
        "Market Value": market_value,
        "Profit/Loss": profit_loss,
        "Gain/Loss (%)": percent_change
    })

if not portfolio:
    print("\nNo stocks entered. Nothing to save.")
else:
    total_invested = sum(item["Invested Amount"] for item in portfolio)
    total_value = sum(item["Market Value"] for item in portfolio)
    total_profit_loss = total_value - total_invested
    total_percent = (total_profit_loss / total_invested) * 100

    print("\n" + "=" * 55)
    print("PORTFOLIO SUMMARY")
    print("=" * 55)

    for item in portfolio:
        print(f"\nStock: {item['Ticker']}")
        print(f"Invested: ${item['Invested Amount']:.2f}")
        print(f"Sample market value: ${item['Market Value']:.2f}")
        print(f"Profit/Loss: ${item['Profit/Loss']:.2f}")
        print(f"Gain/Loss: {item['Gain/Loss (%)']:.2f}%")

    print("\n" + "-" * 55)
    print(f"Total invested: ${total_invested:.2f}")
    print(f"Total sample value: ${total_value:.2f}")
    print(f"Total Profit/Loss: ${total_profit_loss:.2f}")
    print(f"Total Gain/Loss: {total_percent:.2f}%")

    filename = "portfolio_summary.csv"
    fieldnames = list(portfolio[0].keys())

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(portfolio)

    print(f"\nResults saved to {filename}")
