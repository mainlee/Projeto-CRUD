import random
import time
import numpy as np

listaVoo = []

maxAssentos = 30

def art():
  print('                                           ********')
  print('                                          *      *')
  print('                                         *      *')
  print('      ***********************************      *')
  print('    *  (  )      () () () () () ()            *')
  print('  *           *        *                   *')
  print(' *             *        *               *')
  print(' *************************************')
  print('                 *        *')
  print('                  ********** \n\n')
  print('========================================================')
  print('|               BEM-VINDO AO CANADÁ AIRLINES           |')
  print('========================================================')

def incluirVoo():
  
  voo = []
  
  print('========================================================') 
  print('\nINCLUSAO DE VOOS')
  
  print('\nDigite o número do voo:')
  incNumVoo = int(input())
  voo.append(incNumVoo)

  print('\nDigite a origem do voo:')
  incOriVoo = str(input())
  voo.append(incOriVoo)
  
  print('\nDigite o destino do voo:')
  incDestVoo = str(input())
  voo.append(incDestVoo)
  
  voo.append(maxAssentos)
  
  listaVoo.append(voo)
  
def mostrarVoo():
  print('Voo | Origem | Destino | Assentos Disponiveis')
  print(np.matrix(listaVoo))
  
def excluir():
  print('digite o numero do voo que deseja excluir: ')
  
  excluiVoo = int(input())
  
  i = 0
  while(i < len(listaVoo)):
    if(excluiVoo == listaVoo[i][0]):
      del listaVoo[i]
      print('\nVoo ' + str(excluiVoo) + ' excluido com sucesso!') 
    else:
      print('Voo não encontrado')
    i = i + 1
      
def fazReserva(listaVoo):
  print('Digite o numero do voo que deseja fazer a reserva: ')
  
  resVoo = int(input())
  
  i = 0
  if(len(listaVoo) == 0):
    print('nao há nenhum voo cadastrado!')
  
  while(i< len(listaVoo)):
    if(resVoo == listaVoo[i][0]):
      if(listaVoo[i][3] > 0 and listaVoo[i][3] <= 30):
        listaVoo[i][3] = listaVoo[i][3] - 1
        print('\nReserva efetuada com sucesso!\n')
      else:
        print('Voo lotado! Por favor selecione outro voo!')
    i = i + 1

def alteraVoo(listaVoo):
  print('Digite o número do voo que deseja alterar')
  altVoo = int(input())
  i = 0
  while(i<len(listaVoo)):
    if(altVoo == listaVoo[i][0]):
      print('Digite o novo local de origem:')
      listaVoo[i][1] = str(input())
      print('Digite o novo local do destino:')
      listaVoo[i][2] = str(input())
      inicia()
  i = i + 1
  
def inicia():
  opc = 0
  while(opc != 4):
    #Caso a pessoa digite 4 sairá do programa
    print("\nMenu de Opções:")
    print("\n1 - Consultar")
    print("\n2 - Efetuar reservas")
    print("\n3 - Editar voos")
    print("\n4 - Sair")
    print("\nDigite uma Opção: ")
    opc = int(input())
  
    #Caso a pessoa digite um número fora do intervalo 1 - 3
    while(opc<1 or opc>4):
        print('Opção invalida. Por favor digite novamente!')
        opc = int(input())
  
    #Caso a pessoa selecione o "Consultar"
    if(opc == 1):
      
      if(len(listaVoo) == 0):
        print('\n Não há voos registrados')
      
      else:
        mostrarVoo()
    elif(opc == 2):
      fazReserva(listaVoo)
      
    #Caso a pessoa selecione "Editar Voos"
    elif(opc == 3):
      
      edit = 0
      
      while(edit != 4):
        print('========================================================')
        print('\nMenu de edição de voos')
        print('\n1 - Incluir Voos')
        print('\n2 - Remover Voos')
        print('\n3 - Alterar Voo')
        print('\n4 - Voltar ao menu principal')
        edit = int(input())
        
        while(edit<1 or edit>4):
          print('Opção invalida. Por favor digite novamente!')
          edit = int(input())
          
        if(edit == 1):
          incluirVoo()
          
        elif(edit ==2):
          excluir()
          
        elif(edit == 3):
          alteraVoo(listaVoo)
          
art()
time.sleep(2)
inicia()
