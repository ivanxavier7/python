from typing import List


def list_avg(sequence: List) -> float:   #type hinting
    return sum(sequence) / len(sequence)


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":  # Quando retorna o objeto
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)


def divide(dividend, divisor):
    return dividend / divisor

print("mymodule.py: ", __name__)    # Main neste codigo mas a importar da print ao nome do ficheiro importado
