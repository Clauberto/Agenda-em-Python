from classe import *  
lista = []
while True: #Enquanto variavel não receber Break, permanece ativa.
  print("<=== Agenda Telefonica ===>")
  print('1 - Cadastrar contato')
  print('2 - Listar todos os contatos')
  print('3 - Eliminar um contato')
  print('4 - Sair')
  print("<==========================>")
  op = int(input('O que deseja fazer: '))
  if op == 1:
    nome = input('Digite o nome: ')
    telefone = int(input('Digite o telefone: '))
    datanascimento = input("Digite a data de nascimento: ")
    lista.append(Acoes.adcContato(nome, telefone, datanascimento)) #Envia dados do contato para método "Inserir". 
  elif op == 2:
    print(Acoes.listarTodos(lista)) #Extrai as informações da lista de contatos.
  elif op == 3:
    nome = input('Digite o nome para a pesquisa:')
    print(Acoes.deletarNome(lista, nome))
  elif op == 4:
    break #Quebra o codigo, fazendo assim a finalização do programa.
  else:
    print('Digite a opção correta!')
