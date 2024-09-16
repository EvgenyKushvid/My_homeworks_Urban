class WordsFinder:
    file_names = []
    def __init__(self, *file_names ):
        for file in file_names:
            self.file_names.append(file)
        self.file_names  = file_names




    def get_all_words (self):
        symb = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as f:
                    file_str = (f.read().lower())
                    # print(file_str)
                    for s in symb:
                        if s in file_str:
                            file_str = file_str.replace(s,' ')
                    str_sp = file_str.split()
            all_words[file] = str_sp
        return all_words

    def find(self, word):
        res ={}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                res[name] = words.index(word.lower())+1
        return res

    def count(self, word):
        res = {}
        count = 0
        for name, words in self.get_all_words().items():
            for i in words:
                if word.lower() == i:
                    count +=1
            res[name] = count
        return res


finder2 = WordsFinder('One.txt', 'test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего