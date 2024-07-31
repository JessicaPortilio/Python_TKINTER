from tkinter import *
from tkinter import messagebox
import random

lista_frutas = [
    'morango', 'abacaxi', 'uva'
]

lista_estados = [
    'são paulo', 'minas gerais', 'rio de janeiro'
]

estagios = [
    '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
  =======
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
  =======
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
  =======
    ''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =======
    ''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =======
    ''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
  =======
    ''',
    '''
    +---+
    |   |
        |
        |
        |
        |
  =======
    ''',
]

def nomrmalizar(texto):
    substituicoes = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
        'é': 'e', 'ê': 'e',
        'í': 'i',
        'ó': 'o', 'ô': 'o', 'õ': 'o',
        'ú': 'u',
        'ç': 'c'
    }
    return ''.join(substituicoes.get(c, c) for c in texto)

class ForcaJogo:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Jogo da Forca')
        self.opcao = StringVar(value='frutas')
        self.palavra_escolhida = ''
        self.palavra_normalizada = ''
        self.tamanho_palavra_escolhida = 0
        self.vidas = 6
        self.display = []
        self.palpites = set()
        self.primeira_janela()
        
    def primeira_janela(self):
        self.janela.geometry('500x400')
        self.frame_principal = Frame(self.janela)
        self.frame_principal.pack()
        
        # Título do Jogo
        titulo = Label(self.frame_principal, text='Jogo da Forca', font=("Comic Sans MS", 32, "bold"), fg='#00796B')
        titulo.grid(row=0, column=0, padx=10, pady=10)

        info_label = Label(self.frame_principal, text="Escolha a categoria:", font=("Comic Sans MS", 18), fg='#004D40')
        info_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.frame_radio = Frame(self.janela)
        self.frame_radio.pack(pady=5)
        
        opcao_frutas = Radiobutton(self.frame_radio, text='Frutas', variable=self.opcao, value='frutas', font=("Comic Sans MS", 18), fg='#004D40')
        opcao_frutas.grid(row=2, column=0, sticky='w', padx=5)
        
        opcao_estados = Radiobutton(self.frame_radio, text='Estados', variable=self.opcao, value='estados', font=("Comic Sans MS", 18), fg='#004D40')
        opcao_estados.grid(row=2, column=1, sticky='w', padx=5)
        
        opcao_ambos = Radiobutton(self.frame_radio, text='Ambos', variable=self.opcao, value='ambos', font=("Comic Sans MS", 18), fg='#004D40')
        opcao_ambos.grid(row=2, column=2, sticky='w', padx=5)
        
        self.frame_botao = Frame(self.janela)
        self.frame_botao.pack(pady=5)
        
        botao_iniciar =  Button(self.frame_botao, text='Iniciar Jogo', font=("Comic Sans MS", 22), 
                            bd=2, relief='ridge', bg='#80CBC4', fg='white', command=self.iniciar_jogo)
        botao_iniciar.grid(row=3, column=0, pady=50)
        
    def iniciar_jogo(self):
        opcao = self.opcao.get()
        if opcao == 'frutas':
            lista = lista_frutas
        elif opcao == 'estados':
            lista = lista_estados
        else:
            lista= lista_frutas + lista_estados
        
        self.palavra_escolhida = random.choice(lista)
        self.palavra_normalizada = nomrmalizar(self.palavra_escolhida)
        self.tamanho_palavra_escolhida = len(self.palavra_escolhida)
        self.display = [letra if letra == ' ' else '_' for letra in self.palavra_escolhida]
        self.palpites.clear()
        
        self.frame_principal.destroy()
        self.frame_radio.destroy()
        self.frame_botao.destroy()
        self.segunda_janela()
        
    def segunda_janela(self):
        self.janela.geometry('750x650')
        self.frame_principal = Frame(self.janela)
        self.frame_principal.pack()
        
        # Título do Jogo
        titulo = Label(self.frame_principal, text='Jogo da Forca', font=("Comic Sans MS", 32, "bold"), fg='#00796B')
        titulo.grid(row=0, column=0, padx=10, pady=10)
        
        dica = "Dica: é uma fruta" if self.opcao.get() == "frutas" \
            else "Dica: é um estado" if self.opcao.get() == "estados" else "Dica: é uma fruta ou um estado"
        info_label = Label(self.frame_principal, text=dica, font=("Comic Sans MS", 18), fg='#004D40')
        info_label.grid(row=1, column=0)

        self.frame_jogo = Frame(self.janela)
        self.frame_jogo.pack()
        
        self.estagio_label = Label(self.frame_jogo, text=estagios[self.vidas], font=("Courier New", 20),)
        self.estagio_label.grid(row=0, column=0)
        
        self.palavra_label = Label(self.frame_jogo, text=' '.join(self.display),  font=("Comic Sans MS", 28, "bold"), fg='#00796B')
        self.palavra_label.grid(row=1, column=0)
        
        self.frame_entrada = Frame(self.janela)
        self.frame_entrada.pack()
        
        self.entrada_palpite = Entry(self.frame_entrada, font=("Comic Sans MS", 24), width=5, justify='center', bd=2, relief='ridge', fg='#004D40')
        self.entrada_palpite.grid(row=2, column=0)
        self.entrada_palpite.bind("<Return>", self.verificar_palpite)
        
        palpites_label = Label(self.frame_entrada, text="Palpites:", font=("Comic Sans MS", 18),)
        palpites_label.grid(row=3, column=0, pady=5, sticky='w')
        
        self.historico_label = Label(self.frame_entrada,text="", font=("Comic Sans MS", 16), fg='#004D40')
        self.historico_label.grid(row=3, column=1, pady=5,)
        
        self.frame_botoes = Frame(self.janela)
        self.frame_botoes.pack()
        
        self.botao_reiniciar = Button(self.frame_botoes, text="Reiniciar Jogo", 
                                    font=("Comic Sans MS", 14), bd=2, relief='ridge', 
                                    bg='#80CBC4', fg='white', command=self.reiniciar_jogo)
        self.botao_reiniciar.grid(row=4, column=0, pady=5, padx=5)
        
        self.botao_escolher_categoria =  Button(self.frame_botoes, text="Escolher Categoria", 
                                                font=("Comic Sans MS", 14), bd=2, relief='ridge', 
                                                bg='#80CBC4', fg='white', command=self.voltar_para_categoria)
        self.botao_escolher_categoria.grid(row=4, column=1, pady=5, padx=5)

        self.sair = Button(self.frame_botoes, text="Sair", font=("Comic Sans MS", 14), 
                        bd=2, relief='ridge', bg='#80CBC4', 
                        fg='white', command=janela.destroy)
        self.sair.grid(row=4, column=2, pady=5, padx=5)
    
    def verificar_palpite(self, event=None):
        palpite = self.entrada_palpite.get().lower()
        self.entrada_palpite.delete(0, END)
        
        if len(palpite) != 1 or not palpite.isalpha():
            messagebox.showwarning("Palpite Inválido", "Digite apenas uma letra.")
            return
        
        if palpite in self.palpites:
            messagebox.showwarning("Palpite Repetido", "Você já tentou essa letra.")
            return
        
        self.palpites.add(palpite)
        
        if palpite in self.palavra_normalizada:
            for i, letra in enumerate(self.palavra_normalizada):
                if letra == palpite:
                    self.display[i] = self.palavra_escolhida[i]
            self.palavra_label.config(text=' '.join(self.display))
        else:
            self.vidas -= 1
            self.estagio_label.config(text=estagios[self.vidas])
        
        self.historico_label.config(text=', '.join(sorted(self.palpites)))
        
        if '_' not in self.display:
            messagebox.showinfo("Parabéns!", "Você ganhou!")
            self.reiniciar_jogo()
        elif self.vidas == 0:
            messagebox.showinfo("Fim de Jogo", f"Você perdeu! A palavra era '{self.palavra_escolhida}'")
            self.reiniciar_jogo()
            
    def reiniciar_jogo(self):
        self.palavra_escolhida = ''
        self.palavra_normalizada = ''
        self.vidas = 6
        self.display = []
        self.palpites.clear()
        self.frame_principal.destroy()
        self.frame_jogo.destroy()
        self.frame_entrada.destroy()
        self.frame_botoes.destroy()
        self.primeira_janela()
        
    def voltar_para_categoria(self):
        self.palavra_escolhida = ''
        self.palavra_normalizada = ''
        self.vidas = 6
        self.display = []
        self.palpites.clear()
        self.frame_principal.destroy()
        self.frame_jogo.destroy()
        self.frame_entrada.destroy()
        self.frame_botoes.destroy()
        self.primeira_janela()
        
janela = Tk()
jogo = ForcaJogo(janela)
janela.mainloop()
