import tkinter as tk
from Ludo import *

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
        self.desenhar_pinos()

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
                
    
    #def desenhar_pinos(self):
        # Posições iniciais dos pinos de cada jogador
       # posicoes = {
           # 'Vermelho': [vermelho.pino0.coordenada(), vermelho.pino1.coordenada(), vermelho.pino2.coordenada(), vermelho.pino3.coordenada()],
          #  'Verde': [verde.pino0.coordenada(), verde.pino1.coordenada(), verde.pino2.coordenada(), verde.pino3.coordenada()],
           # 'Azul': [azul.pino0.coordenada(), azul.pino1.coordenada(), azul.pino2.coordenada(), azul.pino3.coordenada()],
        #    'Amarelo': [amarelo.pino0.coordenada(), amarelo.pino1.coordenada(), amarelo.pino2.coordenada(), amarelo.pino3.coordenada()]
           #     }

        # Desenha os pinos de cada jogador nas posições iniciais
      #  for jogador, posicoes_iniciais in posicoes.items():
        #    cor = self.cores_jogadores[jogador]
          #  for x, y in posicoes_iniciais:
             #   x1, y1 = 13 + x * 42, 13 + y * 42
              #  x2, y2 = x1 + 30, y1 + 30
              #  self.canvas.create_oval(x1, y1, x2, y2, outline='black', fill=cor)

    def mover_pino_graficamente(self, jogador, pinA):
        casas = {
            0:(3,12),
            1:(4,12),
            2:(3,13),
            3:(4,13),
            4:(12,12),
            5:(13,12),
            6:(12,13),
            7:(13,13),
            8:(12,3),
            9:(13,3),
            10:(12,4),
            11:(13,4),
            12:(3,3),
            13:(4,3),
            14:(3,4),
            15:(4,4),
            16:(7,14),
            17:(7,13),
            18:(7,12),
            19:(7,11),
            20:(7,10),
            21:(6,9),
            22:(5,9),
            23:(4,9),
            24:(3,9),
            25:(2,9),
            26:(1,9),
            27:(1,8),
            28:(1,7),
            29:(2,7),
            30:(3,7),
            31:(4,7),
            32:(5,7),
            33:(6,7),
            34:(7,6),
            35:(7,5),
            36:(7,4),
            37:(7,3),
            38:(7,2),
            39:(7,1),
            40:(8,1),
            41:(9,1),
            42:(9,2),
            43:(9,3),
            44:(9,4),
            45:(9,5),
            46:(9,6),
            47:(10,7),
            48:(11,7),
            49:(12,7),
            50:(13,7),
            51:(14,7),
            52:(15,7),
            53:(15,8),
            54:(15,9),
            55:(14,9),
            56:(13,9),
            57:(12,9),
            58:(11,9),
            59:(10,9),
            60:(9,10),
            61:(9,11),
            62:(9,12),
            63:(9,13),
            64:(9,14),
            65:(9,15),
            66:(8,15),
            67:(7,15),
            68:(8,14),
            69:(8,13),
            70:(8,12),
            71:(8,11),
            72:(8,10),
            73:(8,9),
            74:(8,8),
            75:(14,8),
            76:(13,8),
            77:(12,8),
            78:(11,8),
            79:(10,8),
            80:(9,8),
            81:(8,2),
            82:(8,3),
            83:(8,4),
            84:(8,5),
            85:(8,6),
            86:(8,7),
            87:(2,8),
            88:(3,8),
            89:(4,8),
            90:(5,8),
            91:(6,8),
            92:(7,8),
         
             }
        coord = casas[pinA.posicao()]
        x = coord[0]
        y = coord[1]
        
        x1, y1 = 13 + x * 42, 13 + y * 42
        x2, y2 = x1 + 30, y1 + 30
        
        cor = self.cores_jogadores[jogador]
        self.canvas.create_oval(x1, y1, x2, y2, outline='black', fill=cor)
        
def escolher_botao(valor):
    global resultado
    resultado = valor-1
    root.destroy()  # Fecha a janela
    return resultado

def main_tabuleiro():
    root = tk.Tk()
    tabuleiro = LudoTabuleiro(root)
    root.mainloop()

if __name__ == "__main__":
    main()
