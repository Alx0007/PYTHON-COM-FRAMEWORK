# 6. Validação de horário de funcionamento
# Enunciado:
# Uma loja funciona de segunda a sexta, das 9h às 18h.
# Leia o dia da semana (1=segunda, 7=domingo) e a hora (0 a 23).
# Determine se a loja está aberta.
# Dica: use and para combinar dia útil com horário, e or se quiser tratar 
# sábado/domingo como fechado.

dia = int(input('Dia da semana: '))
hora = int(input('Hora: '))

V = hora >=9 and hora <=18 and dia >=1 and dia <= 5 and "Loja aberta" or 'Loja fechada'

print(V)