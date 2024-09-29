first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']


first_result = [len(elem) for elem in first_strings if len(elem) >= 5]
second_result = [(elem, el)  for elem in first_strings for el in second_strings if len(elem)==len(el)]
third_result = {elem: len(elem) for elem in (first_strings + second_strings) if len(elem) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)