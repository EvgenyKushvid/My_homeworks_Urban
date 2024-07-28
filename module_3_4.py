def single_root_words ( root_word,  *other_words):
    some_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            some_words.append(i)
        if i.lower() in root_word.lower():
            some_words.append(i)
    return some_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)