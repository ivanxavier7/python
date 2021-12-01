class Student:
    # Special methods
    def __init__(self, name, age):  # Construtor do objeto
        self.name = name
        self.age = age
        self.grades = (90, 80, 93, 78, 90)

    # Altera no output para o user
    def __str__(self):
        return f"Nome: {self.name} Idade: {self.age}"

    # Altera tambem n o debugger
    def __repr__(self):
        return f"<Person: {self.name}, {self.age})>"

    def average(self):
        return sum(self.grades) / len(self.grades)


class ClassTest:
    def instance_method(self):
        print(f"Called instance_method: of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")


student = Student("Ivan", 27)
student2 = Student("Francisco", 41)
print(student.name)
print(student.grades)
print(Student.average(student))
print(student.average())

print(student)
print(student2)

test = ClassTest()
test.instance_method()  # Temos de instanciar
ClassTest.class_method()  # Usa a classe sem instanciar
ClassTest.static_method()  # Sem informacao do objeto ou da classe


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book("Eldest", "hardcover", 1900)
print(book)
book_hard = Book.hardcover("Eldest", 1900)  # Aplicaco de um metodo de classe
book_light = Book.paperback("Eldest", 1900)  # Aplicaco de um metodo de classe
print(book_hard)
print(book_light)

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        return "{}, preço total: {}".format(store.name, store.stock_price())
