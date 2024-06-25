from tkinter import *
from tkinter import messagebox

janela = Tk()

janela.title('Minha Primeira Janela')

def mensagem():
    # print('Olá, Mundo!')
    messagebox.showinfo('Mensagem', 'Sejam Bem-vindos ao Canal')

botao = Button(janela, text='Clique aqui', command=mensagem)
botao.pack()

janela.mainloop()