# This is Dictionaries learning examples
my_dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4' : 100}

# Key Accessibility
print my_dictionary['key1']
print my_dictionary['key2']
print my_dictionary['key3']

print my_dictionary

# Key Can have any value (object) and can also be nested
my_nested_dictionary = {'person': [{'name': 'Himanshu', 'address': 'Oak Grove Road', 'city':'concord'},
                                   {'name':'Roshni', 'address': 'Oak Grove Road', 'city':'concord'}],
                        'food':[{'name':'Burger'}, {'name':'Sandwitch'}]
                        }

print my_nested_dictionary['person'][0]
print my_nested_dictionary['person'][1]
print my_nested_dictionary['person'][0]['name']
# Any String functions can be attached to it
print my_nested_dictionary['person'][0]['name'][::-1]

print my_nested_dictionary['food'][0]['name']
print my_nested_dictionary['food'][1]['name']
# Any String functions can be attached to it
print my_nested_dictionary['food'][1]['name'].upper()

# Any Arithematic operations can also be done
print my_dictionary['key4'] + 4
print my_dictionary['key4']
my_dictionary['key4'] += 4
print my_dictionary['key4']

# Dictionary can also be created empty and then can be initialized later
empty_dictionary = {}
empty_dictionary['cook']='Prepare Food to eat.'
empty_dictionary['phone']='An electronic equipment used to talk to other persons'

print empty_dictionary

# Get the list of all the keys
print my_dictionary.keys()
print my_dictionary.values()
# Tuples
print my_dictionary.items()

