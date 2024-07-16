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
        self.menu.frame.pack_forget()  
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
        self.jogadores = []  
    
    def escolha(self):
        for widget in self.frame.winfo_children():
            widget.destroy()  
        
        cores_disponiveis = ["Vermelho", "Verde", "Azul", "Amarelo"]
        self.jogadores = []  
        
        for i in range(qtd):
            jogador = {}
            
            label_nome = tk.Label(self.frame, text=f"Nome do Jogador {i+1}:")
            label_nome.pack(pady=5)
            nome_entry = tk.Entry(self.frame)
            nome_entry.pack(pady=5)
            jogador['nome'] = nome_entry
            
            label_cor = tk.Label(self.frame, text=f"Escolha a cor do Jogador {i+1}:")
            label_cor.pack(pady=5)
            cor_var = tk.StringVar()
            combobox = ttk.Combobox(self.frame, textvariable=cor_var, values=cores_disponiveis, state="readonly")
            combobox.pack(pady=5)
            jogador['cor'] = cor_var
            
            self.jogadores.append(jogador)
        
        botao_iniciar = tk.Button(self.frame, text="Iniciar Jogo", command=self.iniciar_jogo, width=20, height=2)
        botao_iniciar.pack(pady=20)
           
        bot_voltar = tk.Button(self.frame, text="Voltar ao Menu", command=self.voltar, width=20, height=2)
        bot_voltar.pack(pady=20)
        
    def iniciar_jogo(self):
        jogadores = {}
        
        for jogador in self.jogadores:
            nome_jogador = jogador['nome'].get()
            cor_escolhida = jogador['cor'].get()
            
            if cor_escolhida == 'Vermelho':
                jogadores[nome_jogador]=Vermelho(nome_jogador)
            elif cor_escolhida == 'Azul':
                jogadores[nome_jogador]=Azul(nome_jogador)
            elif cor_escolhida == 'Verde':
                jogadores[nome_jogador]=Verde(nome_jogador)
            elif cor_escolhida == 'Amarelo':
                jogadores[nome_jogador]=Amarelo(nome_jogador)
        return jogadores
         
    def voltar(self):
        self.frame.pack_forget()
        self.menu.frame.pack(expand=True)
