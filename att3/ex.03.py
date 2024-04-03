def verifica_parenteses(expressao):
    pilha = []
    abre_parenteses = '({['
    fecha_parenteses = ')}]'
    correspondencia = {')': '(', '}': '{', ']': '['}

    for caractere in expressao:
        if caractere in abre_parenteses:
            pilha.append(caractere)
        elif caractere in fecha_parenteses:
            if not pilha:
                return False  
            elif pilha[-1] == correspondencia[caractere]:
                pilha.pop()
            else:
                return False  
    return not pilha 


expressao1 = "(())"
expressao2 = "()()(()())"
expressao3 = "( ) )"

print(expressao1, "=>", "OK" if verifica_parenteses(expressao1) else "Erro")
print(expressao2, "=>", "OK" if verifica_parenteses(expressao2) else "Erro")
print(expressao3, "=>", "OK" if verifica_parenteses(expressao3) else "Erro")
