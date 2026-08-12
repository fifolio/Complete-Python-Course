data = {'name': 'John', 'age': 30, 'city': 'New York'}

print(data.get('name'))  # Output: John

na = data.get('local', 'N/A')

print(na)  # Output: N/A

del data['age']

print(data)