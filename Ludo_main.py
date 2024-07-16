from Ludo import *
import pandas as pd

def main():
    qtdjogadores=int(input('quantos jogadores?'))
    jogadoresdic={}
    pinos={}
    posicoespinos={}
    listaposicoes=[]
    
    i=1
    while i<qtdjogadores:
        cor=input('qual cor?')
        nome=f'jogador{i+1}'
        jogadoresdic[nome]=Jogador(cor,nome)
        i+=1
    for jogador in jogadoresdic:
        jogadoresdic[jogador].arcoiris()
        jogadoresdic[jogador].cria_pinos()
        
    for jogador in jogadoresdic:
        pinos[jogador]+=jogadoresdic[jogador].pino0
        pinos[jogador]+=jogadoresdic[jogador].pino1
        pinos[jogador]+=jogadoresdic[jogador].pino2
        pinos[jogador]+=jogadoresdic[jogador].pino3
    
    for nome in jogadoresdic:
        posicoespinos[nome]=jogadoresdic[nome].pinos
        
    
    while (74,74,74,74) not in listaposicoes:
        for jogador in jogadoresdic:
            pin=int(input('qual pino?'))
            pinA=pinos[jogador][pin]
            pinA.andar()
            verifica_emcima(jogador,pinA,jogadoresdic,pinos)
            posicoespinos[jogador]=jogadoresdic[jogador].pinos
            listaposicoes+=[posicoespinos[jogador]]
            ultimojogador=jogador
            ultimo_jogo=pd.DataFrame(posicoespinos)
    print(f'{ultimojogador} venceu')
    ultimo_jogo=pd.DataFrame(posicoespinos)
main()
    