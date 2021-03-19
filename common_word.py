fname = input("Insert file name: ")
fhand = open(fname)
words = dict()
for line in fhand:
    line.rstrip()
    w = line.split()
    words[w] = words.get(w, 0) + 1
print(words)


#for key, val in list(d.items()):
#print(val, key)
