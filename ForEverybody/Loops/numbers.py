largest = None
smallest = None
while True:
	num = input("Enter a number: ")
	if num == "done" : break

	try:
		fValue = float(num)
	except:
		print("Invalid Input")
		continue

	if largest is None: 
		largest = fValue
	elif fValue > largest:
		largest = fValue

	if smallest is None:
		smallest = fValue
	elif  fValue < smallest:
		smallest = fValue

print("Maximum", largest)
print("Minimum", smallest)