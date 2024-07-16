import numpy as np

class Jogador:
    def __init__(self,cor : str,nome : str =None):
        if nome==None:
            self.nome=cor
        else:
            self.nome=nome   
        self.pinos=[]
        self.cor=cor

    def cria_pinos(self):
        self.pino0=Pino(self,self.cor,0,self.start)
        self.pino1=Pino(self,self.cor,1,self.start)
        self.pino2=Pino(self,self.cor,2,self.start)
        self.pino3=Pino(self,self.cor,3,self.start)
    
class Pino:
    def __init__(self,jogador : Jogador,cor,numero : int,posição : int,fora : bool=False):
        if fora==False:
            self.posicao=jogador.casas[numero]
        else:
            self.posicao=posição
            
        self.cor=cor
        self.jogador=jogador
        self.numero=numero
        self.fora=fora
        jogador.pinos+=[self.posicao]
        
    def dado(self):
        return np.random.randint(1,7)

    def andar(self):
        jogador=self.jogador
        if self.fora==False:
            self.sair()
        elif self.posicao!=74:
            indice_atual=np.where(jogador.tabuleiro==self.posicao)[0][0]
            casas=self.dado()
            novo_indice=indice_atual+casas
            self.posicao=jogador.tabuleiro[novo_indice]
            jogador.pinos[self.numero]=self.posicao
        
    def morreu(self):
        jogador=self.jogador
        lugarvazio=[lugar for lugar in jogador.casas not in jogador.pinos]
        self.posição=lugarvazio[0]
        jogador.pinos[self.numero]=self.posicao
         
    def sair(self):
        jogada=self.dado()
        if jogada==6:
            self.fora=True
            self.posicao=self.jogador.start

def verifica_emcima(jogadora,pinA,jogadoresdic,pinos):
    for jogadorb in jogadoresdic:
        seguro=(jogadorb.start,)+(24,37,50,63,74)
        if jogadora!=jogadorb:
            for pinob in pinos[jogadorb]:
                if pinA.posicao==pinob.posicao and pinob.posicao not in seguro:
                    pinob.morreu()
  
class Vermelho(Jogador):
    def __init__(self,nome=None,cor='Vermelho'):
        super().__init__(cor,nome)
        self.casas=(12,13,14,15)
        self.start=29
        self.tabuleiro=np.array([i for i in range(29,68)]+[i for i in range(16,28)]
                                +[i for i in range(87,93)]+[74])
        
class Azul(Jogador):
    def __init__(self,nome=None,cor='Azul'):
        super().__init__(cor,nome)
        self.casas=(0,1,2,3)
        self.start=16
        self.tabuleiro=np.delete(np.array([i for i in range(16,75)]),67)

class Verde(Jogador):
    def __init__(self,nome=None,cor='Verde'):
        super().__init__(cor,nome)
        self.casas=(8,9,10,11)
        self.start=42
        self.tabuleiro=np.array([i for i in range(42,68)]+[i for i in range(16,41)]
                                +[i for i in range(81,87)]+[74])


class Amarelo(Jogador):
    def __init__(self,nome=None,cor='Amarelo'):
        super().__init__(cor,nome)
        self.casas=(4,5,6,7)
        self.start=55
        self.tabuleiro=np.array([i for i in range(55,68)]+[i for i in range(16,54)]
                                +[i for i in range(75,81)]+[74])