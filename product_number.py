from functools import reduce

numbers = [1, 2, 5, 4, 10]
product = reduce(lambda x, y: x * y, numbers)
print(product)