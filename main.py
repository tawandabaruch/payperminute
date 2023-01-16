import time

# Video call price
price = 0.5

# User account balance
balance = 3.0


if balance < price:
    print("Insufficient funds. Please add more money to your account.")
else:
    print("Starting video call...")
    start_time = time.time()

    end_time = time.time()
    elapsed_time = end_time - start_time
    total_cost = price * (elapsed_time / 60)
    print("Total cost: $" + str(total_cost))
    print("Elapsed time: " + str(elapsed_time) + " seconds")
