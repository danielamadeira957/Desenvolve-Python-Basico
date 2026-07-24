Documento Descritivo
Trabalho Prático – Python Básico

Empresa: Colorê Personalizados

Aluna: Daniela Madeira

1. Objetivo

Este trabalho tem como objetivo desenvolver um sistema de gerenciamento para a empresa Colorê Personalizados, utilizando a linguagem Python.

O sistema permite realizar o controle de usuários e produtos, utilizando arquivos CSV para armazenar as informações de forma permanente. Além disso, possui controle de acesso por login, diferenciando as permissões entre gerente e funcionário.

2. Descrição do Sistema

O sistema foi desenvolvido utilizando programação estruturada e dividido em funções, facilitando sua organização e manutenção.

Os dados são armazenados em dois arquivos:

usuarios.csv – armazena os usuários do sistema.
produtos.csv – armazena os produtos cadastrados.

Ao iniciar o programa, o usuário deve informar seu login e senha. Após a autenticação, o sistema identifica o nível de acesso e apresenta o menu correspondente.

3. Funcionalidades
3.1 Login

O sistema realiza a autenticação do usuário através do arquivo usuarios.csv.

Caso o usuário e a senha estejam corretos, o sistema identifica seu nível de acesso.

Existem dois níveis de acesso:

Gerente
Funcionário

Se o login estiver incorreto, o sistema solicita uma nova tentativa.

3.2 Gerenciamento de Usuários

Apenas o gerente possui acesso às funções de usuários.

As funcionalidades disponíveis são:

Cadastrar usuário;
Listar usuários;
Editar usuário;
Excluir usuário.

Durante o cadastro, o sistema verifica se já existe um usuário com o mesmo nome para evitar duplicidade.

3.3 Gerenciamento de Produtos

O sistema permite realizar o controle completo dos produtos cadastrados.

As operações disponíveis são:

Cadastrar produto;
Listar produtos;
Buscar produto pelo código;
Editar produto;
Excluir produto;
Listar produtos em ordem alfabética;
Listar produtos em ordem crescente de preço.

No cadastro é realizada a verificação para impedir o registro de códigos duplicados.

4. Estrutura do Programa

O programa foi dividido em funções para facilitar a organização do código.

As principais funções são:

carregar_usuarios()
salvar_usuarios()
cadastrar_usuario()
listar_usuarios()
editar_usuario()
excluir_usuario()
carregar_produtos()
salvar_produtos()
cadastrar_produto()
listar_produtos()
buscar_produto()
editar_produto()
excluir_produto()
listar_por_nome()
listar_por_preco()
login()
menu_gerente()
menu_funcionario()
main()

Cada função possui uma responsabilidade específica, tornando o código mais organizado e facilitando futuras alterações.

5. Estruturas Utilizadas

Durante o desenvolvimento foram utilizados diversos conceitos estudados na disciplina, como:

Variáveis;
Estruturas condicionais (if, elif e else);
Estruturas de repetição (for e while);
Funções;
Listas;
Dicionários;
Manipulação de arquivos CSV;
Biblioteca csv;
Ordenação de listas utilizando sort().
6. Fluxo de Funcionamento
O sistema é iniciado.
O usuário informa seu login e senha.
O sistema verifica as credenciais no arquivo usuarios.csv.
Caso o login seja válido:
Se for gerente, é exibido o menu completo.
Se for funcionário, é exibido o menu de consulta de produtos.
O usuário escolhe as operações desejadas.
Todas as alterações são gravadas automaticamente nos arquivos CSV.
O sistema permanece em execução até que seja escolhida a opção de sair.
7. Conclusão

O desenvolvimento deste trabalho permitiu aplicar na prática os principais conceitos de programação em Python estudados na disciplina. Foram utilizados arquivos CSV para armazenamento de dados, funções para modularização do código e estruturas de decisão e repetição para controlar o funcionamento do sistema.

O sistema atende ao objetivo proposto, permitindo o gerenciamento de usuários e produtos da empresa Colorê Personalizados de forma simples, organizada e funcional.

Esse documento está em um formato adequado para um trabalho de faculdade e é compatível com o código que você desenvolveu.