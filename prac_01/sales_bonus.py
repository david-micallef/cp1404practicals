"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

def main():
    sales_amount = enter_sales_amount()
    calculate_bonus(sales_amount)
    while sales_amount >= 0:
        sales_amount = enter_sales_amount()
        calculate_bonus(sales_amount)

def calculate_bonus(sales_amount):
    if 0 <= sales_amount < 1000:
        bonus_amount = sales_amount * 0.10
        print("Your bonus amount is: ${:.2f}".format(bonus_amount)+ "\n")
    elif sales_amount >= 1000:
        bonus_amount = sales_amount * 0.15
        print("Your bonus amount is: ${:.2f}".format(bonus_amount)+ "\n")
    else:
        print("You have entered a negative number.")

def enter_sales_amount():
    sales_amount = float(input("Please enter your sales amount: $"))
    return sales_amount

main()