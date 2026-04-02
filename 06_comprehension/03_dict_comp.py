tea_prices_inr = {
    "Masala chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 100
}

tea_prices = {tea:price / 90 for tea, price in tea_prices_inr.items()}
print(f"Tea prices in USD : {tea_prices}")