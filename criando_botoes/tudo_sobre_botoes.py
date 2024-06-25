from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


# font tkinter

janela = Tk()

janela.title('Minha primeira Janela')

janela.geometry('600x700')

def mensagem():
    # print('Olá, Mundo!')
    messagebox.showinfo('Mensagem', 'Sejam Bem-vindos ao Canal')

rotulo = Label(janela, text='Exemplos de Botões Tkinter', font=('Arial', 20, 'bold'))
rotulo.pack(pady=10)

botao1 = Button(janela, text='Activebackground', activebackground='blue')
botao1.pack(pady=5)

botao2 = Button(janela, text='Activeforeground', activeforeground='red')
botao2.pack(pady=5)

botao3 = Button(janela, text='Bd', bd=5)
botao3.pack(pady=5)

botao4 = Button(janela, text='Bg', bg='yellow')
botao4.pack(pady=5)

botao5 = Button(janela, text='Command', command=mensagem)
botao5.pack(pady=5)

botao6 = Button(janela, text='Fg', fg='red')
botao6.pack(pady=5)

botao7 = Button(janela, text='Font', font=('Myriad Hebrew', 12, 'italic'))
botao7.pack(pady=5)

botao8 = Button(janela, text='Height', height=3)
botao8.pack(pady=5)

def foco_on(event):
    event.widget.config(bg='blue')

def perdeu_foco(event):
    event.widget.config(bg='SystemButtonFace')


botao9 = Button(janela, text='Highlightcolor')
botao9.pack(pady=5)

botao9.bind("<FocusIn>", foco_on)
botao9.bind("<FocusOut>", perdeu_foco)

imagem_original = Image.open('sair.jpg')
imagem_redimensionada = imagem_original.resize((150,50), Image.LANCZOS)
imagem = ImageTk.PhotoImage(imagem_redimensionada)

botao10 = Button(janela, text='Imagem', image=imagem)
botao10.pack(pady=5)

botao11 = Button(janela, text='Alinhando\nTexto\nA esquerda', justify=LEFT)
botao11.pack(pady=5)

botao12 = Button(janela, text='Padx', padx=20)
botao12.pack(pady=5)

botao13 = Button(janela, text='Pady', pady=20)
botao13.pack(pady=5)

botao14 = Button(janela, text='Padx e Pady', padx=20, pady=20)
botao14.pack(pady=5)

# Estilo de Borda (relief)
# RAISED, SUNKEN, FLAT, GROOVE, RIDGE
botao15 = Button(janela, text='Relief',relief=SUNKEN)
botao15.pack(pady=5)

# State -> Define o estado do botão (desativado, ativo, normal)
botao16 = Button(janela, text='State', state=DISABLED)
botao16.pack(pady=5)

botao17 = Button(janela, text='Underline', underline=0)
botao17.pack(pady=5)

botao18 = Button(janela, text='Width', width=20)
botao18.pack(pady=5)

botao19 = Button(janela, text='Define o comprimento em pixels para quebra de linha do texto no botão', wraplength=100)
botao19.pack(pady=5)

botao20 = Button(janela, text='Modificando Cursor', state=DISABLED, cursor="watch")
botao20.pack(pady=5)


janela.mainloop()