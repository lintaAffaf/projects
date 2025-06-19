def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum

print(add(3,5,6,7))


def calculate(n,**kwargs):
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

