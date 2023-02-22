## Reto #0: EL FAMOSO "FIZZ BUZZ”
## Escribe un programa que muestre por consola (con un print) los
## números de 1 a 100 (ambos incluidos y con un salto de línea entre
## cada impresión), sustituyendo los siguientes:
## - Múltiplos de 3 por la palabra "fizz".
## - Múltiplos de 5 por la palabra "buzz".
## - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

print("Reto #0")

# Is divisible function
def is_divisible(number, by):
    return number % by == 0

# Fizz Buzz function
def fizz_buzz(first_number, last_number):
  for number in range(first_number, last_number + 1):
    isDivisibleBy3 = is_divisible(number = number, by = 3)
    isDivisibleBy5 = is_divisible(number = number, by = 5)
    if isDivisibleBy3 and isDivisibleBy5:
        print("fizzbuzz")
    elif isDivisibleBy3:
        print("fizz")
    elif isDivisibleBy5:
        print("buzz")
    else:
        print(number)

# Challenge
fizz_buzz(first_number = 1, last_number = 100)
