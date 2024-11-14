from __future__ import annotations
from typing import Callable


class Node[T]:
    value: T
    left: Node[T] | None
    right: Node[T] | None
    predicate: Callable[[T, T], bool]

    def __init__(self, value: T, predicate: Callable[[T, T], bool]) -> None:
        self.value = value
        self.predicate = predicate
        self.left = None
        self.right = None

    def correct(self) -> bool:
        if self.left is not None:
            if not self.left.correct():
                return False
            if not self.predicate(self.left.value, self.value):
                return False
        if self.right is not None:
            if not self.right.correct():
                return False
            if not self.predicate(self.value, self.right.value):
                return False
        return True
