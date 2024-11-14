from __future__ import annotations
from abc import ABCMeta, abstractmethod
from enum import Enum, auto
from typing import Any, Callable


class Compare(Enum):
    Less = auto()
    Equal = auto()
    Greater = auto()


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...

    @abstractmethod
    def __gt__(self, other: Any) -> bool: ...

    @abstractmethod
    def __eq__(self, other: Any) -> bool: ...


class Node[T: Comparable]:
    value: T
    left: Node[T] | None
    right: Node[T] | None
    parent: Node[T] | None
    predicate: Callable[[T, T], Compare]

    def __init__(
        self,
        value: T,
        predicate: Callable[[T, T], Compare] = lambda first, second: (
            Compare.Less
            if first < second
            else (Compare.Greater if first > second else Compare.Equal)
        ),
    ) -> None:
        self.value = value
        self.predicate = predicate
        self.left = None
        self.right = None
        self.parent = None

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

    class Set (add, delete,  &,  | , is_subset,  is_empty, __init__(self, collection: Iterable[T]), __in__)
    class Dict([], __init__(self, collection: Iterable[T]), __in__)
    """
