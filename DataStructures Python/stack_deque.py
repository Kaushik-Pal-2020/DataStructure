from collections import deque

my_stack = deque()

my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
my_stack.append(4)
my_stack.append(5)

print(my_stack)

my_stack.appendleft(6)

print(my_stack)

my_stack.pop()
my_stack.popleft()

print(my_stack)

for i in range(0, 4):
    print('='*50)
    print(f"ROtaing {i} :\n")
    my_stack.rotate(1)
    print(my_stack)
    print('='*50)

new_stack = deque()
# new_stack.append(55)
print(new_stack[0])
