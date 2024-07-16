import numpy as np

class Jogador:
    #classe que é usada como base para cada jogador e sua cor
    def __init__(self,cor : str,nome : str =None): #registra o nome, a cor e uma lista com as posições dos 4 pinos do jogador como atributos
        if nome==None:
            self.nome=cor
        else:
            self.nome=nome   
        self.pinos=[]
        self.cor=cor

    def cria_pinos(self):
        'cria os 4 pinos do jogador'
        self.pino0=Pino(self,self.cor,0,self.start)
        self.pino1=Pino(self,self.cor,1,self.start)
        self.pino2=Pino(self,self.cor,2,self.start)
        self.pino3=Pino(self,self.cor,3,self.start)
    
class Pino:
    #classe que é usada para cada pino independente
    def __init__(self,jogador : Jogador,cor,numero : int,posição : int,fora : bool=False): #registra o jogador a que pertence, a cor, o numero de identidade do pino, se está ou não fora do curral e sua posição como atributos, e adiciona a posição do pino a jogador.pinos
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
        'rola um d6'
        return np.random.randint(1,7)

    def andar(self):
        'faz o pino que está no tabuleiro andar conforme o resultado de um d6, caso ele esteja no curral executa o metodo para sair, não é possivel fazer um pino que chegou ao final andar'
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
        'caso o pino seja comido por outro devolve ele ao curral'
        jogador=self.jogador
        lugarvazio=[lugar for lugar in jogador.casas not in jogador.pinos]
        self.posição=lugarvazio[0]
        jogador.pinos[self.numero]=self.posicao
         
    def sair(self):
        'rola um d6 para tentar tirar o pino do curral'
        jogada=self.dado()
        if jogada==6:
            self.fora=True
            self.posicao=self.jogador.start

def verifica_em_cima(jogadora,pinA,jogadoresdic,pinos):
    'verifica se o pino atual comeu o pino de outro jogador que esteja fora das casas seguras'
    for jogadorb in jogadoresdic:
        seguro=(jogadorb.start,)+(24,37,50,63,74)
        if jogadora!=jogadorb:
            for pinob in pinos[jogadorb]:
                if pinA.posicao==pinob.posicao and pinob.posicao not in seguro:
                    pinob.morreu()
  
class Vermelho(Jogador):
    #classe que faz a diferenciação para o jogador da cor vermelha
    def __init__(self,nome=None,cor='Vermelho'): #adiciona os atributos especificos da cor
        super().__init__(cor,nome)
        self.casas=(12,13,14,15) #curral do jogador
        self.start=29 #casa na qual o pino entra no tabuleiro apos sair do curral
        self.tabuleiro=np.array([i for i in range(29,68)]+[i for i in range(16,28)]
                                +[i for i in range(87,93)]+[74]) #casas que os pinos do jogador vão percorrer
        
class Azul(Jogador):
    #classe que faz a diferenciação para o jogador da cor azul
    def __init__(self,nome=None,cor='Azul'):
        super().__init__(cor,nome)
        self.casas=(0,1,2,3) #curral do jogador
        self.start=16 #casa na qual o pino entra no tabuleiro apos sair do curral
        self.tabuleiro=np.delete(np.array([i for i in range(16,75)]),67) #casas que os pinos do jogador vão percorrer

class Verde(Jogador):
    #classe que faz a diferenciação para o jogador da cor verde
    def __init__(self,nome=None,cor='Verde'): #adiciona os atributos especificos da cor
        super().__init__(cor,nome)
        self.casas=(8,9,10,11) #curral do jogador
        self.start=42 #casa na qual o pino entra no tabuleiro apos sair do curral
        self.tabuleiro=np.array([i for i in range(42,68)]+[i for i in range(16,41)]
                                +[i for i in range(81,87)]+[74]) #casas que os pinos do jogador vão percorrer


class Amarelo(Jogador):
    #classe que faz a diferenciação para o jogador da cor amarela
    def __init__(self,nome=None,cor='Amarelo'): #adiciona os atributos especificos da cor
        super().__init__(cor,nome) 
        self.casas=(4,5,6,7) #curral do jogador
        self.start=55 #casa na qual o pino entra no tabuleiro apos sair do curral
        self.tabuleiro=np.array([i for i in range(55,68)]+[i for i in range(16,54)]
                                +[i for i in range(75,81)]+[74]) #casas que os pinos do jogador vão percorrer
