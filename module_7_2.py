def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file:
        #file.writelines(strings)
        for text in strings:
            file.write(text)
            file.write('\n')

    index_pos = []
    data = []

    with open(file_name,'r', encoding='utf-8') as f:
        lines_in_file = sum(1 for line in f)
        f.seek(0)
        for line in  range(lines_in_file):
            index_pos.append((line, f.tell()))
            data.append((f.readline()).replace('\n',''))

        index_pos = tuple(index_pos)
        strings_positions = dict(zip(index_pos, data))

        #print(*strings_positions.items(), sep='\n')
        return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

custom_write('../dop/test.txt', info)

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)