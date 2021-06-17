import math
class lookahead_node:
    def __init__(self, word=None, next=None):
        self.word = word
        self.next = None

gifs = [["who"],["how"],["how","you"],["how","you","wrong"],["how","you","today"]]
gifs.sort()

start = 0
end = 0
def lookahead(stream, curr, gifs):
    i = 0
    while(stream[curr]!=gifs[i][0]):
        print(stream[curr], gifs[i][0])
        if( i < len(gifs)):
            i+=1
        else:
            break
    start = i
    lens = []
    while(stream[curr]==gifs[i][0]):
        lens.append(len(gifs[i]))
        if(i < len(gifs)):
            i+=1
        else:
            break
    end = i
    highest = 0
    for j in range(start, end):
        if(stream[curr:curr+lens[j]]==gifs[j]):
            if(lens[j]>highest):
                highest = lens[j]
    return highest
#print(gifs, start, end)
#stre = "good morning usa year old cat be careful in those grapes and bananas christians go to church what is your problem with the village"
#print(lookahead(["how", "you", "today", "sir"],0,gifs))
#print(lookahead(stre.split(),0,gifs))
#print(gifs, start, end)
gif1s = [elem[0] for elem in gifs]
c = 0
ans = []
def count(stream):
    c = 0
    if(len(stream) == 1):
        if(stream[0] in gif1s):
            ans.append(stream[0])
            return 1
            
        else:
            for letter in stream[0]:
                ans.append(list(letter))
            return len(stream[0])
    else:
        if(stream[0] in gif1s):
            ans.append(stream[:lookahead(stream,0,gifs)])
            c = c + 1 + count(stream[int(lookahead(stream,0,gifs)):])
        else:
            for letter in stream[0]:
                ans.append(list(letter))
            c = c + len(stream[0]) + count(stream[1:])
    return c
print(count(["how", "you", "today", "sir"]))
ans1 = []
f3 = open("playlist.txt","w")
for wordu in ans:
    makeitastring = ' '.join(map(str, wordu))
    makeitastring += ".mpeg"
    ans1.append(makeitastring)
    f3.write(makeitastring + "\n")
print(ans1)