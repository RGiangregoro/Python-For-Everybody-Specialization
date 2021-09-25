import re

handle = open("regex_sum_298561.txt")
txt = handle.read()

sum = 0 
for num in re.findall("[0-9]+", txt):
	sum = sum + float(num)

print(sum)
