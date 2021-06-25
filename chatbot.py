from time import sleep
import pyttsx3

def crie_matriz(n_linhas, n_colunas, valor):
    ''' (int, int, valor) -> matriz (lista de listas)

    	    Cria e retorna uma matriz com n_linhas linha e n_colunas
    	    colunas em que cada elemento é igual ao valor dado.
    	    '''
    matriz = []  # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = []  # lista vazia
        for j in range(n_colunas):
            linha.append(valor)
        # coloque linha na matriz
        matriz.append(linha)
    return matriz


def retorna_dicionario(frase1, resposta1):
    a = open('conversas.txt', 'a')
    a.write(frase1)
    a.write('=')
    a.write(' ')
    a.write(resposta1 + '\n')
    a.close()
    #for chave, valor in dicionario_inicial.items():
        #print(chave, valor)

        #return dicionario_inicial


'''
a = open("conversas.txt", "r")
matriz1 = crie_matriz(100,2," ")
n = 0
for linha1 in a:
    igual = linha1.find("=")
    pergunta = linha1[0:igual]
    resposta = linha1[igual + 1:]
    matriz1[n][0] = pergunta
    matriz1[n][1] = resposta
    n = n + 1
'''
print("CLERO versão 0.5")
print("""
||||||||||||    ||||||          |||||||||||||    ||||||||||||||||       |||||||||||||||||||
||||||||||||    ||||||          |||||||||||||    ||||||||||||||||       |||||||||||||||||||
||||||||||||    ||||||          ||||||           ||||||       |||       |||||||      ||||||
||||||          ||||||          ||||||           ||||||       |||       |||||||      ||||||
||||||          ||||||          |||||||||||||    ||||||||||||||||       |||||||      ||||||    
||||||||||||    ||||||          ||||||           ||||||       |||||     |||||||      ||||||    
||||||||||||    |||||||||||||   |||||||||||||    ||||||        |||||    |||||||||||||||||||               
||||||||||||    |||||||||||||   |||||||||||||    ||||||         |||||   ||||||||||||||||||| """)
while True:
    en = pyttsx3.init('sapi5')
    en.setProperty('voice', b'brazil')
    print("""Escolha: 
    [1] para instrucoes
    [2] para conversar 
    [3] para adicinar novas palavras/frases
    [4] para sair """)
    escolha = int(input("Numero: "))

    if escolha == 1:
        print("========================")
        print("PARA BOM USO DO CLERO!!!")
        print("========================")
        print("O CLERO é muito sensivel, procure não xinga-lo!")
        print("O CLERO também respeita normais gramaticais então, sempre coloque os pronomes nas frases!")
        print("Respeite as normas gramaticais!")
        print("Uma ultima coisa, como o CLERO é um  computador ele não gosta de acentos então  evite-os!")
        print("Tenha bom uso dele e até  mais!!!")
        sleep(7)


    if escolha == 2:
        print("Qual o seu nome? ")
        nome = str(input("Nome: "))
        #LerArquivoPessoasCadastradas(PessoasCadastradas)
        #PessoasCadastradas = open('pessoas.txt', 'r')
        #print(f"Seja bem vindo(a) {nome}")
        en.say(f"Seja bem vindo {nome}")
        en.runAndWait()
        sleep(0.2)
        #print("Eu sou o seu chat bot CLERO!\n Estou aqui para conversar com voce!")
        en.say("Eu sou o seu chat bot CLERO! Estou aqui para conversar com voce!")
        en.runAndWait()
        sleep(0.2)
        while True:
            a = open("conversas.txt", "r")
            matriz1 = crie_matriz(100, 2, " ")
            n = 0
            for linha1 in a:
                igual = linha1.find("=")
                pergunta = linha1[0:igual]
                resposta = linha1[igual + 1:]
                matriz1[n][0] = pergunta
                matriz1[n][1] = resposta
                n = n + 1
            conversa = str(input("Digite aqui: ")).lower().strip()
            if conversa == "tchau" or conversa == "Tchau":
                print("tchau!")
                break
            n = 0
            try:
                while True:
                    if conversa == matriz1[n][0]:
                        #en = pyttsx3.init('sapi5')
                        #en.setProperty('voice', b'brazil')
                        en.say(matriz1[n][1])
                        en.runAndWait()
                        print(matriz1[n][1])
                        break
                    else:
                        n = n + 1
            except:
                print("Desculpe nao entendi o que voce disse!")
                print("Gostaria de adicionar a frase/palavra no meu sistema? ")
                SimOuNao = input("Sim ou nao: ").upper()[0]
                if SimOuNao == "S":
                    frase = input("Qual frase/palavra devo aprender? ").lower().strip()
                    resposta = input("O que eu devo responder? ").lower().strip()
                    retorna_dicionario(frase, resposta)
                    print("Aprendido com sucesso!")
                else:
                    print("Ok...")


    if escolha == 3:
        #dicionario_inicial.clear()
        frase = input("Qual frase/palavra devo aprender? ").lower().strip()
        resposta = input("O que eu devo responder? ").lower().strip()
        retorna_dicionario(frase, resposta)
        print("Aprendido com sucesso!")


    if escolha == 4:
        print("Encerrando...")
        sleep(0.5)
        print("Encerrado")
        break


    if escolha >= 5:
        print("ERRO, digite uma opcao valida!!!")
