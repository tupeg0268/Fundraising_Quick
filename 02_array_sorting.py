expense_list = [['White Mug', 1.0], ['Printing', 0.75], ['Packaging', 0.5]]

# sorted by cost...
expense_list.sort(key=lambda x: x[1])

# Output...
print("**** Item by Cost <Most Expensive to least Expensive> ****")
for item in expense_list:
    print("{} : ${:.2f}" .format(item[0], item[1]))

print()

# Sort alphabetically
expense_list.sort(key=lambda x: x[0])

print("**** Items <Alphabetically> ****")
for item in expense_list:
    print("{}: ${:>2f}" .format(item[0], item[1]))