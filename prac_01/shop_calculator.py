def main():
    total_price_amount = 0
    number_of_items = entering_number_of_items()
    total_price_amount = entering_price_of_items(number_of_items, total_price_amount)
    discount_price_amount = calculate_discount(total_price_amount)
    total_amount_with_discount = total_price_amount - discount_price_amount
    print("Total price for", number_of_items, "items is ${:.2f}".format(total_amount_with_discount))

def calculate_discount(total_price_amount):
    if total_price_amount > 100:
        discount_price_amount = total_price_amount * 0.10
    else:
        discount_price_amount = 0
    return (discount_price_amount)

def entering_number_of_items():
    number_of_items = int(input("Number of items: "))
    while number_of_items <= 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
    return (number_of_items)

def entering_price_of_items(number_of_items, total_price_amount):
    for i in range(number_of_items):
        price_of_item = float(input("Price of item: "))
        total_price_amount += price_of_item
    return (total_price_amount)

main()