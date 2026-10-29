import math

def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    # skip genap increment 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
            
    return True

def fooBarCheck(number) -> int | str | None:
    if is_prime(number):
        return None
    if number % 3 == 0 and number % 5 == 0:
        return "FooBar"
    elif number % 3 == 0 :
        return "Foo"
    elif number % 5 == 0:
        return "Bar"
    return number

numbers = list(range(1,101))
class foobar:
    def __init__(self):
        self.list = []
        
    def foobar(self,number):
        for number in reversed(numbers):
            result = fooBarCheck(number)
            if result is not None:
                self.list.append(result)        
        print(*self.list, sep = ', ')

if __name__ == "__main__":
    fb = foobar()
    fb.foobar(numbers)