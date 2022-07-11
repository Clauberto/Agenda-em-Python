from abc import ABC, abstractmethod
class Sistema(ABC): #Método abstrato para servir de "Fórmula" para o Sistema.
  @abstractmethod
  def getNome(self): #Retorna valor do nome.
    return self.nome
  @abstractmethod
  def getTelefone(self): #Retorna valor do telefone.
    return self.telefone
  def getDataNasc(self):
    return self.__datanascimento
   


class Telefone(Sistema): #Sistema Herando a fórmula do método Abstrato para funcionar.
  def __init__(self, nome, telefone, datanascimento):
    self.nome = nome
    self.telefone = telefone
    self.__datanascimento = datanascimento
  def getNome(self): #Retorna valor do nome.
    return self.nome
  def getTelefone(self): #Retorna valor do telefone.
    return self.telefone
  def getDataNasc(self):
    return self.__datanascimento
#Sistema de encapsulamento da data de nascimento.
  @property
  def datanascimento(self):
    return self.datanascimento
  @datanascimento.setter
  def datanascimento(self, nova_data):
    raise ValueError("Impossível alterar informações diretamente!")



class Acoes():
  def adcContato(nome, telefone, datanascimento):
    return Telefone(nome, telefone, datanascimento)

  def listarTodos(lista):
    for telefone in lista:
      print(f'Nome:{telefone.getNome()} | Telefone:{telefone.getTelefone()} | Data de nascimento: {telefone.getDataNasc()}')
  
  def deletarNome(lista, nome):
    if len(lista) != 0: #Se numero de registros da lista for diferente de zero então:
      contador = 0 #Sistema de contador de registros.
      for telefone in lista:
        if telefone.getNome() == nome: #Se nome capturado no getNome for igual ao nome solicitado -->
          lista.pop(contador) #Então elimina o de mesma posição
          return 'Contato foi removido com sucesso!'
        else: 
          return 'Nome não encontrado!'
    else:
      return 'Lista está vazia!' #Se o numero de registros for zero, então isso acontece.    