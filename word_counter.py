import re
import collections

file = open('98-0.txt', 'r', encoding='utf-8')
text = file.read()

file1 = open('stopwords', 'r', encoding='utf-8')
stopwords = file1.read()

word_list=[]        #list for words
word_count={}       #Dictionary for word count

words = text.lower().split()
for each_word in words:
    word_list.append(each_word)

#print(len(word_list))

word_list_cln = [re.sub(r'\W', '', i) for i in word_list]   #List comprehension so sub values using regex
#print(word_list_cln)

for words_f in word_list_cln:               #building dictionary with word count
    if words_f not in stopwords:
        if words_f not in word_count:
            word_count[words_f] = 1
        else:
            word_count[words_f] += 1

#print(word_count)

d=collections.Counter(word_count)

for word_f, count in d.most_common(10):
    print(word_f, ":", count)





