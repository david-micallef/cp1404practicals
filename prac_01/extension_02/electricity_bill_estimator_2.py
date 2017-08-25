TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

def main():
    print(("Electricity bill estimator 2.0") + "\n")
    customers_tariff = tariff_option()
    daily_use_kWh = float(input("Enter daily use in kWh: "))
    number_of_billing_days = int(input("Enter number of billing days: "))
    estimated_bill = customers_tariff * daily_use_kWh * number_of_billing_days
    print("\n" + ("Estimated bill: ${:.2f}".format(estimated_bill)))

def tariff_option():
    tariff_number = 0
    while tariff_number != 11 and tariff_number != 31:
        tariff_number = int(input("Which tariff? 11 or 31: "))
        if tariff_number == 11:
            customers_tariff = TARIFF_11
        elif tariff_number == 31:
            customers_tariff = TARIFF_31
        else:
            print("Invalid choice.")
    return (customers_tariff)

main()