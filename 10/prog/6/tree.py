from __future__ import annotations
from typing import Callable


class Node[T]:
    value: T
    left: Node[T] | None
    right: Node[T] | None
    predicate: Callable[[T, T], int]

    def __init__(self, value: T, predicate: Callable[[T, T], int]) -> None:
        self.value = value
        self.predicate = predicate
        self.left = None
        self.right = None

    def correct(self) -> bool:
        if self.left is not None:
            if not self.left.correct():
                return False
            if not self.predicate(self.left.value, self.value) < 0:
                return False
        if self.right is not None:
            if not self.right.correct():
                return False
            if not self.predicate(self.right.value, self.value) > 0:
                return False
        return True

    """
    Написать следующие методы:
    add(self, value: T) -> None
    search(self, value: T) -> Node[T]
    delete(self, value: T) -> None
    to_list(self) -> list[T]
    """
