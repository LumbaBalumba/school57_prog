class AVLtree:
    value: float
    left: object
    right: object
    parent: object
    left_h: int
    right_h: int

    def __init__(self, value, parent=None) -> None:
        self.value = value
        self.right = self.left = None
        self.parent = parent
        self.left_h = self.right_h = 0

    def balanced(self):
        return abs(self.left_h - self.right_h) <= 1

    def balance(self):
        if self.balanced():
            return

        self.left.balance()
        self.right.balance()

        if self.right_h - self.left_h == 2:
            if self.right.left_h <= self.right.right_h:
                A = self.left
                B = self.right.left
                C = self.right.right
                b = self.right
                a = self
                self = b
                b.left = a
                a.left = A
                a.right = B
                b.right = C
            else:
                a = self
                b = self.right
                c = b.left
                A = a.left
                B = c.left
                C = c.right
                D = b.right
                self = c
                c.right = b
                c.left = a
                a.left = A
                a.right = C
                b.left = B
                b.right = D
        else:
            pass

    def add(self, value):
        if value > self.value:
            self.right_h += 1
            if self.right is None:
                self.right = AVLtree(value, self)
            else:
                self.right.add(value)
        else:
            self.left_h += 1
            if self.left is None:
                self.left = AVLtree(value, self)
            else:
                self.left.add(value)
