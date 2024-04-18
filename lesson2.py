def hcf(a,b):
    inputs = [a, b]
    q = b//a
    r1 = b - a * q
    r2 = r1

    while r2 > 0:
        r1 = r2
        b = a
        a = r1
        q = b//a
        r2 = b - a * q

    if r1 == 1:
        print(f"{inputs[0]} and {inputs[1]} are co-primes")
    else:
        print(f"HCF of {inputs[0]} and {inputs[1]} is {r1}")

def line_intersections():
    m, c, d, x, y = [], [], [], [], []
    for i in range(0,3):
        m.append(int(input(f"Enter gradient for line {i+1}: ")))
        c.append(int(input(f"Enter y-intersect for line {i+1}: ")))

    for j in range(0,3):
        a = j+1
        if a > 2: a = a - 3

        b = j+2
        if b > 2: b = b - 3

        d.append(m[b] - m[a])
        if d[j] == 0: 
            print("Lines are Parallel")
            continue

        x.append((c[a]-c[b])/d[j])
        y.append(m[a]*x[j]+c[a])
        print(f"Intersection at ({x[j]}, {y[j]})")

def local_min(f, a, b, precision = 0.0001):
    
    minimum = f(a)
    for increment in range(int(a*(1/precision)), int(b*(1/precision))):
        minimum = min(minimum, f(increment*precision))
    
    print(f"Local minimum is {round(minimum, 3)}")

#line_intersections()
local_min(lambda x: 0.2*(x**2)+x+9, -10, -5)