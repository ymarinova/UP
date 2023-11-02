orders_queue = []
largest_order = 0

food_quantity = int(input())

orders_input = input()

orders = orders_input.split()

for order in orders:
    orders_queue.append(int(order))

while len(orders_queue) != 0:
    order = orders_queue.pop(0)
    if largest_order < order:
        largest_order = order
    if food_quantity >= order:
        food_quantity -= order
    else:
        orders_queue.insert(0, order)
        break

temporary_queue = []
while len(orders_queue) != 0:
    order = orders_queue.pop(0)
    temporary_queue.append(order)
    if largest_order < order:
        largest_order = order

while len(temporary_queue) != 0:
    orders_queue.append(temporary_queue.pop(0))

print(largest_order)
if len(orders_queue) == 0:
    print("Orders complete")
else:
    orders_list = []
    while len(orders_queue) != 0:
        orders_list.append(str(orders_queue.pop(0)))
    print("Orders left: " + ", ".join(orders_list))
