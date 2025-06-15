def novo_arquivo():
    nome_arq = input('Digite o nome do novo arquivo: ')
    with open(nome_arq, 'w', encoding='utf-8') as arquivo:
        print(f'Arquivo {nome_arq} criado com sucesso!')
    return nome_arq

def abrir_arquivo():
    nome_arq = input('Digite o nome do arquivo que deseja abrir: ')
    with open(nome_arq, 'r', encoding='utf-8') as arquivo:
        print('\n--- Conteúdo do arquivo ---')
        print(arquivo.read())
    return nome_arq

def adicionar_tarefa(nome_arq):
    print(f'\nAdicionando tarefas ao arquivo: {nome_arq}')
    while True:
        tarefa = input('Digite a tarefa (ou digite "sair" para parar): ')
        if tarefa.lower() == 'sair':
            break
        with open(nome_arq, 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{tarefa}\n')
def remover_tarefa(nome_arq):
    print(f'\nRemovendo tarefas do arquivo: {nome_arq}')
    while True:
        tarefa = input('Digite a tarefa (ou digite "sair" para parar): ')
        if tarefa.lower() == 'sair':
            break
        with open(nome_arq, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
        with open(nome_arq, 'w', encoding='utf-8') as arquivo:
            for linha in linhas:
                if linha.strip() != tarefa:
                    arquivo.write(linha)

# Programa principal
#criando um novo arquivo
nv_arq = input('Deseja criar uma nova lista? (s/n): ').lower()

if nv_arq == 's':
    nome_arquivo = novo_arquivo()
    adicionar_tarefa(nome_arquivo)
    confirmar = input('deseja fazer mais alguma alteração? (s/n)')
 #removendo ou adicionando tarefa
    if confirmar == 's':
       modicaficar = input('O que deseja fazer?: (remover ou adicionar)')
       if modicaficar == 'remover':
           remover_tarefa(nome_arquivo)
       elif modicaficar == 'adicionar':
           adicionar_tarefa(nome_arquivo)

    else:

        print('Encerrando...')

#abrindo arquivo
elif nv_arq == 'n':
    nome_arquivo = abrir_arquivo()
    add_tf = input('Deseja adicionar uma tarefa? (s/n): ').lower()
    if add_tf == 's':
        adicionar_tarefa(nome_arquivo)
#removendo ou adicionando tarefa
        confirmar = input('deseja fazer mais alguma alteração? (s/n)').lower()
    if confirmar == 's':
       modicaficar = input('O que deseja fazer?: (remover ou adicionar)')
       if modicaficar == 'remover':
           remover_tarefa(nome_arquivo)
       elif modicaficar == 'adicionar':
           adicionar_tarefa(nome_arquivo)
#removendo tarefa
    else:
       modicaficar = input('Deseja remover alguma tarefa? (s/n)').lower()
       if modicaficar == 's':
           remover_tarefa(nome_arquivo)
       elif modicaficar == 'n':
            print('Encerrando...')

