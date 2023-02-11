import time

# Video call price per minute
price = 0.5

# User account balance
balance = 3.0

if balance < price:
    print("Insufficient funds. Please add more money to your account.")
else:
    print("Starting video call...")
    start_time = time.time()

    # Simulating the video call
    call_duration = 120  # 2 minutes
    current_time = time.time()
    elapsed_time = current_time - start_time

    while elapsed_time < call_duration:
        time.sleep(1)
        current_time = time.time()
        elapsed_time = current_time - start_time
        total_cost = price * (elapsed_time / 60)
        print("Elapsed time: " + str(elapsed_time) + " seconds")
        print("Price: $" + str(total_cost))
        if balance - total_cost < 0:
            print("Insufficient funds. The video call was cut off.")
            break

    # Checking if the balance is still sufficient
    if balance - total_cost >= 0:
        # Deducting the total cost from the balance
        balance -= total_cost

        # Printing the result
        print("Total cost: $" + str(total_cost))
        print("Remaining balance: $" + str(balance))

