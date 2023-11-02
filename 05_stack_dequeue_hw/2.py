stack = []
user_inputs = []

n = int(input())

for i in range(n):
    user_input = input()
    user_inputs.append(user_input)

for user_input in user_inputs:
    if len(user_input) != 0:
        command = user_input[0]
        if command == "1":
            user_input_split = user_input.split()
            number = int(user_input_split[1])
            stack.append(number)
        elif command == "2":
            if len(stack) != 0:
                stack.pop()
        elif command == "3":
            temporary_stack = []
            maxim = stack.pop()
            temporary_stack.append(maxim)
            while len(stack) != 0:
                new_max = stack.pop()
                temporary_stack.append(new_max)
                if maxim < new_max:
                    maxim = new_max
            while len(temporary_stack) != 0:
                number = temporary_stack.pop()
                stack.append(number)
            print(maxim)
        elif command == "4":
            temporary_stack = []
            minim = stack.pop()
            temporary_stack.append(minim)
            while len(stack) != 0:
                new_min = stack.pop()
                temporary_stack.append(new_min)
                if minim > new_min:
                    minim = new_min
            while len(temporary_stack) != 0:
                number = temporary_stack.pop()
                stack.append(number)
            print(minim)
        elif command == "5":
            counter = 0
            temporary_stack = []
            while len(stack) != 0:
                temporary_stack.append(stack.pop())
                counter += 1
            while len(temporary_stack) != 0:
                stack.append(temporary_stack.pop())
            print(counter)

reversed_list = []
while len(stack) != 0:
    num = str(stack.pop())
    reversed_list.append(num)
print(", ".join(reversed_list))

