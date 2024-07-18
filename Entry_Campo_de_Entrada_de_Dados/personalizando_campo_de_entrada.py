from tkinter import *
from tkinter import messagebox

janela = Tk()

janela.title('Minha Primeira Janela')

janela.geometry('400x150')

texto_usuario = Label(janela, text='Usuário:', font=('Stencil Std', 12))
texto_usuario.grid(row=0, column=0, padx=5, pady=5)

entrada_usuario = Entry(janela, width=50, bd=5)
entrada_usuario.grid(row=0, column=1)

texto_senha = Label(janela, text='Senha:', font=('Stencil Std', 12))
texto_senha.grid(row=1, column=0, padx=5, pady=5)

entrada_senha = Entry(janela, width=50, show='*', bd=5)
entrada_senha.grid(row=1, column=1)

def mensagem():
    nome = entrada_usuario.get()
    senha = entrada_senha.get()
    
    if nome == 'jessica' and senha == '1234':
        messagebox.showinfo('Mensagem', f'Bem-Vindo(a) ao sistema, {nome}')
        # Limpa os campos de entrada após login bem-sucedido
        entrada_usuario.delete(0, END)
        entrada_senha.delete(0, END)
    else:
        messagebox.showerror('Error', 'Usuário ou Senha Inválida!')
        entrada_senha.delete(0, END)

def sair():
    janela.destroy()

frame_botoes = Frame(janela)
frame_botoes.grid(row=2, column=0, columnspan=2, pady=5)    

botao_entrar = Button(frame_botoes, text='Entrar', command=mensagem)
botao_entrar.pack(side=LEFT, padx=10)

botao_sair = Button(frame_botoes, text='Sair', command=sair)
botao_sair.pack(side=LEFT, padx=10)

janela.mainloop()