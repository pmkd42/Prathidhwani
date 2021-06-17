from os import listdir
from os.path import isfile, join
from nltk.tokenize import word_tokenize

f = open("tags.txt", "w")
onlyfiles = [f for f in listdir("C://Users//Pammi//PESU_KA_PRATHIDHWANI//ISL_videos") if isfile(join("C://Users//Pammi//PESU_KA_PRATHIDHWANI//ISL_Videos", f))]
tags = []
for filename in onlyfiles:
    filename = filename.split(".")[0]
    word_tokens = word_tokenize(filename)
    tags.append(word_tokens)
for item in tags:
    for small_item in item:
        f.write("%s," % small_item)
    f.write('\n')
f.close()