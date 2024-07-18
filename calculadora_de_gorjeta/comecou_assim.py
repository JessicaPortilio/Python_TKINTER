import tkinter as tk  # Importa a biblioteca tkinter para criar interfaces gráficas
from tkinter import ttk, messagebox  # Importa classes específicas do tkinter e messagebox para mensagens

import sqlite3  # Importa a biblioteca sqlite3 para trabalhar com banco de dados SQLite

# Função para inicializar o banco de dados SQLite
def inicializar_banco():
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('calculadora_gorjetas.db')
    cursor = conn.cursor()
    
    # Criar a tabela 'gorjetas' se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gorjetas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conta_total REAL,
            gorjeta INTEGER,
            pessoas INTEGER,
            total_por_pessoa REAL,
            mesa INTEGER
        )
    ''')
    conn.commit()  # Confirmar as mudanças no banco de dados
    conn.close()   # Fechar a conexão com o banco de dados

# Função para inserir dados na tabela 'gorjetas'
def inserir_dados(conta_total, gorjeta, pessoas, total_por_pessoa, mesa):
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('calculadora_gorjetas.db')
    cursor = conn.cursor()
    
    # Inserir os dados na tabela 'gorjetas' sem o id (será autoincrementado)
    cursor.execute('''
        INSERT INTO gorjetas (conta_total, gorjeta, pessoas, total_por_pessoa, mesa)
        VALUES (?, ?, ?, ?, ?)
    ''', (conta_total, gorjeta, pessoas, total_por_pessoa, mesa))
    
    conn.commit()  # Confirmar as mudanças no banco de dados
    conn.close()   # Fechar a conexão com o banco de dados
    
    # Recarregar os dados na tabela Tkinter Treeview
    carregar_dados()

# Função para carregar os dados do banco de dados e exibir na tabela Tkinter Treeview
def carregar_dados():
    for row in tree.get_children():
        tree.delete(row)  # Deletar todas as linhas existentes na tabela
    
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('calculadora_gorjetas.db')
    cursor = conn.cursor()
    
    # Selecionar todos os registros da tabela 'gorjetas'
    cursor.execute('SELECT * FROM gorjetas')
    rows = cursor.fetchall()  # Obter todos os registros
    
    # Inserir os dados na tabela Tkinter Treeview
    for row in rows:
        # Formatar os valores para exibição correta
        id = row[0]
        conta_total = f'R${row[1]:.2f}'  # Formatando para exibir como valor monetário
        gorjeta = f'{row[2]}%'  # Adicionando o símbolo de porcentagem
        pessoas = row[3]
        total_por_pessoa = f'R${row[4]:.2f}'  # Formatando para exibir como valor monetário
        mesa = row[5]
        
        # Inserir os valores na tabela Tkinter Treeview
        tree.insert('', 'end', values=(id, conta_total, gorjeta, pessoas, total_por_pessoa, mesa))
    
    conn.close()  # Fechar a conexão com o banco de dados

# Função para deletar dados selecionados da tabela e do banco de dados
def deletar_dados():
    selected_item = tree.selection()  # Obter o item selecionado na tabela
    if not selected_item:
        messagebox.showerror("Erro", "Nenhum item selecionado!")  # Exibir mensagem de erro se nenhum item estiver selecionado
        return
    
    confirmar = messagebox.askyesno("Confirmação", "Deseja realmente deletar o item selecionado?")  # Confirmar a exclusão com o usuário
    if confirmar:
        item = tree.item(selected_item)
        id = item['values'][0]  # ID do item selecionado
        
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect('calculadora_gorjetas.db')
        cursor = conn.cursor()
        
        # Deletar o registro correspondente da tabela 'gorjetas' pelo ID
        cursor.execute('''
            DELETE FROM gorjetas WHERE id=?
        ''', (id,))
        
        conn.commit()  # Confirmar as mudanças no banco de dados
        conn.close()   # Fechar a conexão com o banco de dados
        
        # Deletar o item selecionado da tabela Tkinter Treeview
        tree.delete(selected_item)
        messagebox.showinfo("Sucesso", "Item deletado com sucesso!")  # Exibir mensagem de sucesso
        
        # Recarregar os dados na tabela Tkinter Treeview
        carregar_dados()

# Função para atualizar dados selecionados na tabela e no banco de dados
def atualizar_dados():
    selected_item = tree.selection()  # Obter o item selecionado na tabela
    if not selected_item:
        messagebox.showerror("Erro", "Nenhum item selecionado!")  # Exibir mensagem de erro se nenhum item estiver selecionado
        return
    
    try:
        conta_total = float(entry_conta.get())  # Obter o valor da conta total
        gorjeta = int(entry_gorjeta.get())     # Obter a porcentagem da gorjeta
        pessoas_dividir = int(entry_pessoas.get())  # Obter o número de pessoas
        mesa = int(entry_mesa.get())           # Obter o número da mesa
        
        # Calcular o total por pessoa com base nos valores inseridos
        total = (conta_total / pessoas_dividir) * (gorjeta / 100 + 1)
        total_formatado = f'R${total:.2f}'  # Formatando para exibir como valor monetário
        
        item = tree.item(selected_item)
        valores = item['values']  # Obter os valores do item selecionado na tabela
        
        # Obter o ID do item selecionado
        id_selecionado = valores[0]
        
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect('calculadora_gorjetas.db')
        cursor = conn.cursor()
        
        # Atualizar o registro correspondente na tabela 'gorjetas'
        cursor.execute('''
            UPDATE gorjetas SET conta_total=?, gorjeta=?, pessoas=?, total_por_pessoa=?, mesa=?
            WHERE id=?
        ''', (conta_total, gorjeta, pessoas_dividir, total, mesa, id_selecionado))
        
        conn.commit()  # Confirmar as mudanças no banco de dados
        conn.close()   # Fechar a conexão com o banco de dados
        
        # Atualizar os valores na tabela Tkinter Treeview
        tree.item(selected_item, values=(id_selecionado, f'R${conta_total:.2f}', f'{gorjeta}%', pessoas_dividir, total_formatado, mesa))
        messagebox.showinfo("Sucesso", "Item atualizado com sucesso!")  # Exibir mensagem de sucesso
        
        # Recarregar os dados na tabela Tkinter Treeview
        carregar_dados()
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos!")  # Exibir mensagem de erro se valores inválidos forem inseridos

# Função para calcular a gorjeta e adicionar na tabela e no banco de dados
def calcular_gorjeta():
    if entry_conta.get() != '' and entry_gorjeta.get() != '' and entry_pessoas.get() != '' and entry_mesa != '':
        try:
            conta_total = float(entry_conta.get())  # Obter o valor da conta total
            gorjeta = int(entry_gorjeta.get())     # Obter a porcentagem da gorjeta
            pessoas_dividir = int(entry_pessoas.get())  # Obter o número de pessoas
            mesa = int(entry_mesa.get())           # Obter o número da mesa
            
            # Calcular o total por pessoa com base nos valores inseridos
            total = (conta_total / pessoas_dividir) * (gorjeta / 100 + 1)
            total_formatado = f'R${total:.2f}'  # Formatando para exibir como valor monetário
            
            # Adiciona os dados na tabela Tkinter Treeview
            tree.insert('', 'end', values=(f'R${conta_total:.2f}', f'{gorjeta}%', pessoas_dividir, total_formatado, mesa))
            
            # Insere os dados no banco de dados SQLite
            inserir_dados(conta_total, gorjeta, pessoas_dividir, total, mesa)
            
            messagebox.showinfo("Resultado", f'Cada pessoa deverá pagar: {total_formatado}')  # Exibir resultado
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos!")  # Exibir mensagem de erro se valores inválidos forem inseridos
    else:
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")

# Função para limpar os campos de entrada
def limpar_campos():
    entry_conta.delete(0, tk.END)    # Limpar campo de entrada para a conta total
    entry_gorjeta.delete(0, tk.END) # Limpar campo de entrada para a porcentagem da gorjeta
    entry_pessoas.delete(0, tk.END) # Limpar campo de entrada para o número de pessoas
    entry_mesa.delete(0, tk.END)    # Limpar campo de entrada para o número da mesa

# Função para sair da aplicação
def sair():
    root.destroy()  # Fechar a janela principal

# Função para preencher os campos de entrada com os valores selecionados na tabela
def preencher_campos(event):
    selected_item = tree.selection()  # Obter o item selecionado na tabela
    if not selected_item:
        return  # Retornar se nenhum item estiver selecionado
    
    item = tree.item(selected_item)
    valores = item['values']  # Obter os valores do item selecionado na tabela
    
    # Preencher os campos de entrada com os valores do item selecionado
    entry_conta.delete(0, tk.END)
    entry_conta.insert(0, valores[1][2:])  # Remove "R$" e insere o valor da conta
    
    entry_gorjeta.delete(0, tk.END)
    entry_gorjeta.insert(0, valores[2][:-1])  # Remove "%" e insere a porcentagem da gorjeta
    
    entry_pessoas.delete(0, tk.END)
    entry_pessoas.insert(0, valores[3])  # Insere o número de pessoas
    
    entry_mesa.delete(0, tk.END)
    entry_mesa.insert(0, valores[5])  # Insere o número da mesa


# Cria a janela principal
root = tk.Tk()
root.title("Calculadora de Gorjetas")
root.geometry("600x500")  # Define o tamanho inicial da janela

# Inicializa o banco de dados
inicializar_banco()

# Título
label_title = tk.Label(root, text="Bem-vindo à calculadora de gorjetas!", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white")
label_title.pack(pady=10, fill=tk.X)  # Adiciona o título à janela

# Frame para os campos de entrada
frame_input = tk.Frame(root, bg="#E8F5E9")
frame_input.pack(pady=10, padx=10)  # Adiciona o frame de entrada à janela

# Campo para o valor da conta
label_conta = tk.Label(frame_input, text="Conta Total (R$):", bg="#E8F5E9")
label_conta.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_conta = tk.Entry(frame_input)
entry_conta.grid(row=0, column=1, padx=5, pady=5)

# Campo para a porcentagem da gorjeta
label_gorjeta = tk.Label(frame_input, text="Gorjeta (%):", bg="#E8F5E9")
label_gorjeta.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_gorjeta = tk.Entry(frame_input)
entry_gorjeta.grid(row=1, column=1, padx=5, pady=5)

# Campo para o número de pessoas
label_pessoas = tk.Label(frame_input, text="Número de Pessoas:", bg="#E8F5E9")
label_pessoas.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_pessoas = tk.Entry(frame_input)
entry_pessoas.grid(row=2, column=1, padx=5, pady=5)

# Campo para o número da mesa
label_mesa = tk.Label(frame_input, text="Número da Mesa:", bg="#E8F5E9")
label_mesa.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_mesa = tk.Entry(frame_input)
entry_mesa.grid(row=3, column=1, padx=5, pady=5)

# Frame para os botões
frame_botoes = tk.Frame(root, bg="#E8F5E9")
frame_botoes.pack(pady=10, padx=10)  # Adiciona o frame de botões à janela

# Botão para calcular a gorjeta
button_calcular = tk.Button(frame_botoes, text="Calcular", command=calcular_gorjeta, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
button_calcular.grid(row=0, column=0, padx=10, pady=10)


# Botão para atualizar dados
button_atualizar = tk.Button(frame_botoes, text="Atualizar", command=atualizar_dados, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"))
button_atualizar.grid(row=0, column=1, padx=10, pady=10)

# Botão para deletar dados
button_deletar = tk.Button(frame_botoes, text="Deletar", command=deletar_dados, bg="#F44336", fg="white", font=("Helvetica", 10, "bold"))
button_deletar.grid(row=0, column=2, padx=10, pady=10)

# Botão para limpar os campos de entrada
button_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar_campos, bg="#FFEB3B", fg="black", font=("Helvetica", 10, "bold"))
button_limpar.grid(row=0, column=3, padx=10, pady=10)

# Botão para sair da aplicação
button_sair = tk.Button(frame_botoes, text="Sair", command=sair, bg="#F44336", fg="white", font=("Helvetica", 10, "bold"))
button_sair.grid(row=0, column=4, padx=10, pady=10)

# Frame para a tabela
frame_tabela = tk.Frame(root)
frame_tabela.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)  # Adiciona o frame da tabela à janela

# Scrollbar para a tabela
scrollbar = tk.Scrollbar(frame_tabela)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Tabela para exibir os dados
tree = ttk.Treeview(frame_tabela, columns=("id", "conta", "gorjeta", "pessoas", "total", "mesa"), show="headings", yscrollcommand=scrollbar.set)
tree.pack(fill=tk.BOTH, expand=True)

# Configurar scrollbar
scrollbar.config(command=tree.yview)

# Definir os cabeçalhos da tabela
tree.heading("id", text="ID")
tree.heading("conta", text="Conta Total")
tree.heading("gorjeta", text="Gorjeta")
tree.heading("pessoas", text="Pessoas")
tree.heading("total", text="Total por Pessoa")
tree.heading("mesa", text="Mesa")

# Definir a largura das colunas
tree.column("id", width=80)
tree.column("conta", width=100)
tree.column("gorjeta", width=80)
tree.column("pessoas", width=80)
tree.column("total", width=120)
tree.column("mesa", width=100)

# Carregar os dados do banco de dados na tabela
carregar_dados()

# Adicionar evento de seleção na tabela
tree.bind("<<TreeviewSelect>>", preencher_campos)

# Iniciar o loop principal da interface
root.mainloop()
