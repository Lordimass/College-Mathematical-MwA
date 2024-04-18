import math

def multiply(a,b):
	a = [a]
	b = [b]
	while b[len(b)-1] != 1:
		newb = b[len(b)-1]//2
		b.append(newb)
		newa = a[len(a)-1]*2
		a.append(newa)
		
	output = 0
	for i in range(0, len(a)):
		if b[i] % 2 != 0:
			output += a[i]
			
	print(output)

def quad_solve(a,b,c):
	d = (b**2) - (4*a*c)
	if d < 0:
		print(".")
		print("No real solutions")
		return

	print((-b + math.sqrt(d))/(2*a))
	print((-b - math.sqrt(d))/(2*a))

def sqrt(a, rnd):
	val = 1
	while val**2 < a:
		val+=1
	
	if abs(a-(val**2)) < abs(a-((val-1)**2)):
		pass
	else:
		val -= 1

	b = a/val
	print(round((val+b)/2,rnd))

def frctnl_sqrt(a,dp): # Only works for values between 0 and 2
	x = a - 1
	oldr = 1
	i = 1
	j = 0.5
	k = 0.5
	change = (x**i) * k
	newr = oldr + change
	
	while not(-0.005 < change < 0.005):
		oldr = newr
		i += 1
		j -= 1
		k = k*j/i
		change = (x**i) * k
		newr = oldr + change

	print(round(newr, dp))

def eulers(dp):
	A = 1
	B = 1
	C = 1
	while B != dp:
		C *= B
		A += 1/C
		B += 1
	print(f"e is approximately equal to {round(A,dp)}")

eulers(5)