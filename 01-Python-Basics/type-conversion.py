#two type of type conversion in python
#1. type conversion using built-in functions
#2. type casting

a = 10        # integer
b = 3.14      # float

#type conversion using built-in functions
#convert integer to float
c = float(a)
print("The value of c is:", c)
print("The type of c is:", type(c))
#convert float to integer
d = int(b) 
print("The value of d is:", d)
print("The type of d is:", type(d))
#convert integer to string
e = str(a) 
print("The value of e is:", e)
print("The type of e is:", type(e))
#convert string to integer
f = int("20")
print("The value of f is:", f)
print("The type of f is:", type(f))
#convert string to float
g = float("3.14")
print("The value of g is:", g)
print("The type of g is:", type(g))
#type casting
h = 5
i = 2.5
#casting integer to float   
j = float(h)
print("The value of j is:", j)
print("The type of j is:", type(j))
#casting float to integer
k = int(i)
print("The value of k is:", k)
print("The type of k is:", type(k))
#casting integer to string
l = str(h)
print("The value of l is:", l)
print("The type of l is:", type(l))
#casting string to integer
m = int("15")
print("The value of m is:", m)
print("The type of m is:", type(m))