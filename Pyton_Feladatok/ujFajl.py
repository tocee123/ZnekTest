def GreetTheName(name): 
    """ This function greets the person passed into the name parameter name: The name of the person to greet :return: A greeting message """ 
    return f'Hello, {name}!'

def CreateListWithXNumberOfRandomIntegers(x:int) -> list[int]:
    """ Fuggveny definicioja
    parameter x: the amount of random numbers
    :return: not null list of integers"""
    from random import randint
    if (x<=0):
        raise Exception(f"{x}should be positive integer!")
    return [randint(100, 1000) for _ in range(x)]

listam = CreateListWithXNumberOfRandomIntegers(10)
print(listam)