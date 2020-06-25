from collections import deque


def parenthesis_matching(user_input):
    my_stack = deque()
    my_dict = {'(': ')', '{': '}', '[': ']'}
    try:
        count = 0
        for letter in user_input:
            if letter in my_dict.keys():
                my_stack.append(letter)
                count += 1
            elif letter in my_dict.values() and count > 0:
                if my_dict[my_stack[count-1]] == letter:
                    my_stack.pop()
                    count -= 1
        print(f"Now stack Becomes = {my_stack}")
    except:
        print("error")


parenthesis_matching("{[a+b]*[(c-d]/e}")
