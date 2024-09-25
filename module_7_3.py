class WordsFinder:
    file_names = []
    list_strRead = []
    all_words = {}

    def __new__(cls, *args, **kwargs):
        list_args = list(args)
        for i in list_args:
            cls.file_names.append(i)
        return super().__new__(cls)

    def __int__(self,*args, **kwargs):
        pass

    def get_all_words(self):
        for j in self.file_names:
            name = j
            punktuacion = [',', '.', '=', '!', '?', ';', ':', ' - ']
            with open(name,'r',encoding='utf-8') as file:
                strRead = ''
                for line in file:
                    strRead += ' '+line.strip()
                    strRead = strRead.lower()

                    self.list_strRead = strRead.split()
                    ind = -1
                    for sub in self.list_strRead:
                        ind += 1
                        wordStr = sub
                        while wordStr[-1] in punktuacion:
                            wordStr = wordStr[0:-1]
                        self.list_strRead[ind] = wordStr
            self.all_words[str(name)] = self.list_strRead
        return self.all_words

    def find(self, word):
        find_word = {}
        word = word.lower()
        for name,words in self.get_all_words().items():
            ind = 0
            for i in words:
                ind += 1
                if i == word:
                    find_word[str(name)]=str(ind)
                    break
        return find_word

    def count(self, word):
        count_word = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            count = 0
            for i in words:
                if i == word:
                    count += 1
            count_word[str(name)] = str(count)
        return count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))