tickets = int(input("Enter the number of tickets: "))
if tickets < 5 or tickets > 40:
    print("Minimum of 5 and Maximum of 40 tickets allowed")
else:
    ref = input("Do you want any refreshment (y/n): ").strip().lower()
    cou = input("Do you have any coupon code (y/n): ").strip().lower()
    circle = input("Enter the circle (k for 75 or q for 150): ").strip().lower()

    # Ticket prices for each circle
    price_k = 75
    price_q = 150

    # Determine ticket cost based on the circle
    if circle == "k":
        cost = price_k * tickets
    elif circle == "q":
        cost = price_q * tickets
    else:
        print("Invalid circle input")
        cost = 0

    if cost > 0:  # Only proceed if the circle input is valid
        # Apply discount for more than 20 tickets
        if tickets > 20:
            cost = cost - (0.1 * cost)

        # Add refreshment cost if selected
        if ref == "y":
            cost += tickets * 50  # 50 per ticket for refreshment

        # Apply coupon discount if selected
        if cou == "y":
            cost = cost - (0.02 * cost)

        print("Ticket cost:", format(cost, ".2f"))
