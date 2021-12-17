# Make a list named sandwich_order and fill it with
# the names of various sandwiches. Then make an
# empty list named finished_sandwiches. Loop
# through the list of sandwich orders and print a
# message for each order, such as "I made your tuna
# sandwich." After all the sandwiches have been made,
# print a message listing each sandwich that was
# made.
sandwich_orders = [
    "tuna sandwich",
    "turkey sandwich",
    "chicken sandwich",
    "steak sandwich",
]
finished_sandwiches = []

for sandwich_order in sandwich_orders:
    print(f"\nI made your {sandwich_order} sandwich.")
    finished_sandwiches.append(sandwich_order)

print(f"\nHere is a list of your {finished_sandwiches} "
      f"finished sandwiches.")
