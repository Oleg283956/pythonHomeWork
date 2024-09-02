def single_root_words(root_word,*other_words):
    same_words = []
    for i in range(len(other_words)):
        word_tmp = other_words[i]
        if len(root_word) > len(word_tmp):
            if word_tmp.lower() in root_word.lower():
                same_words.append(word_tmp)
        else:
            if root_word.lower() in word_tmp.lower():
                same_words.append(word_tmp)
    return  same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum','cheers', 'richies')
result2 = single_root_words('Disablement', 'Able','Mable', 'Disable', 'Bagel')
print(result1)
print(result2)




