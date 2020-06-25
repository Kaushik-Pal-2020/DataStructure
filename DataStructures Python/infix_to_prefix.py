from collections import deque
from time import time


class Solution:
    def __init__(self, expression):
        self.expression = expression[::-1]
        self.top = -1
        self.stack = deque()
        self.element = ""
        self.result = ""
        self.precedence = {
            "+": 1,
            "-": 1,
            "/": 2,
            "*": 2,
            "%": 2,
            "^": 3,
            "(": 4,
            ")": 4,
        }

    def insert_in_result(self, character):
        self.result += character

    def insert_in_stack(self, character):
        self.stack.append(character)
        self.top += 1
        self.element = character

    def insert_rest(self):
        try:
            while True:
                self.result += self.stack.pop()
                self.top -= 1
        except IndexError:
            return

    def loop(self):
        for character in self.expression:
            if not character in self.precedence.keys():
                self.insert_in_result(character)
            else:
                if character == "(":
                    self.stack.pop()
                    self.top -= 1
                    while self.element != ")":
                        if self.top == -1:
                            break
                        self.result += self.element
                        self.element = self.stack.pop()
                        self.top -= 1
                    if self.top > -1:
                        self.element = self.stack.pop()
                        self.stack.append(self.element)

                elif self.top == -1:
                    self.insert_in_stack(character)

                elif self.precedence[character] >= self.precedence[self.element]:
                    self.insert_in_stack(character)

                else:
                    flag = 0
                    while (
                        self.precedence[self.element] != self.precedence[character]
                        and self.element != ")"
                    ):

                        self.result += self.element
                        self.stack.pop()
                        self.top -= 1
                        if self.top == -1:
                            break
                        self.element = self.stack.pop()
                        self.stack.append(self.element)

                    self.stack.append(character)
                    self.element = character
                    self.top += 1

        self.insert_rest()

    def __str__(self):
        return self.result[::-1]


if __name__ == "__main__":

    # expression = "K+L-M*N+(O^P)*W/U/V*T+Q"
    expression = input("enter infix :\t")
    t1 = time()
    s = Solution(expression)
    s.loop()
    print("=" * 75)
    print(f"\nInfix : {expression}")
    print(f"Prefix : {s}")
    print(f"Total time taken : {time()-t1:0.4f}  sec\n")
    print("=" * 75)
