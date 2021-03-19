import string
fname = input("Insert file name: ")
fhand = open(fname)
words = dict()
common = list()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line.rstrip()
    w = line.split()
    for i in w:
        words[i] = words.get(i, 0) + 1
#print(words, end="\n")

for key,value in list(words.items()):
    common.append((value,key))

common.sort(reverse=True)
#print(common, end="\n")


print("The 3 most common words are: %s, %s, %s"%(common[0][1], common[1][1], common[2][1]))



