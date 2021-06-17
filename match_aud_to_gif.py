from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
import math
import re
from collections import Counter

stop_words = set(stopwords.words('english'))

WORD = re.compile(r"\w+")

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

ps = PorterStemmer()
all_tags = []
fr = open("tags.txt", "r")
for item in fr:
    temp = item.split(",")[:-1]
    all_tags.append(temp)
#all_tags = [["ahmedabad"], ["are", "busy"], ["french", "biriyani"]]
f = open("phrases.txt", "r")
for line in f:
    #temp = list(line)
    word_tokens = word_tokenize(line)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = []
    for w in word_tokens:
       if w not in stop_words:
           filtered_sentence.append(w)
    highest = 0
    ind = [""]
    for tags in all_tags:
        tags.sort()
        filtered_sentence.sort()
        cosine = get_cosine(text_to_vector(str(tags)), text_to_vector(str(filtered_sentence)))
        if(cosine > highest):
            ind = tags
            highest=cosine
        print(cosine, highest)
        highest = 0
        cosine = 0
    print(ind)


