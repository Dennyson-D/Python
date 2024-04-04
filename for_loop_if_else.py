compra_confirmada = True
dados_compra = 'Compra no valor de R$20,00 e entrega confirmada'

for enviar in range(3):
 if compra_confirmada:
     print(dados_compra)
     print('Detalhes no email')
     break
 else:
     print('falha')    