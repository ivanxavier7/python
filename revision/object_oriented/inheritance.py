class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
        
    def __str__(self):
        return f"Dispositivo {self.name!r} ({self.connected_by})" # !r mete "

    def disconnect(self):
        self.connected = False
        print("Desconectado.")

printer = Device("Impressora", "USB")
print(printer)

class Printer(Device):  # Passamos a classe mae
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)    # Chamamos os argumentos da classe mae
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("A impressora não se encontra conectada!")
            return
        print(f"Imprimindo {pages} páginas.")
        self.remaining_pages -= pages

printer = Printer("Impressora", "USB", 500)
printer.print(20)
print(printer)
printer.disconnect()
printer.print(20)
