from tkinter import *

janela = Tk()

janela.title('Minha Primeira Janela')

janela.geometry('380x150')

texto_usuario = Label(janela, text='Usuário:')
texto_usuario.grid(row=0, column=0)

# Usuário: ______________________________
# Senha: ________________________________
entrada_usuario = Entry(janela, width=50)
entrada_usuario.grid(row=0, column=1)

texto_senha = Label(janela, text='Senha:')
texto_senha.grid(row=1, column=0)

entrada_senha = Entry(janela, width=50, show='*')
entrada_senha.grid(row=1, column=1)

def mensagem():
    nome = entrada_usuario.get()
    senha = entrada_senha.get()
    
    print(f'Usuário: {nome}')
    print(f'Senha: {senha}')

botao_entrar = Button(janela, text='Entrar', command=mensagem)
botao_entrar.grid(row=2, column=1)

janela.mainloop()