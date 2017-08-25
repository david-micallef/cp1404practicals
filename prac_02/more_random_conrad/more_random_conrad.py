"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at a random number between $5.00 to $10.00, and, at the end of every day there is
a 50% chance it increases by 10% to 17.5%, and
a 50% chance that it decreases by 2.5% to 5%.
If the price rises above a random number between $95 to $115, or falls below a random number between $1 to $4, 
the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = random.uniform(0.1, 0.175)
MAX_DECREASE = random.uniform(0.025, 0.05)
MIN_PRICE = random.randint(1, 4)
MAX_PRICE = random.randint(95, 115)
INITIAL_PRICE = random.randint(5, 10)

out_file = open("extension_conrad.txt", "w")

day = 0
price = INITIAL_PRICE
print("Starting price: ${:,.2f}".format(price), file=out_file)

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    day += 1
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("On day {} price is: ${:,.2f}".format(day, price), file=out_file)

out_file.close()
