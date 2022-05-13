import random as rnd

usuPalavra = []
splPalavra = []
chances = 6
acertos = 0
rodando = True
caminho = r"C:\Users\PICHAU\Desktop\Pastas\LDP - Geral\Python\OthersPrograms\JogoDaForca\palavras.txt"
utiliz = ''

def sorteiaPalavra():
    global splPalavra, palavra

    with open(caminho, encoding="utf8") as banco:
        bancoPalavras = banco.readlines()
    palavra = rnd.choice(bancoPalavras).strip().lower()
    splPalavra = list(palavra)
    for c in splPalavra:
        usuPalavra.append('-')    
    

def escrevePalavra():
    global usuPalavra
    out = ''
    id = 0

    for x in usuPalavra:
        out += usuPalavra[id]
        id += 1
    print(out)        


def verificaEsc():
    global usuPalavra, acertos, esc, splPalavra, chances, utiliz
    idx = 0
    cont = 0

    utiliz += esc + ' '
    for c in splPalavra:
        if esc.strip().lower() == splPalavra[idx] and usuPalavra[idx] == '-':
            usuPalavra[idx] = esc.strip().lower()    
            acertos += 1
        else:
            cont += 1        
        idx += 1
    if cont == len(splPalavra):
        chances -= 1  


def verificaVic():
    global usuPalavra, acertos, chances, rodando

    if acertos == len(usuPalavra):
        rodando = False
        escrevePalavra()
        print('Voce venceu!')
    elif chances == 0:
        rodando = False
        print(f'Voce perdeu! a palavra correta era {palavra}')
        

sorteiaPalavra()
while rodando:
    print(f'Chances restantes: {chances}')
    escrevePalavra()
    esc = input('Digite uma letra: ')
    print('')         
    verificaEsc()
    verificaVic()    
    print(f"Letras digitadas: {utiliz}") 
