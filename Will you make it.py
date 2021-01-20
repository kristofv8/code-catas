def zero_fuel(distance_to_pump, mpg, fuel_left):
    range_reachable = mpg * fuel_left
    if distance_to_pump >= range_reachable:
        return False
    if distance_to_pump <= range_reachable:
        return True


range = zero_fuel(50, 25, 2)
print(range)

