#===================================================================================
# Trabalho Prático - Python Básico
# Empresa: Colorê Personalizados
# Sistema de gerenciamento de usuários e produtos da empresa Colorê Personalizados
# Aluna: Daniela Madeira  
#===================================================================================

# Importa a biblioteca csv para leitura e gravação dos arquivos CSV.

import csv

#=======================
# Funções de usuários
#=======================

# Função: carregar_usuarios
# Descrição: Lê o arquivo usuarios.csv e carrega os usuários em uma lista.
# Entrada: Nenhuma.
# Saída: Retorna uma lista de usuários.

def carregar_usuarios():
    usuarios = []

    try:
        with open("usuarios.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                usuarios.append(linha)

    except FileNotFoundError:
        pass

    return usuarios

# Função: salvar_usuarios
# Descrição: Salva a lista de usuários no arquivo usuarios.csv.
# Entrada: Lista de usuários.
# Saída: Atualiza o arquivo usuarios.csv.

def salvar_usuarios(usuarios):
    with open("usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["usuario", "senha", "nivel"])

        for u in usuarios:
            escritor.writerow([
                u["usuario"],
                u["senha"],
                u["nivel"]
            ])

# Função: cadastrar_usuario
# Descrição: Cadastra um novo usuário no sistema.
# Entrada: Usuário, senha e nível informados pelo teclado.
# Saída: Adiciona o usuário ao arquivo usuarios.csv.

def cadastrar_usuario():
    usuarios = carregar_usuarios()

    usuario = input("Novo usuário: ")
    senha = input("Senha: ")
    nivel = input("Nível (gerente/funcionario): ")

    for u in usuarios:
        if u["usuario"] == usuario:
            print("Esse usuário já existe!")
            return

    novo = {
        "usuario": usuario,
        "senha": senha,
        "nivel": nivel
    }

    usuarios.append(novo)
    salvar_usuarios(usuarios)

    print("Usuário cadastrado com sucesso!")

# Função: listar_usuarios
# Descrição: Exibe todos os usuários cadastrados.
# Entrada: Nenhuma.
# Saída: Mostra os usuários na tela.

def listar_usuarios():
    usuarios = carregar_usuarios()

    print("\n=== LISTA DE USUÁRIOS ===")

    for u in usuarios:
        print(f"Usuário: {u['usuario']} | Nível: {u['nivel']}")


# Função: editar_usuario
# Descrição: Permite alterar a senha e o nível de um usuário cadastrado.
# Entrada: Nome do usuário, nova senha e novo nível.
# Saída: Atualiza os dados do usuário no arquivo usuarios.csv.

def editar_usuario():
    usuarios = carregar_usuarios()

    usuario = input("Digite o usuário que deseja editar: ")

    for u in usuarios:
        if u["usuario"] == usuario:
            print("Usuário encontrado!")

            nova_senha = input("Nova senha: ")
            novo_nivel = input("Novo nível (gerente/funcionario): ")

            u["senha"] = nova_senha
            u["nivel"] = novo_nivel

            salvar_usuarios(usuarios)

            print("Usuário atualizado com sucesso!")
            return

    print("Usuário não encontrado.")

# Função: excluir_usuario
# Descrição: Exclui um usuário cadastrado.
# Entrada: Nome do usuário.
# Saída: Remove o usuário do arquivo usuarios.csv.

def excluir_usuario():
    usuarios = carregar_usuarios()

    usuario = input("Digite o usuário que deseja excluir: ")

    for u in usuarios:
        if u["usuario"] == usuario:
            usuarios.remove(u)
            salvar_usuarios(usuarios)
            print("Usuário excluído com sucesso!")
            return

    print("Usuário não encontrado.")

#=======================
# Funções de produtos
#=======================

# Função: carregar_produtos
# Descrição: Lê o arquivo produtos.csv e carrega os produtos em uma lista.
# Entrada: Nenhuma.
# Saída: Retorna uma lista de produtos.

def carregar_produtos():
    produtos = []

    try:
       with open("produtos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            linha["preco"] = float(linha["preco"])
            linha["quantidade"] = int(linha["quantidade"])
            produtos.append(linha)

    except FileNotFoundError:
         pass

    return produtos

# Função: salvar_produtos
# Descrição: Salva a lista de produtos no arquivo produtos.csv.
# Entrada: Lista de produtos.
# Saída: Atualiza o arquivo produtos.csv.

def salvar_produtos(produtos):
    with open("produtos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["codigo", "nome", "preco", "quantidade"])

        for p in produtos:
            escritor.writerow([p["codigo"], p["nome"], p["preco"], p["quantidade"]])

# Função: cadastrar_produto
# Descrição: Cadastra um novo produto no sistema.
# Entrada: Código, nome, preço e quantidade do produto.
# Saída: Adiciona o produto ao arquivo produtos.csv.

def cadastrar_produto():
    produtos = carregar_produtos()

    codigo = input("Código: ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    # Verifica se já existe um produto cadastrado com o mesmo código.

    for p in produtos:
        if p["codigo"] == codigo:
            print("Produto já existe!")
            return

    novo = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(novo)
    salvar_produtos(produtos)

    print("Produto cadastrado com sucesso!")

# Função: listar_produtos
# Descrição: Exibe todos os produtos cadastrados.
# Entrada: Nenhuma.
# Saída: Mostra os produtos na tela.

def listar_produtos():
    produtos = carregar_produtos()

    print("\n=== LISTA DE PRODUTOS ===")

    for p in produtos:
        print(f"{p['codigo']} - {p['nome']} | R$ {p['preco']:.2f} | Quantidade: {p['quantidade']}")
        
# Função: buscar_produto
# Descrição: Busca um produto pelo código.
# Entrada: Código do produto.
# Saída: Exibe as informações do produto encontrado.

def buscar_produto():
    produtos = carregar_produtos()

    codigo = input("Código do produto: ")

    for p in produtos:
        if p["codigo"] == codigo:
            print(f"\nCódigo: {p['codigo']}")
            print(f"Nome: {p['nome']}")
            print(f"Preço: R$ {p['preco']:.2f}")
            print(f"Quantidade: {p['quantidade']}")
            return

    print("Produto não encontrado.")

# Função: editar_produto
# Descrição: Permite alterar os dados de um produto cadastrado.
# Entrada: Código do produto, novo nome, novo preço e nova quantidade.
# Saída: Atualiza as informações do produto no arquivo produtos.csv.

def editar_produto():
    produtos = carregar_produtos()

    codigo = input("Código do produto: ")

    for p in produtos:
        if p["codigo"] == codigo:
            p["nome"] = input("Novo nome: ")
            p["preco"] = float(input("Novo preço: "))
            p["quantidade"] = int(input("Nova quantidade: "))

            salvar_produtos(produtos)
            print("Produto atualizado com sucesso!")
            return

    print("Produto não encontrado.")

# Função: excluir_produto
# Descrição: Exclui um produto cadastrado.
# Entrada: Código do produto.
# Saída: Remove o produto do arquivo produtos.csv.

def excluir_produto():
    produtos = carregar_produtos()

    codigo = input("Código do produto: ")

    for p in produtos:
        if p["codigo"] == codigo:
            produtos.remove(p)
            salvar_produtos(produtos)
            print("Produto excluído com sucesso!")
            return

    print("Produto não encontrado.")

# Função: listar_por_nome
# Descrição: Lista todos os produtos em ordem alfabética pelo nome.
# Entrada: Nenhuma.
# Saída: Exibe os produtos ordenados por nome.

def listar_por_nome():
    produtos = carregar_produtos()

    produtos.sort(key=lambda p: p["nome"])

    print("\n=== PRODUTOS ORDENADOS POR NOME ===")

    for p in produtos:
        print(f"{p['codigo']} - {p['nome']} | R$ {p['preco']:.2f}")


# Função: listar_por_preco
# Descrição: Lista todos os produtos em ordem crescente de preço.
# Entrada: Nenhuma.
# Saída: Exibe os produtos ordenados por preço.

def listar_por_preco():
    produtos = carregar_produtos()

    produtos.sort(key=lambda p: p["preco"])

    print("\n=== PRODUTOS ORDENADOS POR PREÇO ===")

    for p in produtos:
        print(f"{p['codigo']} - {p['nome']} | R$ {p['preco']:.2f}")

#=========
# Login
#=========

# Função: login
# Descrição: Verifica se o usuário e a senha estão corretos.
# Entrada: Usuário e senha digitados.
# Saída: Retorna o nível de acesso do usuário.

def login():
    usuarios = carregar_usuarios()

    usuario_digitado = input("Usuário: ").strip()
    senha_digitada = input("Senha: ").strip()
    
    # Percorre a lista de usuários para verificar se o login é válido.
    for u in usuarios:
        if u["usuario"].strip() == usuario_digitado and u["senha"].strip() == senha_digitada:
            print(f"\nBem-vindo {u['usuario']}!")
            return u["nivel"]

    print("Usuário ou senha inválidos!")
    return None

#=========
# Menus
#=========

# Função: menu_gerente
# Descrição: Exibe o menu do gerente e executa as opções escolhidas.
# Entrada: Opção digitada pelo usuário.
# Saída: Executa as funções disponíveis para o gerente.

def menu_gerente():
    # Mantém o menu em execução até que o gerente escolha sair.
    while True:
        print("\n====== MENU GERENTE ======")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Editar usuário")
        print("4 - Excluir usuário")
        print("5 - Cadastrar produto")
        print("6 - Listar produtos")
        print("7 - Buscar produto")
        print("8 - Editar produto")
        print("9 - Excluir produto")
        print("10 - Listar produtos por nome")
        print("11 - Listar produtos por preço")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_usuario()

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            editar_usuario()

        elif opcao == "4":
            excluir_usuario()

        elif opcao == "5":
            cadastrar_produto()

        elif opcao == "6":
            listar_produtos()

        elif opcao == "7":
            buscar_produto()

        elif opcao == "8":
            editar_produto()

        elif opcao == "9":
            excluir_produto()

        elif opcao == "10":
            listar_por_nome()

        elif opcao == "11":
            listar_por_preco()

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")

# Função: menu_funcionario
# Descrição: Exibe o menu do funcionário.
# Entrada: Opção digitada pelo usuário.
# Saída: Executa as funções permitidas ao funcionário.

def menu_funcionario():
    # Mantém o menu em execução até que o funcionário escolha sair.
    while True:
        print("\n=== MENU FUNCIONÁRIO ===")
        print("1 - Listar produtos")
        print("2 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            listar_produtos()

        elif opcao == "2":
            break

#======================
# Programa principal
#======================

# Função: main
# Descrição: Inicia o sistema realizando o login e direcionando para o menu correspondente.
# Entrada: Usuário e senha.
# Saída: Executa o sistema até que o usuário escolha sair.

def main():

    # Executa o sistema até que seja realizado um login válido.

    while True:
        nivel = login()

        if nivel == "gerente":
            menu_gerente()
            break

        elif nivel == "funcionario":
            menu_funcionario()
            break

        else:
         print ("Usuário ou senha inválidos! Tente novamente.\n")

# Inicia a execução do programa.

if __name__ == "__main__":
    main()