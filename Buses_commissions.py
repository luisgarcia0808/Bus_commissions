# This is a weekly Bus Revenue and Split Calculator
# Is useful for calculate weekly revenue for multiple buses and splits earnings between the driver and the bus owner; i use 30% and 70%, but everyone can use anothers %.

print("This program calculates weekly bus earnings and distributes the shares: 30% for the driver and 70% for the owner.")

# Validation for the total number of buses
while True:
    try:
        num_buses = int(input("Enter the number of buses to calculate earnings for: "))
        if num_buses <= 0:
            print("Invalid number of buses. Please enter a number greater than 0.")
            continue
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# In this point the code Iterate over each bus to collect daily revenues
for b in range(num_buses):
    daily_earnings = []  # Initialize empty list to store daily amounts
    
    # Input validation for the number of operational days (1 to 7)
    while True:
        try:
            num_days = int(input(f"Enter the number of working days for bus {b + 1}: "))
            if num_days <= 0 or num_days > 7:
                print("Invalid number of days. Please enter a number between 1 and 7.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Collect earnings for each operational day
    for d in range(num_days):
        while True:
            try:
                amount = float(input(f"Enter the earnings for day {d + 1}: "))
                if amount < 0:
                    print("Negative amounts cannot be processed. Please enter a positive value.")
                else:
                    daily_earnings.append(amount)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # This is for compute totals and percentage distribution
    total_revenue = sum(daily_earnings)
    driver_share = float(total_revenue * 0.30)
    owner_share = float(total_revenue * 0.70)

    # Finally display the calculated results using formatted concatenation
    print("\n--- Summary for Bus " + str(b + 1) + " ---")
    print(f"Total weekly earnings for bus {b + 1}: ${total_revenue:.2f}")
    print(f"Driver's weekly earnings (30%): ${driver_share:.2f}")
    print(f"Owner's weekly revenue (70%): ${owner_share:.2f}\n")