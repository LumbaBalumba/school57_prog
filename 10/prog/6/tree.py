from __future__ import annotations
from enum import Enum, auto
from typing import Callable


class Compare(Enum):
    Less = auto()
    Equal = auto()
    Greater = auto()


class Node[T]:
    value: T
    left: Node[T] | None
    right: Node[T] | None
    predicate: Callable[[T, T], Compare]

    def __init__(self, value: T, predicate: Callable[[T, T], Compare]) -> None:
        self.value = value
        self.predicate = predicate
        self.left = None
        self.right = None

    def correct(self) -> bool:
        if self.left is not None:
            if not self.left.correct():
                return False
            if not self.predicate(self.left.value, self.value) == Compare.Less:
                return False
        if self.right is not None:
            if not self.right.correct():
                return False
            if not self.predicate(self.right.value, self.value) == Compare.Greater:
                return False
        return True

    """
    Написать следующие методы:
    add(self, value: T) -> None
    search(self, value: T) -> Node[T] | None
    delete(self, value: T) -> None
    to_list(self) -> list[T]
    merge(self, other: Node[T]) -> None

    class Set
    class Dict
    """
