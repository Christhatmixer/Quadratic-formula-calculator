def quadratic(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    discRoot = math.sqrt((b * b) - 4 * a * c)
    answer = (-b + discRoot) / (2 * a) # solving positive
    answer2 = (-b - discRoot) / (2 * a) # solving negative
    return (answer,answer2)