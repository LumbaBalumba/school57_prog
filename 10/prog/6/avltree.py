from __future__ import annotations

from typing import Callable

from tree import Comparable, Node, Compare


class AVLNode[T: Comparable](Node[T]):
    height: int

    def __init__(
        self,
        value: T,
        predicate: Callable[[T, T], Compare] = lambda first, second: (
            Compare.Less
            if first < second
            else (Compare.Greater if first > second else Compare.Equal)
        ),
    ) -> None:
        super().__init__(value, predicate)
        self.height = 0

    def correct(self) -> bool:
        """Your code here"""
        return False

    def add(self, value: T) -> None:
        """Your code here"""

    def search(self, value: T) -> AVLNode[T] | None:
        """Your code here"""

    def delete(self, value: T) -> None:
        """Your code here"""

    def to_list(self) -> list[T]:
        """Your code here"""
        return []

    def merge(self, other: AVLNode[T]) -> None:
        """YOur code here"""


class AVLSet:
    """Your code here"""


class AVLDict:
    """Your code here"""


"""Также обязательны тесты для проверки функциональности написанных классов. Должен быть проверен каждый метод включая конструктор, в различных случаях (в том числе в краевых)"""
