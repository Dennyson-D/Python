# pequena funçaõs em nome
# muito utilizada dent4ro de funções
# cóidigo mais clean

'''
def somar(x):
    return x+10

print(somar(4))
'''

# função de somar com 10
somar10 = lambda x : x + 10
print(somar10(7))

# função com 2 args

somar = lambda x,y:x+y
subtra = lambda x,y:x-y
mult = lambda x,y:x*y
div = lambda x,y:x/y

print(somar(4,8))
print(subtra(10,5))
print(f'multi {mult(10,10)}')
print(f'div {div(20,2)}')