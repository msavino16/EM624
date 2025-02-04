while True:
    dollars = input("How many US Dollars do you want to exchange? If you want to exit type 'done' \n")
    if dollars.lower == "done":
        break

    if not dollars.isdigit():
        print("That is not a number, try again")
        continue

    currency = input("Enter the name of the currency you are converting dollars to:\n")

    if currency.isdigit():
        print("That is not valid, please try again")
        continue

    rate = input("What is the exchange rate?\n")

    if not rate.isdigit():
        print("That is not a number, try again")
        continue

    print(f"You can exchange {dollars} U.S. dollars for {float(dollars)*float(rate)} {currency}")


    break