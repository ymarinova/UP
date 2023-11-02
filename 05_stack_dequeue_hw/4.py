user_input = input()
user_input_list = user_input.split()
stack = []
for user_input in user_input_list:
    stack.append(int(user_input))

row_limit = int(input())
row_counter = 1

row_current_sum = 0
while len(stack) != 0:
    num = stack.pop()
    row_current_sum += num
    if row_current_sum < row_limit:
        continue
    else:
        row_counter += 1
        stack.append(num)
        row_current_sum = 0
        
print(row_counter)