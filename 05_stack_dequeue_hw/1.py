stack = []

user_input = input()
numbers = user_input.split(", ")
for num in numbers:
    stack.append(num)

reversed_list = []
while len(stack) != 0:
    num = stack.pop()
    reversed_list.append(num)
print(" ".join(reversed_list))
    