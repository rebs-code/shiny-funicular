fname = input("Enter a mbox file name in txt: ")
fhand = open(fname)
names = dict()
for line in fhand:
    line = line.rstrip()

    if not line.startswith("From "): continue
    else:
        d = line.split()[1]
        names[d] = names.get(d, 0) + 1

l = list()

for key,value in names.items():
    l.append((value, key))


l.sort(reverse=True)
print(l)
