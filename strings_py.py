x = "ABCDE"
y = '!aeioú' + '\n' + 'ddddd'
z = 'O rato Roeu a Roupa do rei de Roma'
seq = z.split(" ") # vazio ele quebra por espaço
busca = z.find("rei")
recolocar = z.replace('rei','imperador')

print(x.lower())
print(y.strip()) # remove carcter especial \n pular linha
print(seq)
print(busca)
print(z[busca:])
print(recolocar)

