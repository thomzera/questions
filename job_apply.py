from time import sleep


def questaoUm():
    INDICE = 13
    SOMA = K = 0

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    print(f"Questao 1:\nResultado: {SOMA}")
    print("-"*50)


def questaoDois():
    '''
    Captura um inteiro e informa se pertence à sequência Fibonacci
    '''

    print("Questao 2:")

    # captura um número inteiro
    numero = int(input("Digite um número: "))

    primeiro = terceiro = 0
    segundo = 1

    # segue a lógica de Fibonacci até o número capturado.
    while terceiro < numero:
        terceiro = primeiro + segundo
        primeiro = segundo
        segundo = terceiro

    # retorna True se o número pertencer a sequencia.
    return terceiro == numero


def questaoTres():

    print("Questao 3:")

    dict = dados()

    # retorna o (primeiro) menor valor encontrado
    # o valor encontrado é um dia em que não houve faturamento
    minimo = min(dict, key=lambda v: v['valor'])

    dias_com_faturamento = [
        item for item in dict if item['valor'] > minimo['valor']]

    menor_faturamento = min(dias_com_faturamento, key=lambda v: v['valor'])
    maior_faturamento = max(dias_com_faturamento, key=lambda v: v['valor'])

    print(f'''O MENOR faturamento foi no dia {menor_faturamento['dia']} 
com o valor de R${round(menor_faturamento['valor'], 2)}
        '''
          )

    print(f'''O MAIOR faturamento foi no dia {maior_faturamento['dia']} 
com o valor de R${round(maior_faturamento['valor'], 2)}
        '''
          )

    total = round(sum([item['valor'] for item in dias_com_faturamento]), 3)
    media = round((total/len(dias_com_faturamento)), 3)

    faturamento_superior_media = [
        item for item in dias_com_faturamento if item['valor'] > media]

    print(f'''O número de dias no mês com faturamento
maior que a media é de: {len(faturamento_superior_media)}    
        '''
          )

    print("-"*50)


def questaoQuatro():
    '''
    SP - R$67.836,43
    RJ - R$36.678,66
    MG - R$29.229,88
    ES - R$27.165,48
    Outros - R$19.849,53
    '''

    print("Questao 4:")

    SP = 67836.43
    RJ = 36678.66
    MG = 29229.88
    ES = 27165.48
    OUTRO = 19849.53
    TOTAL = SP + RJ + MG + ES + OUTRO

    print(f'''
Representação percentual que cada Estado teve
dentro do valor total mensal da distribuidora.

SP: {round((SP/TOTAL)*100, 2)}%
RJ: {round((RJ/TOTAL)*100, 2)}%
MG: {round((MG/TOTAL)*100, 2)}%
ES: {round((ES/TOTAL)*100, 2)}%
OUTROS: {round((OUTRO/TOTAL)*100, 2)}%
    ''')

    print("-"*50)


def questaoCinco():
    '''
    Captura uma string e retorna a string com as palavras invertidas
    '''

    print("Questao 5:")

    frase = input('Digite uma frase ou uma palavra: ')

    frase_invertida = ""

    # percorre a frase/palavra de trás para frente e incrementa letra por letra
    for letra in frase.split(" "):
        frase_invertida += letra[::-1]+" "
    print(f"A frase que você digitou foi: {frase}")
    print(f"A frase que você digitou invertida fica: {frase_invertida}")
    print("-"*50)


def dados():
    data_dict = [
        {
            "dia": 1,
            "valor": 22174.1664
        },
        {
            "dia": 2,
            "valor": 24537.6698
        },
        {
            "dia": 3,
            "valor": 26139.6134
        },
        {
            "dia": 4,
            "valor": 0.0
        },
        {
            "dia": 5,
            "valor": 0.0
        },
        {
            "dia": 6,
            "valor": 26742.6612
        },
        {
            "dia": 7,
            "valor": 0.0
        },
        {
            "dia": 8,
            "valor": 42889.2258
        },
        {
            "dia": 9,
            "valor": 46251.174
        },
        {
            "dia": 10,
            "valor": 11191.4722
        },
        {
            "dia": 11,
            "valor": 0.0
        },
        {
            "dia": 12,
            "valor": 0.0
        },
        {
            "dia": 13,
            "valor": 3847.4823
        },
        {
            "dia": 14,
            "valor": 373.7838
        },
        {
            "dia": 15,
            "valor": 2659.7563
        },
        {
            "dia": 16,
            "valor": 48924.2448
        },
        {
            "dia": 17,
            "valor": 18419.2614
        },
        {
            "dia": 18,
            "valor": 0.0
        },
        {
            "dia": 19,
            "valor": 0.0
        },
        {
            "dia": 20,
            "valor": 35240.1826
        },
        {
            "dia": 21,
            "valor": 43829.1667
        },
        {
            "dia": 22,
            "valor": 18235.6852
        },
        {
            "dia": 23,
            "valor": 4355.0662
        },
        {
            "dia": 24,
            "valor": 13327.1025
        },
        {
            "dia": 25,
            "valor": 0.0
        },
        {
            "dia": 26,
            "valor": 0.0
        },
        {
            "dia": 27,
            "valor": 25681.8318
        },
        {
            "dia": 28,
            "valor": 1718.1221
        },
        {
            "dia": 29,
            "valor": 13220.495
        },
        {
            "dia": 30,
            "valor": 8414.61
        }
    ]

    return data_dict


def main():
    '''
    Funcao principal
    '''

    print("#"*100, '\n'*30)

    # questao 1
    sleep(0.5)
    questaoUm()

    # questao 2
    sleep(1)
    if questaoDois():
        print("Resultado: O numero FAZ parte da sequência de Fibonacci")
        print("-"*50)
    else:
        print("Resultado: O numero NAO FAZ parte da sequência de Fibonacci")
        print("-"*50)

    # questao 3
    sleep(2)
    questaoTres()

    # questao 4
    sleep(2)
    questaoQuatro()

    # questao 5
    sleep(2)
    questaoCinco()

    print("#"*100)


if __name__ == "__main__":
    main()
