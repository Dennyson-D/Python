# método sem list comprehension
"""
x = [1,2,3,4,5]
y = []

for i in x:
	y.append(i**2)

print(x)
print(y)	
"""
# método list comprehension

x = [1,2,3,4,5]
y = [i**2 for i in x]
z = [i for i in x if i%2==1] # pegar números impares - resto de impar/2 sempre dá 1
print(x)
print(y)
print(z)
