import string
opened_file = open("sample.txt")

book = opened_file.read().lower()


def getKey(item):
    return item[1]

for punct in string.punctuation:
    book = book.replace(punct, "").replace("\n", " ").replace("-", " ").replace("  ", " ")

# print(book)


word_count = {}
word_count_list = []


for word in book.split():
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    temp = [word, count]
    word_count_list.append(temp)


sorted_list = ((sorted(word_count_list, key=getKey, reverse=True))[0:19])


for i in sorted_list:
    print(i)