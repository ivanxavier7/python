from code import divide
import sys

print(divide(10, 2))
print(sys.path)


# print(divide(10, 0))

# Levantar erros
def divide2(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor não pode ser 0.")
    return dividend / divisor


# print(divide(10, 0))
grades = []
# Agir consoante o erro
try:
    average = divide2(sum(grades), len(grades))
except ZeroDivisionError:
    print("Não existem notas na sua lista.")
else:
    print(f"A média é {average}.")
finally:
    print("Thank you!")


# Costum errors, para fazer raise temos de passar como parametro uma excecao
class CostumErrorClass(ValueError):
    pass


x, y = 5, 10
# Com traceback
#if x < y:
#    raise CostumErrorClass("Erro personalizado")
# Sem traceback para users
try:
    if x < y:
        raise CostumErrorClass("Erro personalizado")  # Pode ser levantado dentro de uma funcao
except CostumErrorClass as e:
    print(e)
