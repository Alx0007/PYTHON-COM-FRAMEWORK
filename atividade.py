# Contexto:
# Uma indústria monitora temperatura (T), umidade (U) e presença de gás inflamável (G, 0 ou 1).
# O nível de risco é dado por:
# Crítico: (T > 40 ou U > 80) e G == 1
# Alto: (T > 40 ou U > 80) e G == 0
# Médio: (T entre 25 e 40) e (U entre 50 e 80) e o  G == 0
# Baixo: qualquer outra situação
# Tarefa:
# Receba T (float), U (float), G (0 ou 1).
# Classifique o risco em "Crítico", "Alto", "Médio" ou "Baixo" sem usar if/elif.
# Use apenas dicionários com chaves booleanas e operadores lógico
# UTILIZE APENAS SINAIS LÓGICOS -  VARIAVEIS  -  LISTAS  -  I/O -  NÃO UTILIZE CONDICIONAIS OU LOOPS

t = float(input('Digite a temperatura: '))
u = float(input('Digite a umidade: '))
g = int(input('Digite a presença de gás inflamável (0 ou 1): '))

v = (t > 40 or u > 80) and g == 1 and "Crítico" or (t > 40 or u >80) and g == 0 and "Alto" or (t >=25 and t<=40) and (u >=50 and u <=80) and g ==0 and "Médio" or "Baixo"

print('Nível de risco: ', v)