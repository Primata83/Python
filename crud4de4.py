#------------------inicio da variaveis globais------------------
lista_livros = []
codigo_livro = 0
#-----------------fim das variaveis globais-----------------

#-----------------inicio de cadastrar produto-----------------
def cadastrar_livro(codigo):
  print('\n -----Bem vindo ao menu de Cadastrar Livro-----')
  print('Código do Produto {}'.format(codigo))
  id = input('Entre com o ID do Livro:')
  nome = input('Coloque o NOME do Livro:')
  autor = input('Nome do AUTOR do Livro:')
  editora = input('Nome da EDITORA do Livro:')
  id_global = {'id'      : id,
               'nome'    : nome,
               'autor'   : autor,
               'editora' : editora}
  lista_livros.append(id_global.copy())
#-----------------fim de cadastrar produto-----------------

#-----------------inicio de Consultar Livro-----------------
def consultar_livro():
  print('\n -----Bem vindo ao menu de Consultar Livros-----')
  while True:
    opcao_consultar = input('\n  Escolha a opção desejada: \n' +
                            '1 - Consultar TODOS Livros \n' +
                            '2 - Consultar Livros por ID \n' +
                            '3 - Consultar por AUTOR \n' +
                            '4 - Retornar \n' +
                            '>>>')
    if opcao_consultar == '1': # num menu, sempre se usa if, elif e else
      print('Você escolheu a opção Todos os Livros')
      for livro in lista_livros: # livro vai varrer toda a lista de livros
        print('--------------------------')
        for key, value in livro.items(): # varrer todos os conjuntos chave e valor do dicionario produto
          print('{}:{}' .format(key,value)) # imprime chave e valor no terminal
        print('--------------------------')
    elif opcao_consultar == '2':
      print('Você escolheu a opção Livros por ID')
      codigo_desejado = input('Entre com o ID do Livro:')
      for livro in lista_livros:
        if livro['id'] == codigo_desejado: # o valor do campo codigo desse id_global e igual o valor desejado
          print('--------------------------')
          for key, value in livro.items(): # varrer todos os conjuntos chave e valor do dicionario produto
            print('{}:{}' .format(key,value)) # imprime chave e valor no terminal
        print('--------------------------')
    elif opcao_consultar == '3':
      print('Você escolheu a opção Livro(s) por Autor')
      codigo_desejado = input('Escolha Livros por Autor:')
      for livro in lista_livros:
        if livro['autor'] == codigo_desejado: # o valor do campo codigo desse id_global e igual o valor desejado
          print('--------------------------')
          for key, value in livro.items(): # varrer todos os conjuntos chave e valor do dicionario produto
            print('{}:{}' .format(key,value)) # imprime chave e valor no terminal
        print('--------------------------')
    elif opcao_consultar == '4':
      return # sai da função contultar e volta para o menu
    else: # retorna para o inicio (da maneira mais comum)
      print('Opção invalida Tente Novamente')
      continue # continue faz voltar para o inicio do laço (é uma segunda maneira disso acontecer)
#-----------------fim de Consultar Livros-----------------

#-----------------inicio de Editar Livro-----------------
def editar_livro():
  print('-----Digite o ID do Livro para ser Editado-----')
  codigo_desejado = input('Entre com o ID do livro que deseja editar: ')
  for livro in lista_livros:
    if livro['id'] == codigo_desejado:
      print('Livro encontrado! Entre com os novos dados:')
      livro['nome'] = input('Coloque o NOVO NOME do Livro:')
      livro['autor'] = input('Nome do NOVO AUTOR do Livro:')
      livro['editora'] = input('Nome da NOVA EDITORA do Livro:')
      print('Livro atualizado com sucesso!')
      return
  print('Livro não encontrado.')
#-----------------fim de Editar Livro-----------------

#-----------------inicio de Remover Livro-----------------
def remover_livro():
  print('-----Digite o ID do Livro para ser Removido-----')
  codigo_desejado = input('Entre com o ID do produto que deseja remover: ')
  for livro in lista_livros:
    if livro['id'] == codigo_desejado:
      lista_livros.remove(livro)
      print('Livro Removido!')
#-----------------fim de Remover Livro-----------------

#-----------------INICIO DO MENU PRINCIPAL-----------------
print('---Bem Vindo ao Controle de Livros Primata---')
while True:
  opcao_principal = input('\n -----Escolha a opção desejada----- \n' +
                          '1 - Cadastrar Livros \n' +
                          '2 - Consultar Livros \n' +
                          '3 - Remover Livros \n' +
                          '4 - Editar Livros \n' +
                          '5 - Sair \n' +
                          '>>>')
  if opcao_principal == '1':
    codigo_livro = codigo_livro + 1
    cadastrar_livro(codigo_livro)
  elif opcao_principal == '2':
    consultar_livro()
  elif opcao_principal == '3':
    remover_livro()
  elif opcao_principal == '4':
    editar_livro()
  elif opcao_principal == '5':
    break
  else:
    print('Opção invalida Tente Novamente')
    continue
#-----------------FIM DO MENU PRINCIPAL-----------------

