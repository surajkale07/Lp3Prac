class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # value-to-weight ratio

def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0  # Total value of knapsack
    for i in items:
        if capacity >= i.weight:
            # If we can take the whole item
            capacity -= i.weight
            total_value += i.value
        else:
            # Take only a fraction of the remaining item
            total_value += i.ratio * capacity
            break  # Knapsack is now full

    return total_value

# Example usage
if __name__ == "__main__":
    # Input: list of (value, weight) pairs and knapsack capacity
    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30)
    ]
    capacity = 50

    max_value = fractional_knapsack(items, capacity)
    print(f"Maximum value in knapsack: {max_value:.2f}")
