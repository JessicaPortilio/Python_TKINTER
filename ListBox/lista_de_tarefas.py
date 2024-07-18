from tkinter import *
from tkinter import messagebox

def adicionar_tarefa():
    tarefa = entrada_tarefa_entry.get()

    if tarefa !='':
        lista_tarefas_listbox.insert(END, tarefa)
        entrada_tarefa_entry.delete(0, END)
    else:
        messagebox.showwarning('Aviso', 'Você precisa digitar uma tarefa.')

def remover_tarefa():
    try:
        indice_selecionado = lista_tarefas_listbox.curselection()[0]
        lista_tarefas_listbox.delete(indice_selecionado)
    except IndexError:
        messagebox.showwarning('Aviso', 'Você precisa selecionar uma tarefa para remover.')

def limpar_tarefa():
    lista_tarefas_listbox.delete(0, END)

def sair():
    janela.destroy()
    
janela = Tk()
janela.geometry('700x400')
janela.title('Lista de Tarefas')
janela.config(bg='#2e2e2e')

frame_tarefas = Frame(janela)
frame_tarefas.pack(pady=10)

lista_tarefas_listbox = Listbox(frame_tarefas, width=50, height=10, 
                    bg='#f0f0f0', bd=0, fg='#333333', selectbackground='#007acc')
lista_tarefas_listbox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(frame_tarefas)
scrollbar.pack(side=RIGHT, fill=BOTH)
lista_tarefas_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_tarefas_listbox.yview)

entrada_tarefa_entry = Entry(janela, font=('Arial', 14), bd=0, bg='#f0f0f0')
entrada_tarefa_entry.pack(pady=10)

frame_botoes = Frame(janela, bg='#2e2e2e')
frame_botoes.pack(pady=20)

def criar_botao(texto, comando):
    return Button(frame_botoes, text=texto, font=('Arial', 14), command=comando, 
                bg='#007acc', fg='#ffffff', bd=0, activebackground='#005f99', activeforeground='#ffffff')

botao_adicionar = criar_botao('Adicionar Tarefa', adicionar_tarefa)
botao_remover = criar_botao('Remover Tarefa', remover_tarefa)
botao_limpar = criar_botao('Limpar Tarefa', limpar_tarefa)
botao_sair = criar_botao('Sair', sair)

botao_adicionar.grid(row=0, column=0, padx=10, pady=5)
botao_remover.grid(row=0, column=1, padx=10, pady=5)
botao_limpar.grid(row=0, column=2, padx=10, pady=5)
botao_sair .grid(row=0, column=3, padx=10, pady=5)
janela.mainloop()