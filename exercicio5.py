x = 2
y = 8
s = '/'

def soma(x,y):
	print(x+y)
def subtracao(x,y):
	print(x-y)
def mult(x,y):
	print(x*y)
def div(x,y):
	print(x/y)

if s == '+':
	soma(x,y)
elif s == '-':
	subtracao(x,y)
elif s == '*':
	mult(x,y)
elif s == '/':
	div(x,y)
