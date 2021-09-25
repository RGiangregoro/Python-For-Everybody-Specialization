name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hist = dict()
for line in handle:
    line.rstrip()
    if line.startswith("From "):
        hist[line.split()[5].split(":")[0]] = hist.get(line.split()[5].split(":")[0], 0) + 1

for k,v in sorted(hist.items()):
    print(k,v)
        	