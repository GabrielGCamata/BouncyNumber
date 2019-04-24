# num = 10352

# print(num%10)
# num = num // 10
# print(num%10)
# print("  ")
# print(num%10)
# num = num // 10
# print(num%10)

#           Função para ver se o numero é Saltitante
def eh_bouncy(num):
    numeroDireita = num % 10 # número mais a direita
    numeroEsquerda = 0 # penultimo número mais a direita
    sequenciaIncremental = 0  # flag para ver se é crescente
    sequenciaDecremental = 0  # flag para ver se é decrescente

    num = num //10 #já leu o numero mais a direita, pega a parte inteira da divisao

    while num > 0:
        numeroEsquerda = num % 10
        if(numeroDireita > numeroEsquerda): # verifica se é decrescente
            sequenciaIncremental = 1
        if(numeroDireita < numeroEsquerda): # verifica se é crescente
            sequenciaDecremental = 1        
        if(sequenciaIncremental and sequenciaDecremental): # se existir uma sequencia crescente e decrescente no número significa que é Bouncy Number
            return 1
        num = num // 10 # anda uma casa, pega a parte inteira da divisao
        numeroDireita = numeroEsquerda # atualizo o mais a direita com o que era o penultimo
    return 0

### testando a funcao
# if (eh_bouncy(631) == 1):
#     print("numero saltitante")
# else:
#     print("numero nao é saltitante")

# if (eh_bouncy(567) == 1):
#     print("numero saltitante")
# else:
#     print("numero nao é saltitante")

#### Encontra o numero que a proporcao de bouncy number é passado
def porcentagem(proporcao):
    count = 0
    number = 99
    while count < proporcao/100 * number :
        if eh_bouncy(number):
            count += 1
        if count < proporcao/100 * number :
            number += 1
    return number

print(porcentagem(99))
