# Initialise lists
item_cost = []
expenses = []

# Get inputs and add to item_cost list
item = ""
while item.lower() != "xxx":
    item_cost = []
    item = input("Item Name: ")

    # If the user enters the exit code, Break out of the loop
    if item.lower() == "xxx":
        break

    # Get the cost (replace with number checking functions in due course
    cost = float(input("Item Cost: $"))

    # Add item name and the cost to 'item' list
    item_cost.append(item)
    item_cost.append(cost)

    # add item and cost to expense list
    expenses.append (item_cost)

print(expenses)