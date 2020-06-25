from collections import deque


def infix_to_postfix(expression):
    my_stack = deque()
    my_list = ""
    my_stack_top = -1
    precedence = {"+": 1, "-": 1, "/": 2,
                  "*": 2, "%": 2, "^": 3, "(": 4, ")": 4}
    associativity_RtoL = ["^"]

    for char in expression:
        if char in precedence.keys():
            if my_stack_top >= 0:
                my_stack_top_value = my_stack.pop()
                my_stack.append(my_stack_top_value)

            if my_stack_top == -1 or char == "(":
                my_stack.append(char)
                my_stack_top += 1
                my_stack_top_value = char

            elif char == ")":
                while my_stack_top_value != "(":
                    value = my_stack.pop()
                    my_list += value
                    my_stack_top -= 1
                    if my_stack_top == -1:
                        break
                    my_stack_top_value = my_stack.pop()
                    my_stack.append(my_stack_top_value)
                if my_stack_top != -1:
                    my_stack.pop()
                    my_stack_top -= 1

            elif precedence[char] > precedence[my_stack_top_value]:
                my_stack.append(char)
                my_stack_top += 1
                my_stack_top_value = my_stack.pop()
                my_stack.append(my_stack_top_value)

            elif precedence[char] == precedence[my_stack_top_value]:
                if char in associativity_RtoL:
                    my_stack.append(char)
                    my_stack_top += 1

                else:
                    p = precedence[char]
                    while my_stack_top >= 0 and precedence[my_stack_top_value] == p:
                        my_list += my_stack.pop()
                        my_stack_top -= 1
                        if my_stack_top == -1:
                            break
                        my_stack_top_value = my_stack.pop()
                        my_stack.append(my_stack_top_value)

                    my_stack.append(char)
                    my_stack_top += 1

            elif precedence[char] < precedence[my_stack_top_value]:
                p = precedence[char]
                while (
                    my_stack_top >= 0
                    and precedence[my_stack_top_value] >= p
                    and my_stack_top_value != "("
                ):
                    value = my_stack.pop()
                    my_list += value
                    my_stack_top -= 1
                    if my_stack_top == -1:
                        break
                    my_stack_top_value = my_stack.pop()
                    my_stack.append(my_stack_top_value)

                my_stack.append(char)
                my_stack_top += 1
        else:
            my_list += char

    while my_stack_top != -1:
        my_list += my_stack.pop()
        my_stack_top -= 1

    return my_list


# s = "K+L-M*N+(O^P)*W/U/V*T+Q"
s = input()
result = infix_to_postfix(s)
print(result)
