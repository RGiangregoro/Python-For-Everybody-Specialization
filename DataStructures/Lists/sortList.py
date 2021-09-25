fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    innerList = line.split()
    for inner in innerList:
        if inner in lst : continue
        lst.append(inner)
lst.sort()
print(lst)
