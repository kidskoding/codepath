# create a dictionary
student = {'name': 'Alice', 'age': 20, 'grade': 'A'}
empty = {}

# insert into dictionary
student['email'] = 'alice@school.com' # -> adds 'email' key to student
student.update({'city': 'San Francisco', 'state': 'CA'}) # -> adds multiple keys at once
print(f'{student}\n') # -> prints the updated dictionary

# read value from key
print(student['name']) # -> prints 'Alice'; raises KeyError if key missing
print(student.get('phone')) # -> prints None; no KeyError if key missing
print(f'{student.get('phone', 'N/A')}\n') # -> prints 'N/A' as fallback if key missing

# check existence
print('age' in student) # -> prints True because 'age' string is in student dictionary
print(f'{'phone' in student}\n') # -> prints False because 'phone' string is not in student dictionary

# change value at a key
student['grade'] = 0 # -> changes the value associated with 'grade' in students to 0

# iterate
for key in student:
    print(key, student[key]) # -> prints the key and value associated with the key

print()

# print values only
for value in student.values():
    print(value) # -> prints the values in the student dictionary
