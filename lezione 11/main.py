# We need the functional paradigm everytime we need something that is reliable and with good performances.
# It is based on pure functions: Functions that produce the same exact output everytime with the same input
# A Pure Function has no "side effects" - modifications outside the scope of the function (eg. changing global variables, printing, etc.)
# State shouldn't change (no variables change)
# Recursion is preferred over cycles

### THIS IS CODE WRITTEN USING THE PROCEDURAL PARADIGM
def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num%2 == 0:
            print(f"Found even number: {num}")
            even_numbers.append(num)
    numbers.clear()
    numbers.extend(even_numbers)
    print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
get_even_numbers(numbers)


### THIS IS CODE WRITTEN USING THE OBJECT ORIENTED PARADIGM
class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers
    def get_even_numbers(self):
        even_numbers = []
        for num in self.numbers:
            if num % 2 == 0:
                even_numbers.append(num)
        self.numbers = even_numbers

processor = NumberProcessor([1, 2, 3, 4, 5, 6, 7, 8, 9])
processor.get_even_numbers()
print(processor)

### THIS IS CODE WRITTEN USING THE FUNCTIONAL PARADIGM
def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(get_even_numbers(numbers)) 


## EXCEPTIONS
# An exception is an event that blocks the flow of the program. If the exception does not get caught, it stops the execution
# The exception is represented in python by a class. There is a hierarchy of exceptions
# When the exception is raised, an object of the exception class is generated

"""
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    ├── PythonFinalizationError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
"""

car_price = 20_000

class NegativeMonthsError(Exception):
    def __init__(self):
        super().__init__("Il numero di mesi non può essere negativo")
try:
    months = int(input("In quanti mesi vuoi pagare? "))
    monthly_payment = car_price / months
    assert months>0 # mostly used in testing phase
    ## If i run my program like this python -O .\main.py the assert won't run
    ## We shouldn't leave assert in production code, use raise instead

    if months < 0:
        raise NegativeMonthsError

except ValueError:
    print("Per favore, inserisci un numero intero ")

except ZeroDivisionError:
    print("Per favore, inserisci un numero intero diverso da zero")

except Exception as e:
    print("Errore:", e)

else:
    print(monthly_payment) # The portion of code in the else executes only if no exception is raised

finally:
    print("Connessione al database chiusa con successo") # The finally part is executed everytime
"""
you can also do like this
except (ValueError, ZeroDivisionError):
    print("Per favore, inserisci un numero intero ")
"""