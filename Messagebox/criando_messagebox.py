from tkinter import *
from tkinter import messagebox

# Funções para exibir as mensagens
def mensagemInformacao():
    # Exibe uma mensagem de informação
    messagebox.showinfo('Informação', 'Bem-vindo(a) ao curso Tkinter! Esperamos que você aproveite e aprenda bastante.')

def mensagemAviso():
    # Exibe uma mensagem de aviso
    messagebox.showwarning('Aviso', 'Você está aprendendo Tkinter. Lembre-se de salvar seu progresso regularmente.')

def mensagemErro():
    # Exibe uma mensagem de erro
    messagebox.showerror('Erro', 'Ocorreu um erro ao carregar o sistema. Por favor, tente novamente mais tarde.')

def mensagemQuestao():
    # Exibe uma pergunta ao usuário e reage conforme a resposta
    resposta = messagebox.askquestion('Questão', 'Você sabia que o Tkinter é uma biblioteca GUI para Python?')
    if resposta == 'yes':
        # Se a resposta for 'sim', exibe uma mensagem de confirmação
        messagebox.showinfo('Informação', 'Parabéns! Você está no caminho certo.')
    else:
        # Se a resposta for 'não', exibe uma mensagem de erro
        messagebox.showerror('Erro', 'Resposta incorreta. Tkinter é, de fato, uma biblioteca GUI para Python.')

def mensagemOk_ou_Cancelar():
    # Exibe uma pergunta ao usuário com opções Ok ou Cancelar e reage conforme a resposta
    resposta = messagebox.askokcancel('Ok ou Cancelar', 'Deseja continuar com esta ação?')
    if resposta:
        # Se a resposta for Ok, prossegue com a ação
        messagebox.showinfo('Informação', 'Você optou por continuar. Prosseguindo...')
    else:
        # Se a resposta for Cancelar, exibe uma mensagem de aviso
        messagebox.showwarning('Aviso', 'Ação cancelada. Nenhuma alteração foi feita.')

def mensagemSim_ou_Nao():
    # Exibe uma pergunta ao usuário com opções Sim ou Não e reage conforme a resposta
    resposta = messagebox.askyesno('Sim ou Não', 'Você gostaria de realizar a buscar?')
    if resposta:
        # Se a resposta for Sim, prossegue com a busca
        messagebox.showinfo('Informação', 'Buscando o solicitado...')
    else:
        # Se a resposta for Não, exibe uma mensagem informando que a busca foi cancelada
        messagebox.showinfo('Informação', 'Busca cancelada. Nenhuma ação foi realizada.')

def mensagemRepetir_ou_Cancelar():
    # Exibe uma pergunta ao usuário com opções Repetir ou Cancelar e reage conforme a resposta
    resposta = messagebox.askretrycancel('Repetir ou Cancelar', 'Deseja tentar novamente a operação?')
    if resposta:
        # Se a resposta for Repetir, tenta a operação novamente
        messagebox.showinfo('Informação', 'Tentando novamente...')
    else:
        # Se a resposta for Cancelar, exibe uma mensagem informando que a operação foi cancelada
        messagebox.showinfo('Informação', 'Operação cancelada com sucesso.')

# Configuração da janela principal
janela = Tk()  # Cria uma nova janela principal
janela.geometry('400x550')  # Define as dimensões da janela
janela.title('Janela Principal')  # Define o título da janela
janela.config(bg='#2e2e2e')  # Define a cor de fundo da janela

# Label informativa
informacao = Label(janela, text='Mensagens', font=('Arial', 24), bg='#2e2e2e', fg='#ffffff')  # Cria um rótulo informativo
informacao.pack(pady=20)  # Adiciona o rótulo à janela com espaçamento

# Função para criar botões com estilo
def criar_botao(texto, comando):
    # Retorna um botão estilizado
    return Button(janela, text=texto, font=('Arial', 16), command=comando, bg='#007acc', fg='#ffffff', bd=0, highlightthickness=0, activebackground='#005f99', activeforeground='#ffffff')

# Criação dos botões
botaoInformacao = criar_botao('Informação', mensagemInformacao)  # Cria botão de informação
botaoAviso = criar_botao('Aviso', mensagemAviso)  # Cria botão de aviso
botaoErro = criar_botao('Erro', mensagemErro)  # Cria botão de erro
botaoQuestao = criar_botao('Questão', mensagemQuestao)  # Cria botão de questão
botaoOk_ou_Cancelar = criar_botao('Ok ou Cancelar', mensagemOk_ou_Cancelar)  # Cria botão Ok ou Cancelar
botaoSim_ou_Nao = criar_botao('Sim ou Não', mensagemSim_ou_Nao)  # Cria botão Sim ou Não
botaoRepetir_ou_Cancelar = criar_botao('Repetir ou Cancelar', mensagemRepetir_ou_Cancelar)  # Cria botão Repetir ou Cancelar

# Empacotamento dos botões
botoes = [botaoInformacao, botaoAviso, botaoErro, botaoQuestao, botaoOk_ou_Cancelar, botaoSim_ou_Nao, botaoRepetir_ou_Cancelar]  # Lista de botões
for botao in botoes:
    # Adiciona cada botão à janela com espaçamento e preenchimento horizontal
    botao.pack(pady=10, padx=20, fill=X)

botao_sair = Button(janela, text='Sair', font=('Arial', 16), command=janela.destroy, bg='red',fg='#ffffff', bd=0)
botao_sair.pack()

# Iniciar o loop principal
janela.mainloop()  # Inicia o loop principal da janela