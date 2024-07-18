from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import sqlite3

# Função para inicializar o banco de dados SQLite
def inicializar_banco():
    conectar = sqlite3.connect('calculadora_gorjetas.db') # Conectando ao banco de dados
    cursor = conectar.cursor() # Criando um cursor para executar comandos SQL
    
    # Criar a tabela 'gorjetas' se não existir
    
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS gorjetas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    total_conta REAL,
                    gorjeta INTEGER,
                    pessoas INTEGER,
                    total_por_pessoa REAL,
                    mesa INTEGER,
                    data TEXT,
                    garcom TEXT
                )
                ''')
    conectar.commit() # Confirmando as alterações no banco de dados
    conectar.close() # Fecha a conexão com o banco de dados

# Função para inserir dados na tabela 'gorjetas'
def inserir_dados(total_conta, gorjeta, pessoas, total_por_pessoa, mesa, garcom):
    data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Obtém a data atual formatada
    conectar = sqlite3.connect('calculadora_gorjetas.db') # Conectando ao banco de dados
    cursor = conectar.cursor() # Criando um cursor para executar comandos SQL

    # Inserir os dados na tabela 'gorjetas'
    cursor.execute('''
                INSERT INTO gorjetas (total_conta, gorjeta, pessoas, total_por_pessoa, mesa, data, garcom) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (total_conta, gorjeta, pessoas, total_por_pessoa, mesa, data_atual, garcom))
    
    conectar.commit() # Confirma as alterações no banco de dados
    conectar.close()
    
    carregar_dados() # Atualizar a exibição dos dados na tabela

# Função para calcular a gorjeta do garçom com base na conta total e na porcentagem da gorjeta
def calcular_gorjeta_garcom(total_conta, gorjeta):
    total_gorjeta = (total_conta * gorjeta) / 100 # Calculando a gorjeta do garçom 
    return total_gorjeta

# Função para carregar os dados do banco de dados e exibir na tabela
def carregar_dados():
    for row in tree.get_children():
        tree.delete(row) # Limpa os dados existentes na tabela
    
    conectar = sqlite3.connect('calculadora_gorjetas.db') # Conectando ao banco de dados
    cursor = conectar.cursor() # Criando um cursor para executar comandos SQL
    
    # Seleciona todas os dados da tabela 'gorjetas'
    cursor.execute('SELECT * FROM gorjetas')
    rows = cursor.fetchall() # Obtém todas as linhas retornadas pela consulta
    
    # Itera sobre as linhas retornadas e exibir na tabela
    for linha in rows:
        id = linha[0]
        total_conta = f'RS{linha[1]:.2f}'
        gorjeta = f'{linha[2]}%'
        pessoas = linha[3]
        total_por_pessoa = f'R${linha[4]:.2f}'
        mesa = linha[5]
        data = linha[6]
        garcom = linha[7]
        
        # Inserir os valores formatados na tabela
        tree.insert('', 'end', values=(id, total_conta, gorjeta, pessoas, total_por_pessoa, mesa, data, garcom))
    
    conectar.close() # Fechar a conexão com o banco de dados

# Função para deletar os dados selecionados da tabela
def deletar_dados():
    seleciona_item = tree.selection() # Obtém o item selecionado na tabela
    
    if not seleciona_item:
        messagebox.showerror('Erro', "Nenhum item selecionado!")
        return
    
    confirmar = messagebox.askyesno('Confirmação', 'Deseja realmente deletar o item selecionado?')
    if confirmar:
        item = tree.item(seleciona_item)
        id = item['values'][0] # Obtém o ID do item selecionado
        
        conectar = sqlite3.connect('calculadora_gorjetas.db') # Conectando ao banco de dados
        cursor = conectar.cursor() # Criando um cursor para executar comandos SQL
        
        cursor.execute('''
                    DELETE FROM gorjetas WHERE id=?
                    ''', (id, )) # Deleta o item da tabela onde o ID corresponde ao ID selecionado

        conectar.commit() # Confimando as alterações no banco de dados
        conectar.close() # Fecha a conexão com o banco de dados
        
        tree.delete(seleciona_item) # Remove o item deletado da tabela
        messagebox.showinfo('Sucesso', 'Item deletado com sucesso!')
        carregar_dados() # Atualizar a exibição dos dados na tabela

def atualizar_dados():
    seleciona_item = tree.selection() # Obtém o item selecionado na tabela
    
    if not seleciona_item:
        messagebox.showerror('Erro', "Nenhum item selecionado!")
        return

    try:
        total_conta = float(entry_conta.get())
        gorjeta = int(entry_gorjeta.get())
        pessoas_dividir = int(entry_pessoas.get())
        mesa = int(entry_mesa.get())
        garcom = entry_garcom.get()
            
            
        # Calcula o total por pessoa com base nos dados atualizados
        total = (total_conta / pessoas_dividir) * (gorjeta / 100 + 1)
        total_formatado = f'R${total:.2f}' # Formando o total por pessoa com duas casas decimais
        
        item = tree.item(seleciona_item) # Obtém as informações do item selecionado na tabela
        valores = item['values'] # Obtém os valores do item
        
        id_selecionado = valores[0] # Obtém o Id od item selecionada
        
        conectar = sqlite3.connect('calculadora_gorjetas.db') # Conectando ao banco de dados
        cursor = conectar.cursor() # Criando um cursor para executar comandos SQL
        
        cursor.execute('''
                    UPDATE gorjetas SET total_conta=?, gorjeta=?, pessoas=?, total_por_pessoa=?, mesa=?, garcom=?
                    WHERE id=?
                    ''', (total_conta, gorjeta, pessoas_dividir, total, mesa, garcom, id_selecionado)) # Atualizando os dados na tabela
        
        conectar.commit()
        conectar.close()
        
        # Atualizar os valores do item na tabela com os novos dados atualizados
        tree.item(seleciona_item, values=(id_selecionado, f'RS{total_conta:.2f}', f'{gorjeta}%', pessoas_dividir, total_formatado, mesa, valores[6], garcom))
        messagebox.showinfo('Sucesso', 'Item atualizado com sucesso!')
        
        carregar_dados()
    except ValueError:
        messagebox.showerror('Erro', 'Por favor, insira valores válidos!')
        
# Função para calcular a gorjeta e adicionar na tabela e no banco de dados
def calcular_gorjeta():
    if entry_conta.get() != '' and entry_gorjeta.get() != '' and  entry_pessoas.get() != '' and entry_mesa.get() != '' and entry_garcom.get() != '':
        try:
            total_conta = float(entry_conta.get())
            gorjeta = int(entry_gorjeta.get())
            pessoas_dividir = int(entry_pessoas.get())
            mesa = int(entry_mesa.get())
            garcom = entry_garcom.get()
            
            
            # Calcula o total por pessoa com base nos dados atualizados
            total = (total_conta / pessoas_dividir) * (gorjeta / 100 + 1)
            total_formatado = f'R${total:.2f}' # Formando o total por pessoa com duas casas decimais
            
            # Insere os dados na tabela e no banco de dados
            tree.insert('', 'end', values=(f'R${total_conta:.2f}', f'{gorjeta}%', pessoas_dividir, total_formatado, mesa, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), garcom))
            inserir_dados(total_conta, gorjeta, pessoas_dividir, total, mesa, garcom)
            
            gorjeta_garcom = calcular_gorjeta_garcom(total_conta, gorjeta)
            messagebox.showinfo('Resultado', f'Cada pessoa deverá pagar: {total_formatado}\nGorjeta do garçom: RS{gorjeta_garcom:.2f}')
        except ValueError:
            messagebox.showerror('Erro', 'Por favor, insira valores válidos')
            
    else:
        messagebox.showwarning('Aviso', 'Todos os campos devem ser preenchidos!')

# Função para limpar os campos de entrada
def limpar_campos():
    entry_conta.delete(0, END)
    entry_gorjeta.delete(0, END)
    entry_pessoas.delete(0, END)
    entry_mesa.delete(0, END)
    entry_garcom.delete(0, END)
    

# Função para sair da aplicação
def sair():
    root.destroy()

# Função para preencher os campos de entrada com os valores selecionados na tabela
def preencher_campos(event):
    seleciona_item = tree.selection() # Obtém o item selecionado na tabela
    
    if not seleciona_item:
        messagebox.showerror('Erro', "Nenhum item selecionado!")
        return

    item = tree.item(seleciona_item)
    valores = item['values']
    
    # Preenche os campos de entrada com os valores do item selecionado
    entry_conta.delete(0, END)
    entry_conta.insert(0, valores[1][2:])
    
    entry_gorjeta.delete(0, END)
    entry_gorjeta.insert(0, valores[2][:-1])
    
    entry_pessoas.delete(0, END)
    entry_pessoas.insert(0, valores[3])
    
    entry_mesa.delete(0, END)
    entry_mesa.insert(0, valores[5])
    
    entry_garcom.delete(0, END)
    entry_garcom.insert(0, valores[7])
    
# Criar a janela principal
root = Tk() # Instânciando a nossa classe TK para criar a nossa janela principal
root.title('Calculadora de Gorjetas') # Definindo o título da janela
root.geometry('900x600') # Definindo as dimensões inicias da janela

# Inicializar o banco de dados SQLite
inicializar_banco()

# Título da aplicação
label_title = Label(root, text='Bem-vindo(a) à calculadora de gorjetas!', font=('Helvetica', 16, 'bold'), bg='#4CAF50', fg='white')
label_title.pack(pady=10, fill=X)

# Frame para os campos de entrada
frame_input = Frame(root, bg='#E8F5e9')
frame_input.pack(pady=10, padx=10)

# Label e Campo de entrada para o valor da conta total
label_conta = Label(frame_input, text='Total da Conta (R$):', bg='#E8F5e9')
label_conta.grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry_conta = Entry(frame_input, width=30)
entry_conta.grid(row=0, column=1, padx=5, pady=5)

# Label e Campo de entrada para a porcentagem da gorjeta
label_gorjeta = Label(frame_input, text='Gorjeta (%):', bg='#E8F5e9')
label_gorjeta.grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_gorjeta = Entry(frame_input, width=30)
entry_gorjeta.grid(row=1, column=1, padx=5, pady=5)

# Label e campo de entrada para a porcentagem da gorjeta
label_gorjeta = Label(frame_input, text="Gorjeta (%):", bg="#E8F5E9")
label_gorjeta.grid(row=1, column=0, padx=5, pady=5, sticky='w')  # Adiciona a label com alinhamento à direita
entry_gorjeta = Entry(frame_input, width=30)
entry_gorjeta.grid(row=1, column=1, padx=5, pady=5)  # Adiciona o campo de entrada

# Label e campo de entrada para o número de pessoas
label_pessoas = Label(frame_input, text="Número de Pessoas:", bg="#E8F5E9")
label_pessoas.grid(row=2, column=0, padx=5, pady=5, sticky='w')  # Adiciona a label com alinhamento à direita
entry_pessoas = Entry(frame_input, width=30)
entry_pessoas.grid(row=2, column=1, padx=5, pady=5)  # Adiciona o campo de entrada

# Label e campo de entrada para o número da mesa
label_mesa = Label(frame_input, text="Número da Mesa:", bg="#E8F5E9")
label_mesa.grid(row=3, column=0, padx=5, pady=5, sticky='w')  # Adiciona a label com alinhamento à direita
entry_mesa = Entry(frame_input, width=30)
entry_mesa.grid(row=3, column=1, padx=5, pady=5)  # Adiciona o campo de entrada

# Label e campo de entrada para o nome do garçom
label_garcom = Label(frame_input, text="Garçom:", bg="#E8F5E9")
label_garcom.grid(row=4, column=0, padx=5, pady=5, sticky='w')  # Adiciona a label com alinhamento à direita
entry_garcom = Entry(frame_input, width=30)
entry_garcom.grid(row=4, column=1, padx=5, pady=5)  # Adiciona o campo de entrada


# Frame para os botões
frame_botoes = Frame(root, bg="#E8F5E9")
frame_botoes.pack(pady=10, padx=10)

# Botão para Calcular a Gorjeta
button_calcular = Button(frame_botoes, text='Calcular', command=calcular_gorjeta, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
button_calcular.grid(row=0, column=0, padx=10, pady=10)

# Botão para atualizar os dados
button_atualizar = Button(frame_botoes, text='Atualizar', command=atualizar_dados, bg='#2196F3', fg='white', font=('Helvetica', 10, 'bold'))
button_atualizar.grid(row=0, column=1, padx=10, pady=10)

# Botão para deletar os dados
button_deletar = Button(frame_botoes, text='Deletar', command=deletar_dados, bg='#F44336', fg='white', font=('Helvetica', 10, 'bold'))
button_deletar.grid(row=0, column=2, padx=10, pady=10)

# Botão para limpar os campos de entrada
button_limpar = Button(frame_botoes, text='Limpar', command=limpar_campos, bg='#FFEB3B', fg='black', font=('Helvetica', 10, 'bold'))
button_limpar.grid(row=0, column=3, padx=10, pady=10)

# Botão para sair da aplicação
button_sair = Button(frame_botoes, text='Sair', command=sair, bg='#F44336', fg='white', font=('Helvetica', 10, 'bold'))
button_sair.grid(row=0, column=4, padx=10, pady=10)

# Frame para exibir a tabela
tree_frame = Frame(root)
tree_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Scrollbar para a tabela
tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Tabela para exibir os dados
tree = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), show='headings', height=15, yscrollcommand=tree_scroll.set)
tree.pack(fill=BOTH, expand=True)

# Configurando o scrollbar para controlar a tabela vertical
tree_scroll.config(command=tree.yview)

# Configurando o cabeçalho da coluna
tree.heading(1, text='ID')
tree.heading(2, text='Total Conta')
tree.heading(3, text='Gorjeta')
tree.heading(4, text='Pessoas')
tree.heading(5, text='Total por Pessoa')
tree.heading(6, text='Mesa')
tree.heading(7, text='Data')
tree.heading(8, text='Garçom')

# Configurando a largura da coluna
tree.column(1, width=50)
tree.column(2, width=100)
tree.column(3, width=80)
tree.column(4, width=120)
tree.column(5, width=120)
tree.column(6, width=80)
tree.column(7, width=150)
tree.column(8, width=150)

# Liga a função preencher campos ao evento ded liberação do botão
tree.bind('<ButtonRelease-1>', preencher_campos)

# Carregar os dados do banco de dados na tabela
carregar_dados()

# Executar a aplicação
root.mainloop()