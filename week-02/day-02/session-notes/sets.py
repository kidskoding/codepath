empty_dict = {}
empty_set = set()

nums = {1, 2, 3, 1, 2, 3, 1, "1", 1, "1"}
# nums.remove(5)
nums.discard(1)
print(nums)

students_A = {"Alice", "Bob", "Carol"}
students_B = {"Bob", "Carol", ""}

union = students_A | students_B
intersect = students_A & students_B
diffA = students_A - students_B
diffB = students_B - students_A
sym = students_A ^ students_B

print(f'Intersection of students_A and students_B: {intersect}')
print(f'Union of students_A and students_B: {union}')
print(f'Difference of students_A and students_B: {diffA}')
print(f'Difference of students_B and students_A: {diffB}')
print(f'Symmetric Difference of students_A and students_B: {sym}')
