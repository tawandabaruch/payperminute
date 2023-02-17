import time

# Video call price per minute
price = 2.0

# User account balance
balance = 3.0

# Check if the user has sufficient funds in their account
if balance < price:
    print("Insufficient funds. Please add more money to your account.")
else:
    print("Starting video call...")
    start_time = time.time()

    # Simulate the video call by looping for the duration of the call
    call_duration = 120  # 2 minutes
    current_time = time.time()
    elapsed_time = current_time - start_time

    # Loop until the call duration has been reached or the user runs out of funds
    while elapsed_time < call_duration:
        # Wait for 1 second to simulate the passage of time during the call
        time.sleep(1)

        # Calculate the elapsed time and the total cost of the call so far
        current_time = time.time()
        elapsed_time = current_time - start_time
        total_cost = price * (elapsed_time / 60)

        # Print the elapsed time and the total cost of the call so far
        print("Elapsed time: " + str(elapsed_time) + " seconds")
        print("Price: $" + str(total_cost))

        # Check if the user has enough funds to continue the call
        if balance - total_cost < 0:
            print("Insufficient funds. The video call was cut off.")
            break

    # If the user still has enough funds, deduct the cost of the call from their balance
    if balance - total_cost >= 0:
        balance -= total_cost

        # Print the total cost of the call and the remaining balance
        print("Total cost: $" + str(total_cost))
        print("Remaining balance: $" + str(balance))
