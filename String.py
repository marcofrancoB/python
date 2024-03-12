s='Ferrari'
#concatenação
print('O carro '+s+'está na estrada') #interpolação
#string tratada como sequência
print('O tamanho de %s => %d' %s(s, len(s)))

for ch in s: print(ch) #string são Objetos
if s.starswith('F'): print(s.upper())
