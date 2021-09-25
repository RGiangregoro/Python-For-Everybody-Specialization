# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
    print("Incorrect file name")

count = 0
numberSum = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    
    count = count + 1
    numberSum = numberSum + float(line[20:])
    
print("Average spam confidence:", numberSum / count)
