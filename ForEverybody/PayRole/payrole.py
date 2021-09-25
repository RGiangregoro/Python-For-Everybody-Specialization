hrs = input("Enter Hours:")
h = float(hrs)

rte = input("Enter Rate:")
r = float(rte)

def computepay(hours,rate):
	if h <= 40:
		return(h * r)
	else:
		return (rate * 40 + (rate * 1.5) * (hours - 40))

print(computepay(h,r))