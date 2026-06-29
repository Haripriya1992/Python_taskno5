people = [
    {'name': 'Alice', 'age': 20},
    {'name': 'Bob', 'age': 15},
    {'name': 'Charlie', 'age': 17},
    {'name': 'Diana', 'age': 22},
]

age=list(filter(lambda p: p['age'] >= 18, people))
age1=list(filter(lambda p: p['age'] <= 18,people))
name=list(map(lambda p: p['name'],age1))
print(age)  # ['Alice', 'Diana']
print(name)