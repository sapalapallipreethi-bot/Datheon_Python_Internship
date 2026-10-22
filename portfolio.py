import csv
import yfinance as yf

# Load the complete company dataset provided for the task
try:
    with open("sp500_companies.csv", "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        companies = {
            row["Symbol"].strip().upper(): row
            for row in reader
            if row.get("Symbol")
        }
except FileNotFoundError:
    print("Error: sp500_companies.csv was not found.")
    print("Place it in the same folder as portfolio.py.")
    raise SystemExit(1)

if not companies:
    print("Error: No company records found in sp500_companies.csv.")
    raise SystemExit(1)

portfolio = []

print("=" * 60)
print("       STOCK PORTFOLIO PERFORMANCE TRACKER")
print("=" * 60)
print(f"Loaded {len(companies)} companies from the dataset.")
print("Current prices are retrieved using Yahoo Finance.")
print("Prices may be delayed or unavailable.\n")

while True:
    ticker = input("Enter stock ticker (or DONE to finish): ").strip().upper()

    if ticker == "DONE":
        break

    if not ticker:
        print("Please enter a ticker symbol.")
        continue

    # Validate the ticker against the supplied company dataset
    if ticker not in companies:
        print(f"{ticker} is not listed in sp500_companies.csv.")
        print("Please enter a valid Symbol from the dataset.\n")
        continue

    company = companies[ticker]

    try:
        buy_price = float(input("Enter buy price per share ($): "))
        quantity = int(input("Enter number of shares: "))

        if buy_price <= 0 or quantity <= 0:
            print("Price and quantity must be positive.\n")
            continue

    except ValueError:
        print("Enter a valid price and whole number of shares.\n")
        continue

    try:
        # Yahoo Finance uses hyphens for some tickers containing periods
        yahoo_ticker = ticker.replace(".", "-")
        stock = yf.Ticker(yahoo_ticker)
        history = stock.history(period="5d", interval="1d")

        if history.empty or history["Close"].dropna().empty:
            print(f"Could not retrieve a price for {ticker}. Try again.\n")
            continue

        current_price = float(history["Close"].dropna().iloc[-1])

        invested = buy_price * quantity
        market_value = current_price * quantity
        profit_loss = market_value - invested
        percent_change = (profit_loss / invested) * 100

        portfolio.append({
            "Symbol": company["Symbol"],
            "Security": company["Security"],
            "GICS Sector": company["GICS Sector"],
            "GICS Sub-Industry": company["GICS Sub-Industry"],
            "Headquarters Location": company["Headquarters Location"],
            "Date added": company["Date added"],
            "CIK": company["CIK"],
            "Founded": company["Founded"],
            "Buy Price": round(buy_price, 2),
            "Quantity": quantity,
            "Current Price": round(current_price, 2),
            "Invested Amount": round(invested, 2),
            "Market Value": round(market_value, 2),
            "Profit/Loss": round(profit_loss, 2),
            "Gain/Loss (%)": round(percent_change, 2)
        })

        print(f"Company: {company['Security']}")
        print(f"Latest available close for {ticker}: ${current_price:.2f}\n")

    except Exception as error:
        print(f"Price lookup failed for {ticker}: {error}")
        print("Check your internet connection and try again.\n")

if not portfolio:
    print("No stock data to save.")
else:
    total_invested = sum(item["Invested Amount"] for item in portfolio)
    total_value = sum(item["Market Value"] for item in portfolio)
    total_profit_loss = total_value - total_invested
    total_percent = (
        total_profit_loss / total_invested * 100
        if total_invested else 0
    )

    print("\n" + "=" * 60)
    print("PORTFOLIO SUMMARY")
    print("=" * 60)

    for item in portfolio:
        print(f"\nStock: {item['Security']} ({item['Symbol']})")
        print(f"Invested: ${item['Invested Amount']:.2f}")
        print(f"Market value: ${item['Market Value']:.2f}")
        print(f"Profit/Loss: ${item['Profit/Loss']:.2f}")
        print(f"Gain/Loss: {item['Gain/Loss (%)']:.2f}%")

    print("\n" + "-" * 60)
    print(f"Total invested: ${total_invested:.2f}")
    print(f"Total market value: ${total_value:.2f}")
    print(f"Total Profit/Loss: ${total_profit_loss:.2f}")
    print(f"Total Gain/Loss: {total_percent:.2f}%")

    output_fields = [
        "Symbol",
        "Security",
        "GICS Sector",
        "GICS Sub-Industry",
        "Headquarters Location",
        "Date added",
        "CIK",
        "Founded",
        "Buy Price",
        "Quantity",
        "Current Price",
        "Invested Amount",
        "Market Value",
        "Profit/Loss",
        "Gain/Loss (%)"
    ]

    with open(
        "portfolio_summary.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=output_fields)
        writer.writeheader()
        writer.writerows(portfolio)

    print("\nResults saved to portfolio_summary.csv")