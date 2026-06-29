is_number = lambda s: s.replace('.', '', 1).lstrip('-').isdigit()

s = input("Enter a string: ")
print("Yes, it is a number!" if is_number(s) else "No, it is not a number!")