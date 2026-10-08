def add(*args):
    print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(3, 5, 6, 1, 7, 4, 3))

def calculate(n, **kwargs):
    # print(kwargs)
    # for k, v in kwargs.items():
    #     print(k)
    #     print(v)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        self.year = kwargs["year"]

my_car = Car(make="Mercedes", model="GLE", year=2020)
print(my_car.make, my_car.model, my_car.year)


