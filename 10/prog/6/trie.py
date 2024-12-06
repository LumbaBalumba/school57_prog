from __future__ import annotations


class TrieNode:
    nodes: dict[str, TrieNode]

    def __init__(self) -> None:
        pass


class Trie:
    root: TrieNode

    def __init__(self) -> None:
        pass

    def add(self, s: str) -> None
        pass

    def contains(self, s: str) -> bool:
        pass

    def delete(self, s: str) -> None:
        pass

    """
    1) Реализовать класс узла префиксного дерева и класс префиксного дерева. Дерево должно хранить множество строк способом, указанным на лекции в классе.
    2) Протестировать полученные классы с помощью pytest/unittest
    3) Найти примеры на которых set[str] показывает себя эффективнее и примеры для которы эффективнее будет полученное дерево
    4) * Вместо стандартного класса dict использовать написанный ранее класс AVLDict/Dict
    5) * Реализовать сжатое префиксное дерево, то есть такое, которое в одном узле хранит символы не по одному, а строками по несколько
    """
