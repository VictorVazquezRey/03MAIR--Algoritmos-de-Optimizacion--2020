import numpy as np


class Node:
    def __init__(self, numbers:list=[], operations:list=[]):
        self.numbers = numbers
        self.operations = operations
        self.expression = self.generate_expression()

    def eval_node(self):
        if Node.is_empty(self.numbers):
            return None
        return eval(self.expression)

    @staticmethod
    def is_empty(l: list):
        return not l

    def generate_expression(self):
        if not self.numbers:
            return ''
        elif Node.is_empty(self.operations):
            return str(self.numbers[0])

        result = str(self.numbers[0])
        for n,o in zip(self.numbers[1:],self.operations):
            result += "{}{}".format(o,n)

        return result

    def add_number(self, number:int):
        self.numbers.append(number)
        self.expression += str(number)

    def add_operation(self,operation:str):
        self.operations.append(operation)
        self.expression += operation
        
    def substact_number(self):
        self.numbers.pop()
        self.expression = self.expression[:-1]

    def substact_operation(self):
        self.operations.pop()
        self.expression = self.expression[:-1]
