# Use words.txt as the file name
fname = input("Enter file name: ")

try:
	fh = open(fname)
except:
    print("File name doesn't exist")
    quit()
    

for line in fh:
    strippedLine = line.rstrip()
    print(strippedLine.upper())