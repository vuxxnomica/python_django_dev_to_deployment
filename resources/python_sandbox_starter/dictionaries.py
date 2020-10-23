# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple dictionary
person = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 30
}

# Using a constructor
# person = dict(first_name='Jane', last_name='Doe', age=30)

print(person)

# Access value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

print(person)

# Get keys
print(person.keys())

# Get items
print(person.items())

# Make copy
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)

# Remove item
del person['age']
person.pop('phone')

print(person)

# Clear
person.clear()

print(person)

# Get length
print(len(person2))

# List of dictionaires
people = [
    {'name': 'Martha', 'age': 40},
    {'name': 'Bob', 'age': 20}
]

print(people)
print(people[1]['name'])
