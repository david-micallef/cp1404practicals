def main():
    print(("Electricity bill estimator") + "\n")
    cents_per_kWh = float(input("Enter cents per kWh: "))
    daily_use_kWh = float(input("Enter daily use in kWh: "))
    number_of_billing_days = int(input("Enter number of billing days: "))
    estimated_bill = (cents_per_kWh / 100) * daily_use_kWh * number_of_billing_days
    print("\n" + ("Estimated bill: ${:.2f}".format(estimated_bill)))

main()
