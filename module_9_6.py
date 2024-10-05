def all_variants(text):
    for j in range(1,len(text)+1):
        for i in range(0,len(text)):
            if i+j <= len(text):
                i = text[i:i+j]
                yield i

a = all_variants("abc")
for i in a:
    print(i)
