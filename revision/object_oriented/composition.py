# Heranca e para ser usada quando as propriedades da mae nao devem passar para os filhos,
# Composicao permite dizer que uma estante de livros e a composicao de varios livros
# Uma classe e composta por varias classes
class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Prateleira com {len(self.books)} livros."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Livro {self.name}"


book = Book("Eldest")
book2 = Book("Harry Potter")
shelf = BookShelf(book, book2)

print(shelf)
print(f"\nLivros:\n{book}\n{book2}")


