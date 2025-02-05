from Ludo import *
from Menu  import *
from tabuleiro import *
import tkinter as tk

def main():
    root=tk.Tk()
    menu=Menu(root)
    root.mainloop()

    
    jogadoresdic=menu.cores_instancia.iniciar_jogo()
    root.quite()

    root=tk.Tk()
    tabuleiro = LudoTabuleiro(root)
    
    
    pinos={}
    listaposicoes=[]
    posicoespinos={}
    
    for jogador in jogadoresdic:
        jogadoresdic[jogador].cria_pinos()
        
    for jogador in jogadoresdic:
        pinos[jogador]+=jogadoresdic[jogador].pino0
        pinos[jogador]+=jogadoresdic[jogador].pino1
        pinos[jogador]+=jogadoresdic[jogador].pino2
        pinos[jogador]+=jogadoresdic[jogador].pino3
    
    while (74,74,74,74) not in listaposicoes:
        for jogador in jogadoresdic:
            root = tk.Tk()
            resultado = None
            for i in range(4):
                botao = tk.Button(root, text=str(i+1), command=lambda i=i: escolher_botao(i))
                botao.pack()
            root.mainloop()
            pin=resultado
            pinA=pinos[jogador][pin]
            pinA.andar()
            verifica_emcima(jogador,pinA,jogadoresdic,pinos)
            posicoespinos[jogador]=jogadoresdic[jogador].pinos
            listaposicoes+=[posicoespinos[jogador]]
            mover_pino_graficamente(jogador, pinA)
            tabuleiro.atualizar_tabuleiro()
            
    messagebox.showinfo("Vencedor", "Parabéns Você Ganhou o Jogo!!!")
    root.mainloop()
    root.quit()
    
main()
