
import json
person = '{"c": 310.13, "h": 310.29, "l": 304.29, "o": 305.64, "pc": 303.74, "t": 1589083003}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(person_dict)

# Output: ['English', 'French']
print(person_dict['l'])
