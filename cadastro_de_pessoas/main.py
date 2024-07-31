import database

# Função para exibir o menu de opções
def menu():
    print('__________MENU__________')
    print('1. INSERIR PESSOA')
    print('2. ATUALIZAR PESSOA')
    print('3. DELETAR PESSOA')
    print('4. PESQUISAR PESSOA')
    print('5. LISTAR PESSOA')
    print('6. SAIR')


# Função para inserir uma nova pessoa
def inserir_pessoa():
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    email = input('Email: ')
    
    database.inserir_pessoa(nome, idade, email)
    print('Pessoa inserida com sucesso')
    lista_pessoas()
    
# Função para listar todas as pessoas
def lista_pessoas():
    pessoas = database.lista_as_pessoas()
    print('Lista de Pessoas:')
    for pessoa in pessoas:
        print(f'{pessoa[0]}, {pessoa[1]},  {pessoa[2]},  {pessoa[3]}')

# Função para atualizar os dados de uma pessoa
def atualizar_pessoa():
    id_pessoa = int(input('ID da Pessoa: '))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    email = input('Email: ')
    
    database.atualizar_pessoa(id_pessoa, nome, idade, email)
    print('Pessoa atualizada com sucesso!')
    lista_pessoas()


# Função para deletar uma pessoa:
def deletar_pessoa():
    id_pessoa = int(input('ID da Pessoa: '))
    database.deletar_pessoa(id_pessoa)
    print('Pessoa deletada com sucesso')
    lista_pessoas()

# Função para pesquisar uma pessoa pelo nome
def pesquisar_pessoa():
    nome = input('Nome: ')
    resultado = database.pesquisar_pessoa(nome)
    for linha in resultado:
        print(f'{linha[0]}, {linha[1]},  {linha[2]},  {linha[3]}')

def main():
    database.conectar()
    while True:
        menu()
        
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            inserir_pessoa()
        elif opcao == 2:
            atualizar_pessoa()
        elif opcao == 3:
            deletar_pessoa()
        elif opcao == 4:
            pesquisar_pessoa()
        elif opcao == 5:
            lista_pessoas()
        elif opcao == 6:
            break
        else:
            print('Opção Inválida')

# Verifica se o arquivo está sendo executado diretamente
if __name__ == '__main__':
    # Chamar a função principal para inicializar o programa
    main()