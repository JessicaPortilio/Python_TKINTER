import tkinter as tk  # Importa a biblioteca tkinter para interface gráfica
from tkinter import ttk, messagebox  # Importa widgets ttk e messagebox de tkinter
from datetime import datetime  # Importa datetime para lidar com datas e horas
import sqlite3  # Importa sqlite3 para trabalhar com bancos de dados SQLite

# Função para inicializar o banco de dados SQLite
def inicializar_banco():
    conn = sqlite3.connect('calculadora_de_gorjetas.db')  # Conecta ao banco de dados
    cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
    
    # Cria a tabela 'gorjetas' se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gorjetas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conta_total REAL,
            gorjeta INTEGER,
            pessoas INTEGER,
            total_por_pessoa REAL,
            mesa INTEGER,
            data TEXT,
            garcom TEXT
        )
    ''')
    conn.commit()  # Confirma as alterações no banco de dados
    conn.close()  # Fecha a conexão com o banco de dados

# Função para inserir dados na tabela 'gorjetas'
def inserir_dados(conta_total, gorjeta, pessoas, total_por_pessoa, mesa, garcom):
    data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Obtém a data atual formatada
    conn = sqlite3.connect('calculadora_de_gorjetas.db')  # Conecta ao banco de dados
    cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
    
    # Insere os dados na tabela 'gorjetas'
    cursor.execute('''
        INSERT INTO gorjetas (conta_total, gorjeta, pessoas, total_por_pessoa, mesa, data, garcom)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (conta_total, gorjeta, pessoas, total_por_pessoa, mesa, data_atual, garcom))
    
    conn.commit()  # Confirma as alterações no banco de dados
    conn.close()  # Fecha a conexão com o banco de dados
    
    carregar_dados()  # Atualiza a exibição dos dados na tabela

# Função para calcular a gorjeta do garçom com base na conta total e na porcentagem da gorjeta
def calcular_gorjeta_garcom(conta_total, gorjeta):
    total_gorjeta = (conta_total * gorjeta) / 100  # Calcula a gorjeta do garçom
    return total_gorjeta  # Retorna o valor calculado da gorjeta do garçom

# Função para carregar os dados do banco de dados e exibir na tabela
def carregar_dados():
    for row in tree.get_children():
        tree.delete(row)  # Limpa os dados existentes na tabela
    
    conn = sqlite3.connect('calculadora_de_gorjetas.db')  # Conecta ao banco de dados
    cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
    
    cursor.execute('SELECT * FROM gorjetas')  # Seleciona todos os dados da tabela 'gorjetas'
    rows = cursor.fetchall()  # Obtém todas as linhas retornadas pela consulta
    
    # Itera sobre as linhas retornadas e exibe na tabela
    for row in rows:
        id = row[0]
        conta_total = f'R${row[1]:.2f}'  # Formata a conta total com duas casas decimais
        gorjeta = f'{row[2]}%'  # Adiciona o símbolo de percentagem à porcentagem da gorjeta
        pessoas = row[3]
        total_por_pessoa = f'R${row[4]:.2f}'  # Formata o total por pessoa com duas casas decimais
        mesa = row[5]
        data = row[6]
        garcom = row[7]
        
        # Insere os valores formatados na tabela
        tree.insert('', 'end', values=(id, conta_total, gorjeta, pessoas, total_por_pessoa, mesa, data, garcom))
    
    conn.close()  # Fecha a conexão com o banco de dados

# Função para deletar os dados selecionados da tabela
def deletar_dados():
    selected_item = tree.selection()  # Obtém o item selecionado na tabela
    if not selected_item:
        messagebox.showerror("Erro", "Nenhum item selecionado!")  # Exibe uma mensagem de erro se nenhum item estiver selecionado
        return
    
    confirmar = messagebox.askyesno("Confirmação", "Deseja realmente deletar o item selecionado?")  # Pergunta ao usuário se deseja confirmar a exclusão
    if confirmar:
        item = tree.item(selected_item)  # Obtém as informações do item selecionado
        id = item['values'][0]  # Obtém o ID do item selecionado
        
        conn = sqlite3.connect('calculadora_de_gorjetas.db')  # Conecta ao banco de dados
        cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
        
        cursor.execute('''
            DELETE FROM gorjetas WHERE id=?
        ''', (id,))  # Deleta o item da tabela onde o ID corresponde ao ID selecionado
        
        conn.commit()  # Confirma as alterações no banco de dados
        conn.close()  # Fecha a conexão com o banco de dados
        
        tree.delete(selected_item)  # Remove o item deletado da tabela
        messagebox.showinfo("Sucesso", "Item deletado com sucesso!")  # Exibe uma mensagem de sucesso
        carregar_dados()  # Atualiza a exibição dos dados na tabela

# Função para atualizar os dados selecionados na tabela
def atualizar_dados():
    selected_item = tree.selection()  # Obtém o item selecionado na tabela
    if not selected_item:
        messagebox.showerror("Erro", "Nenhum item selecionado!")  # Exibe uma mensagem de erro se nenhum item estiver selecionado
        return
    
    try:
        conta_total = float(entry_conta.get())  # Obtém o valor da conta total do campo de entrada
        gorjeta = int(entry_gorjeta.get())  # Obtém a porcentagem da gorjeta do campo de entrada
        pessoas_dividir = int(entry_pessoas.get())  # Obtém o número de pessoas do campo de entrada
        mesa = int(entry_mesa.get())  # Obtém o número da mesa do campo de entrada
        garcom = entry_garcom.get()  # Obtém o nome do garçom do campo de entrada
        
        # Calcula o total por pessoa com base nos dados atualizados
        total = (conta_total / pessoas_dividir) * (gorjeta / 100 + 1)
        total_formatado = f'R${total:.2f}'  # Formata o total por pessoa com duas casas decimais
        
        item = tree.item(selected_item)  # Obtém as informações do item selecionado na tabela
        valores = item['values']  # Obtém os valores do item selecionado
        
        id_selecionado = valores[0]  # Obtém o ID do item selecionado
        
        conn = sqlite3.connect('calculadora_de_gorjetas.db')  # Conecta ao banco de dados
        cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
        
        cursor.execute('''
            UPDATE gorjetas SET conta_total=?, gorjeta=?, pessoas=?, total_por_pessoa=?, mesa=?, garcom=?
            WHERE id=?
        ''', (conta_total, gorjeta, pessoas_dividir, total, mesa, garcom, id_selecionado))  # Atualiza os dados na tabela
        
        conn.commit()  # Confirma as alterações no banco de dados
        conn.close()  # Fecha a conexão com o banco de dados
        
        # Atualiza os valores do item na tabela com os novos dados atualizados
        tree.item(selected_item, values=(id_selecionado, f'R${conta_total:.2f}', f'{gorjeta}%', pessoas_dividir, total_formatado, mesa, valores[6], garcom))
        messagebox.showinfo("Sucesso", "Item atualizado com sucesso!")  # Exibe uma mensagem de sucesso
        
        carregar_dados()  # Atualiza a exibição dos dados na tabela
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos!")  # Exibe uma mensagem de erro se os valores inseridos não forem válidos

# Função para calcular a gorjeta e adicionar na tabela e no banco de dados
def calcular_gorjeta():
    if entry_conta.get() != '' and entry_gorjeta.get() != '' and entry_pessoas.get() != '' and entry_mesa.get() != '' and entry_garcom.get() != '':
        try:
            conta_total = float(entry_conta.get())  # Obtém o valor da conta total do campo de entrada
            gorjeta = int(entry_gorjeta.get())  # Obtém a porcentagem da gorjeta do campo de entrada
            pessoas_dividir = int(entry_pessoas.get())  # Obtém o número de pessoas do campo de entrada
            mesa = int(entry_mesa.get())  # Obtém o número da mesa do campo de entrada
            garcom = entry_garcom.get()  # Obtém o nome do garçom do campo de entrada
            
            # Calcula o total por pessoa com base nos dados inseridos
            total = (conta_total / pessoas_dividir) * (gorjeta / 100 + 1)
            total_formatado = f'R${total:.2f}'  # Formata o total por pessoa com duas casas decimais
            
            # Insere os dados na tabela e no banco de dados
            tree.insert('', 'end', values=(f'R${conta_total:.2f}', f'{gorjeta}%', pessoas_dividir, total_formatado, mesa, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), garcom))
            
            inserir_dados(conta_total, gorjeta, pessoas_dividir, total, mesa, garcom)  # Insere os dados no banco de dados
            
            gorjeta_garcom = calcular_gorjeta_garcom(conta_total, gorjeta)  # Calcula a gorjeta do garçom
            messagebox.showinfo("Resultado", f'Cada pessoa deverá pagar: {total_formatado}\nGorjeta do garçom: R${gorjeta_garcom:.2f}')  # Exibe o resultado
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos!")  # Exibe uma mensagem de erro se os valores inseridos não forem válidos
    else:
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")  # Exibe um aviso se todos os campos não estiverem preenchidos

# Função para limpar os campos de entrada
def limpar_campos():
    entry_conta.delete(0, tk.END)  # Limpa o campo de entrada 'Conta Total'
    entry_gorjeta.delete(0, tk.END)  # Limpa o campo de entrada 'Gorjeta'
    entry_pessoas.delete(0, tk.END)  # Limpa o campo de entrada 'Número de Pessoas'
    entry_mesa.delete(0, tk.END)  # Limpa o campo de entrada 'Número da Mesa'
    entry_garcom.delete(0, tk.END)  # Limpa o campo de entrada 'Garçom'

# Função para sair da aplicação
def sair():
    root.destroy()  # Fecha a janela principal da aplicação

# Função para preencher os campos de entrada com os valores selecionados na tabela
def preencher_campos(event):
    selected_item = tree.selection()  # Obtém o item selecionado na tabela
    if not selected_item:
        return  # Retorna se nenhum item estiver selecionado
    
    item = tree.item(selected_item)  # Obtém as informações do item selecionado
    valores = item['values']  # Obtém os valores do item selecionado na tabela
    
    # Preenche os campos de entrada com os valores do item selecionado
    entry_conta.delete(0, tk.END)
    entry_conta.insert(0, valores[1][2:])  # Insere o valor da conta total sem o símbolo 'R$'
    
    entry_gorjeta.delete(0, tk.END)
    entry_gorjeta.insert(0, valores[2][:-1])  # Insere a porcentagem da gorjeta sem o símbolo '%'
    
    entry_pessoas.delete(0, tk.END)
    entry_pessoas.insert(0, valores[3])  # Insere o número de pessoas
    
    entry_mesa.delete(0, tk.END)
    entry_mesa.insert(0, valores[5])  # Insere o número da mesa
    
    entry_garcom.delete(0, tk.END)
    entry_garcom.insert(0, valores[7])  # Insere o nome do garçom

# Criar a janela principal
root = tk.Tk()  # Cria uma instância da classe Tk para a janela principal
root.title("Calculadora de Gorjetas")  # Define o título da janela
root.geometry("900x600")  # Define as dimensões iniciais da janela

# Inicializar o banco de dados SQLite
inicializar_banco()

# Título da aplicação
label_title = tk.Label(root, text="Bem-vindo à calculadora de gorjetas!", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white")
label_title.pack(pady=10, fill=tk.X)  # Adiciona o título à janela com preenchimento horizontal

# Frame para os campos de entrada
frame_input = tk.Frame(root, bg="#E8F5E9")
frame_input.pack(pady=10, padx=10)  # Adiciona o frame de entrada à janela com preenchimento vertical e horizontal

# Label e campo de entrada para o valor da conta total
label_conta = tk.Label(frame_input, text="Conta Total (R$):", bg="#E8F5E9")
label_conta.grid(row=0, column=0, padx=5, pady=5, sticky="e")  # Adiciona a label com alinhamento à direita
entry_conta = tk.Entry(frame_input)
entry_conta.grid(row=0, column=1, padx=5, pady=5)  # Adiciona o campo de entrada

# Label e campo de entrada para a porcentagem da gorjeta
label_gorjeta = tk.Label(frame_input, text="Gorjeta (%):", bg="#E8F5E9")
label_gorjeta.grid(row=1, column=0, padx=5, pady=5, sticky="e")  # Adiciona a label com alinhamento à direita
entry_gorjeta = tk.Entry(frame_input)
entry_gorjeta.grid(row=1, column=1, padx=5, pady=5)  # Adiciona o campo de entrada

# Label e campo de entrada para o número de pessoas
label_pessoas = tk.Label(frame_input, text="Número de Pessoas:", bg="#E8F5E9")
label_pessoas.grid(row=2, column=0, padx=5, pady=5, sticky="e")  # Adiciona a label com alinhamento à direita
entry_pessoas = tk.Entry(frame_input)
entry_pessoas.grid(row=2, column=1, padx=5, pady=5)  # Adiciona o campo de entrada

# Label e campo de entrada para o número da mesa
label_mesa = tk.Label(frame_input, text="Número da Mesa:", bg="#E8F5E9")
label_mesa.grid(row=3, column=0, padx=5, pady=5, sticky="e")  # Adiciona a label com alinhamento à direita
entry_mesa = tk.Entry(frame_input)
entry_mesa.grid(row=3, column=1, padx=5, pady=5)  # Adiciona o campo de entrada

# Label e campo de entrada para o nome do garçom
label_garcom = tk.Label(frame_input, text="Garçom:", bg="#E8F5E9")
label_garcom.grid(row=4, column=0, padx=5, pady=5, sticky="e")  # Adiciona a label com alinhamento à direita
entry_garcom = tk.Entry(frame_input)
entry_garcom.grid(row=4, column=1, padx=5, pady=5)  # Adiciona o campo de entrada

# Frame para os botões
frame_botoes = tk.Frame(root, bg="#E8F5E9")
frame_botoes.pack(pady=10, padx=10)  # Adiciona o frame de botões à janela com preenchimento vertical e horizontal

# Botão para calcular a gorjeta
button_calcular = tk.Button(frame_botoes, text="Calcular", command=calcular_gorjeta, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
button_calcular.grid(row=0, column=0, padx=10, pady=10)  # Adiciona o botão com preenchimento e margens internas

# Botão para atualizar dados
button_atualizar = tk.Button(frame_botoes, text="Atualizar", command=atualizar_dados, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"))
button_atualizar.grid(row=0, column=1, padx=10, pady=10)  # Adiciona o botão com preenchimento e margens internas

# Botão para deletar dados
button_deletar = tk.Button(frame_botoes, text="Deletar", command=deletar_dados, bg="#F44336", fg="white", font=("Helvetica", 10, "bold"))
button_deletar.grid(row=0, column=2, padx=10, pady=10)  # Adiciona o botão com preenchimento e margens internas

# Botão para limpar os campos de entrada
button_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar_campos, bg="#FFEB3B", fg="black", font=("Helvetica", 10, "bold"))
button_limpar.grid(row=0, column=3, padx=10, pady=10)  # Adiciona o botão com preenchimento e margens internas

# Botão para sair da aplicação
button_sair = tk.Button(frame_botoes, text="Sair", command=sair, bg="#F44336", fg="white", font=("Helvetica", 10, "bold"))
button_sair.grid(row=0, column=4, padx=10, pady=10)  # Adiciona o botão com preenchimento e margens internas

# Frame para exibir a tabela
tree_frame = tk.Frame(root)
tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)  # Adiciona o frame com preenchimento vertical e horizontal e expansão

# Scrollbar para a tabela
tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)  # Adiciona a scrollbar à direita do frame

# Tabela para exibir os dados
tree = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height=15, yscrollcommand=tree_scroll.set)
tree.pack(fill=tk.BOTH, expand=True)  # Adiciona a tabela com preenchimento vertical e expansão

tree_scroll.config(command=tree.yview)  # Configura a scrollbar para controlar a visão vertical da tabela

# Configuração das colunas da tabela
tree.heading(1, text="ID")  # Configura o cabeçalho da coluna 1
tree.heading(2, text="Conta Total")  # Configura o cabeçalho da coluna 2
tree.heading(3, text="Gorjeta")  # Configura o cabeçalho da coluna 3
tree.heading(4, text="Pessoas")  # Configura o cabeçalho da coluna 4
tree.heading(5, text="Total por Pessoa")  # Configura o cabeçalho da coluna 5
tree.heading(6, text="Mesa")  # Configura o cabeçalho da coluna 6
tree.heading(7, text="Data")  # Configura o cabeçalho da coluna 7
tree.heading(8, text="Garçom")  # Configura o cabeçalho da coluna 8

tree.column(1, width=50)  # Configura a largura da coluna 1
tree.column(2, width=100)  # Configura a largura da coluna 2
tree.column(3, width=80)  # Configura a largura da coluna 3
tree.column(4, width=100)  # Configura a largura da coluna 4
tree.column(5, width=120)  # Configura a largura da coluna 5
tree.column(6, width=80)  # Configura a largura da coluna 6
tree.column(7, width=150)  # Configura a largura da coluna 7
tree.column(8, width=150)  # Configura a largura da coluna 8

tree.bind('<ButtonRelease-1>', preencher_campos)  # Liga a função de preencher campos ao evento de liberação do botão

# Carregar os dados do banco de dados na tabela
carregar_dados()

# Executar a aplicação
root.mainloop()
