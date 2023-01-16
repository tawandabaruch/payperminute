import time


# Initialize variables
start_time = time.time()
price_per_minute = 0.05
total_cost = 0.0

# Start timer
while True:
    elapsed_time = time.time() - start_time
    elapsed_minutes = int(elapsed_time / 60)
    cost = elapsed_minutes * price_per_minute
    total_cost += cost

    print(f'Elapsed Time: {elapsed_minutes} minutes')
    print(f'Total Cost: {total_cost}')
    print()

    time.sleep(60)
