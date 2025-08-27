def double_penny(days):
    total_value = 0.01  # Initial value of a penny
    for day in range(1, days + 1):
        total_value *= 2  # Double the value each day
    return total_value

# Calculate the value after 30 days
value_after_30_days = double_penny(30)
print(f"The value of the penny after 30 days is ${value_after_30_days:,.2f}")