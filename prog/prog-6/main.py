from typing import Any


class ExprNode:
    value: str
    left: Any
    right: Any

    def __init__(self, expr: str):
        index = self.sign_split(expr)
        while index == -1:
            if expr[0] == "(" and expr[-1] == ")":
                expr = expr[1:-1]
                index = self.sign_split(expr)
            else:
                self.value = expr
                self.left = self.right = None
                return
        self.left = ExprNode(expr[:index])
        self.right = ExprNode(expr[index + 1 :])
        self.value = expr[index]

    @staticmethod
    def sign_split(expr: str) -> int:
        res_prio_1 = -1
        res_prio_2 = -1
        balance = 0
        for i in range(len(expr)):
            if expr[i] == ")":
                balance -= 1
            elif expr[i] == "(":
                balance += 1
            elif expr[i].isdigit() or expr[i] == "x":
                continue
            elif expr[i] in ["*", "/"] and balance == 0:
                res_prio_2 = i
            elif expr[i] in ["+", "-"] and balance == 0:
                res_prio_1 = i
        if res_prio_1 == -1 and res_prio_2 == -1:
            return -1
        elif res_prio_1 >= 0:
            return res_prio_1
        else:
            return res_prio_2
        return -1

    def calc(self, x: float = 0) -> float:
        if self.right is None and self.left is None:
            if self.value == "x":
                return x
            else:
                return float(self.value)
        else:
            left_value = self.left.calc(x)
            right_value = self.right.calc(x)
            if self.value == "+":
                return left_value + right_value
            elif self.value == "-":
                return left_value - right_value
            elif self.value == "*":
                return left_value * right_value
            elif self.value == "/":
                return left_value / right_value
            return 0


tree = ExprNode("2+5*x")
print(tree.calc(10))
