# Contexto:
# Uma loja oferece um cupom especial. O cliente ganha o cupom se atender a pelo menos  das seguintes condições:
# Se for VIP (responde "sim" ou "não")
# Valor da compra acima de R$ 200
# Primeira compra no mês (responder "sim" ou "nao")
# Além disso, o cupom  pode ser aplicado se o cliente tiver  no histórico. 
# Tarefa Receba:
# vip (string "sim" ou "nao")
# valor (float)
# primeira_compra (string "sim" ou "nao")
# Reclamação 
# Determine se o cliente  ("Cupom liberado") ou  ("Sem cupom"),  (SEM IF , SEM LOOP, SEM FUNÇÃO)

vip = input('vip (sim ou não): ')
valor = float(input('Valor da compra: '))
pcompra = input('Primeira compra no mês: ')
rc = input('Reclamação: ')

resultado = (vip == "sim") + (valor > 200) + (pcompra == "sim")
saida = "Cupom liberado" * (resultado >= 2) + "Sem cupom" * (resultado < 2)

print('Resumo: ', 'Valor da compra: ', valor, saida, 'Reclamação: ', rc)