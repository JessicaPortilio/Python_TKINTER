from tkinter import *

janela = Tk()
janela.geometry('400x300')
janela.title('Janela Principal')

def atualizarLabel():
    texto_Da_Cor_Selecionada.config(text=f'Cor selecionada: {cor.get()}')

cor = StringVar()
cor.set('Azul')
# variable -> Variável de controle que rastreia o estado do checkbutton
radioAzul = Radiobutton(janela, text='Azul', variable=cor, value='Azul', command=atualizarLabel)
radioAzul.pack(anchor='w', padx=20, pady=5)

radioVermelho = Radiobutton(janela, text='Vermelho', variable=cor, value='Vermelho', command=atualizarLabel)
radioVermelho.pack(anchor='w', padx=20, pady=5)

radioVerde = Radiobutton(janela, text='Verde', variable=cor, value='Verde', command=atualizarLabel)
radioVerde.pack(anchor='w', padx=20, pady=5)

radioAmarelo = Radiobutton(janela, text='Amarelo', variable=cor, value='Amarelo', command=atualizarLabel)
radioAmarelo.pack(anchor='w', padx=20, pady=5)

texto_Da_Cor_Selecionada = Label(janela, text='Cor selecionada: Azul', font=('Arial', 14))
texto_Da_Cor_Selecionada.pack(pady=20)

janela.mainloop()