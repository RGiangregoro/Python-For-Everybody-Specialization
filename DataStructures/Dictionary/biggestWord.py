name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hist = dict()

for line in handle:
    line.rstrip()
    if line.startswith("From "):
        words = line.split()
        hist[words[1]] = hist.get(words[1],0) + 1
        
bigWord = None
bigCount = None
for k,v in hist.items():
    if k == None or v > bigCount:
        bigWord = k
        bigCount = v
        
print(bigWord, bigCount)
            
        