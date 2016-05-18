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
ignore_list = ["a", "able", "about", "across", "after", "all", "almost", "also",
               "am", "among", "an", "and", "any", "are", "as", "at", "be",
               "because", "been", "but", "by", "can", "cannot", "could", "dear",
               "did", "do", "does", "either", "else", "ever", "every", "for", "from",
               "get", "got", "had", "has", "have", "he", "her", "hers", "him", "his",
               "how", "however", "i", "if", "in", "into", "is", "it", "its", "just",
               "least", "let", "like", "likely", "may", "me", "might", "most", "must",
               "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only",
               "or", "other", "our", "own", "rather", "said", "say", "says", "she", "should",
               "since", "so", "some", "than", "that", "the", "their", "them", "then", "there",
               "these", "they", "this", "tis", "to", "too", "twas", "us", "wants", "was",
               "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why",
               "will", "with", "would", "yet", "you", "your"]


for word in book.split():
    if word in ignore_list:
        continue
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    temp = [word, count]
    word_count_list.append(temp)


sorted_list = ((sorted(word_count_list, key=getKey, reverse=True))[0:20])

number_list = []
word_list = []

for i in sorted_list:
    number_list.append(i[1])
    word_list.append(i[0])

sorted_words = sorted(word_list, key=len)

print(sorted_words[-1])
print(max(number_list))

for word, counter in sorted_list:
    print(word, counter * "|")

opened_file.close()