import tkinter as tk

class LudoTabuleiro:
    def __init__(self, master):
        self.master = master
        self.master.title("Tabuleiro de Ludo")
        self.master.geometry("700x700")
        
        # Cores para os jogadores
        self.cores_jogadores = {
            'Vermelho': 'red',
            'Azul': 'blue',
            'Verde': 'green',
            'Amarelo': 'yellow'
        }
        
        # Criando o canvas para desenhar o tabuleiro
        self.canvas = tk.Canvas(self.master, width=700, height=700, bg='white')
        self.canvas.pack()

        # Desenha o tabuleiro
        self.desenhar_tabuleiro()

        # Posiciona os pinos dos jogadores
        self.posicionar_pinos()

    def desenhar_tabuleiro(self):
        # Desenha as casas principais do tabuleiro
        for i in range(16):
            self.canvas.create_line(50, 50 + i * 42, 680, 50 + i * 42)
            self.canvas.create_line(50 + i * 42, 50, 50 + i * 42, 680)

        # Desenha as zonas seguras
        for i, cor in enumerate(['red', 'green']):
            self.canvas.create_rectangle(50 + i * 378, 50, 302 + i * 378, 92, fill=cor, outline='')
            self.canvas.create_rectangle(50 + i * 378, 302, 302 + i * 378, 260, fill=cor, outline='')
            self.canvas.create_rectangle(50 + i * 378, 92, 92 + i * 378, 260, fill=cor, outline='')
            self.canvas.create_rectangle(260 + i * 378, 92, 302 + i * 378, 260, fill=cor, outline='')

            
        for i, cor in enumerate(['red', 'green']):
            self.canvas.create_rectangle(92 + i * 294, 302 - i * 210, 134 + i * 294, 344 - i * 210, fill=cor, outline='black')

        for i, cor in enumerate(['blue', 'yellow']):
            self.canvas.create_rectangle(50 + i * 378, 428, 302 + i * 378, 470, fill=cor, outline='')
            self.canvas.create_rectangle(50 + i * 378, 680, 302 + i * 378, 638, fill=cor, outline='')
            self.canvas.create_rectangle(50 + i * 378, 470, 92
                                         + i * 378, 638, fill=cor, outline='')
            self.canvas.create_rectangle(260 + i * 378, 470, 302 + i * 378, 638, fill=cor, outline='')

        
        for i, cor in enumerate(['blue', 'yellow']):
            self.canvas.create_rectangle(302 + i * 294, 596 - i * 210, 344 + i * 294, 638 - i * 210, fill=cor, outline='black')

        # Desenha as zonas finais
        for i, cor in enumerate(['red', 'green']):
            self.canvas.create_polygon(302, 302, 365, 364, 302 + i * 126, 428 - i * 126, fill=cor, outline='black')
            
        for i, cor in enumerate(['blue', 'yellow']):
            self.canvas.create_polygon(302 + i * 126, 428 - i * 126, 365, 364, 428, 428, fill=cor, outline='black')
            
        # Desenha as estradas finais
        for i, cor in enumerate(['green', 'blue']):
            for j in range(5):
                self.canvas.create_rectangle(344, 92 + j * 42 + i * 336, 386, 134 + j * 42 + i * 336, fill=cor, outline='black')
        
        for i, cor in enumerate(['red', 'yellow']):
            for j in range(5):
                self.canvas.create_rectangle(92 + j * 42 + i * 336, 344, 134 + j * 42 + i * 336, 386, fill=cor, outline='black')
        
    def posicionar_pinos(self):
        # Posições iniciais dos pinos de cada jogador
        posicoes = {
            'Vermelho': [(2, 1), (1, 2), (2, 2), (1, 1)],
            'Verde': [(11, 2), (10, 1), (11, 1), (10, 2)],
            'Azul': [(1, 10), (2, 10), (1, 11), (2, 11)],
            'Amarelo': [(11, 10), (10, 10), (11, 11), (10, 11)]
        }

        # Desenha os pinos de cada jogador nas posições iniciais
        for jogador, posicoes_iniciais in posicoes.items():
            cor = self.cores_jogadores[jogador]
            for x, y in posicoes_iniciais:
                x1, y1 = 100 + x * 42, 100 + y * 42
                x2, y2 = x1 + 30, y1 + 30
                self.canvas.create_oval(x1, y1, x2, y2, outline='black', fill=cor)
                
                
def obter_coordenadas(event):
    x = event.widget.winfo_x()
    y = event.widget.winfo_y()
    print(f"Coordenadas X dentro da janela: {x}, Coordenadas Y dentro da janela: {y}")

def main():
    root = tk.Tk()
    tabuleiro = LudoTabuleiro(root)
    button = tk.Button(root, text="Clique aqui")
    button.pack()
    button.bind("<Button-1>", obter_coordenadas)
    root.mainloop()

if __name__ == "__main__":
    main()
