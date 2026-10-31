
# SMART CANTEEN BILLING AND ORDER ANALYZER
# Python Mini Project - Module 2 (Control Flow)


# Menu items and their prices
item_names = ["Veg Sandwich", "Masala Dosa", "Chole Rice", "Paneer Roll", "Tea"]
item_prices = [60, 80, 90, 100, 20]


# Function to display menu
def show_menu():

    print("\n========== SMART CANTEEN ==========")

    for i in range(5):
        print(i + 1, ".", item_names[i], "- Rs.", item_prices[i])


# Function to take customer order
def take_one_order():

    quantities = [0, 0, 0, 0, 0]
    subtotal = 0

    show_menu()

    # Take orders until customer finishes
    while True:

        choice = input("\nChoose item number (1-5): ")

        # Validate item number
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        item_number = int(choice)

        if item_number < 1 or item_number > 5:
            print("Invalid item number. Choose between 1 and 5.")
            continue

        # Enter quantity
        quantity_text = input("Enter quantity: ")

        if not quantity_text.isdigit():
            print("Please enter a valid quantity.")
            continue

        quantity = int(quantity_text)

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        # Calculate item price
        index = item_number - 1

        line_cost = item_prices[index] * quantity

        quantities[index] = quantities[index] + quantity

        subtotal = subtotal + line_cost

        print("Added:", item_names[index], "x", quantity,
              "= Rs.", format(line_cost, ".2f"))

        # Ask for another item
        again = input("Add another item? (y/n): ").lower()

        if again == "n":
            break

        elif again == "y":
            continue

        else:
            print("Invalid choice. Continuing order.")


    # Check whether any item was ordered
    if subtotal == 0:

        print("\nNo order was placed.")
        return


    # Calculate discount
    if subtotal >= 500:

        discount_rate = 0.10

    elif subtotal >= 250:

        discount_rate = 0.05

    else:

        discount_rate = 0


    discount = subtotal * discount_rate

    final_total = subtotal - discount


    # Print final receipt
    print("\n========== RECEIPT ==========")

    print("Items ordered:")

    for i in range(5):

        if quantities[i] > 0:

            line_cost = item_prices[i] * quantities[i]

            print(item_names[i], "x", quantities[i],
                  ": Rs.", format(line_cost, ".2f"))


    print("------------------------------")

    print("Subtotal: Rs.", format(subtotal, ".2f"))

    print("Discount: Rs.", format(discount, ".2f"))

    print("Final total: Rs.", format(final_total, ".2f"))

    print("Thank you!")


# MAIN PROGRAM

print("Welcome to the Smart Canteen!")


# Allow multiple customer orders
while True:

    take_one_order()

    another_order = input(
        "\nTake another customer's order? (y/n): "
    ).lower()

    if another_order == "n":

        print("\nCanteen is closed. Have a nice day!")

        break

    elif another_order == "y":

        continue

    else:

        print("Invalid choice. Program finished.")

        break
