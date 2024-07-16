import tkinter as tk
from tkinter import messagebox, ttk
from Ludo import *

class Menu:
    def __init__(self, root):
        self.master = root
        self.master.title('Ludo')
        self.master.geometry('700x700')
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)
        
        self.novojogo_instancia = Novojogo(root, self)
        self.cores_instancia = Cores(root, self)
        self.novojogo_instancia.set_cores_instancia(self.cores_instancia)
        
        bot_novojogo = tk.Button(self.frame, text='Novo Jogo', command=self.novojogo, width=20, height=2)
        bot_continuar = tk.Button(self.frame, text='Continuar Jogo', command=self.continuar, width=20, height=2)
        bot_sair = tk.Button(self.frame, text='Sair', command=self.sair, width=20, height=2)
        
        bot_novojogo.pack(pady=20)
        bot_continuar.pack(pady=20)
        bot_sair.pack(pady=20)
        
    def novojogo(self):
        self.frame.pack_forget()
        self.novojogo_instancia.frame.pack(expand=True)
        
    def continuar(self):
        messagebox.showinfo("Continuar Jogo", "Continuando o jogo...")
        
    def sair(self):
        self.master.quit()
        
class Novojogo:
    def __init__(self, root, menu):
        self.frame = tk.Frame(root)
        self.menu = menu
        
        label_qtdjogadores = tk.Label(self.frame, text="Escolha a quantidade de jogadores", font=("Helvetica", 16))
        label_qtdjogadores.pack(pady=20)

        bot_2jogadores = tk.Button(self.frame, text="2 Jogadores", command=lambda: self.qtd(2), width=20, height=2)
        bot_2jogadores.pack(pady=20)
    
        bot_3jogadores = tk.Button(self.frame, text="3 Jogadores", command=lambda: self.qtd(3), width=20, height=2)
        bot_3jogadores.pack(pady=20)
        
        bot_4jogadores = tk.Button(self.frame, text="4 Jogadores", command=lambda: self.qtd(4), width=20, height=2)
        bot_4jogadores.pack(pady=20)
        
        bot_voltar = tk.Button(self.frame, text="Voltar ao Menu", command=self.voltar, width=20, height=2)
        bot_voltar.pack(pady=20)
        
    def set_cores_instancia(self, cores):
        self.cores = cores
        
    def escolha_cor(self):
        self.frame.pack_forget()
        self.cores.frame.pack(expand=True)
        self.cores.escolha()
    
    def qtd(self, n):
        global qtd
        qtd = n
        self.escolha_cor()
        
    def voltar(self):
        self.frame.pack_forget()
        self.menu.frame.pack(expand=True)
        
class Cores:
    def __init__(self, root, menu):
        self.frame = tk.Frame(root)
        self.menu = menu
        
    def escolha(self):
        for widget in self.frame.winfo_children():
            widget.destroy()  
        
        escolhas={}
        cores = ["Vermelho", "Verde", "Azul", "Amarelo"]
    
        for i in range(qtd):
            tk.Label(self.frame, text=f"Nome do Jogador {i+1}:").pack(pady=5)
            nome=tk.Entry(self.frame).pack(pady=5)
    
            tk.Label(self.frame, text=f"Escolha a cor do Jogador {i+1}:").pack(pady=5)
            cor = ttk.Combobox(self.frame, values=cores, state="readonly")
            cor.pack(pady=5)
            
            escolhas[nome]=cor
        global jogadores
        tk.Button(self.frame, text="Iniciar Jogo", command=self.iniciar_jogo, width=20, height=2).pack(pady=20)
           
    def iniciar_jogo(self):
        for nome in jogadores:
            jogadores={}
            if escolhas[nome]=='Vermelho':
                jogadores[nome]=Vermelho(nome)
            elif escolhas[nome]=='Azul':
                jogador[nome]=Azul(nome)
            elif escolhas[nome]=='Verde':
                jogador[nome]=Verde(nome)
            else :
                jogadores[nome]=Amarelo(nome)
                
        

    def voltar(self):
        self.frame.pack_forget()
        self.menu.frame.pack(expand=True)

def main():
    root = tk.Tk()
    menu = Menu(root)
    root.mainloop()

main()
