#Essa função faz a leitura do AFD de um arquivo.TXT e salva-o em uma lista
def leitura_afd():
  while True:
    nome_arq = str(input('Informe o nome do arquivo: ')).strip()+'.txt'
    try:
      arquivo = open(nome_arq, 'r')
      print('\nArquivo lido com sucesso!\nAFD Cadastrado:\n')
      print(arquivo.read())
      with open(nome_arq, 'r') as arquivo:
        afd = arquivo.readlines()
      arquivo.close()
      break
    except IOError:
      print('\nErro na leitura do arquivo!\n')
  return afd
#Essa função separa o alfabeto do AFD usando a 1ª linha do arquivo.TXT
def separar_alf(afd):
  cont_chav = 0
  alf = []
  for i in range(0, len(afd)):
    if cont_chav < 2 and afd[i]!=',' and afd[i]!='{' and afd[i]!='}' and afd[i]!=' ' and afd[i]!='(' and afd[i]!=')':
      alf.append(afd[i])
    if afd[i] == '{' or afd[i] == '}':
      cont_chav += 1
  return alf
#Essa função separa os estados do AFD usando a 1ª linha do arquivo.TXT
def separar_estados(afd):
  cont_chav = 0
  est = []
  aux = ' '
  i = contagem(afd, 1)
  while True:
    while afd[i]!=',':
      if cont_chav == 1:
        break
      if afd[i] == '}':
        cont_chav += 1
      if afd[i]!=',' and afd[i]!='{' and afd[i]!='}' and afd[i]!=' ' and afd[i]!='(' and afd[i]!=')' and cont_chav <= 1:
        aux = aux + afd[i]
      i += 1
    if cont_chav <= 1:
      if aux != ' ':
        est.append(aux)
      aux = ' '
    if cont_chav == 1:
      break
    i += 1
  return est
#Essa função separa o estado inicial do AFD usando a 1ª linha do arquivo.TXT
def separar_est_inicial(afd):
  est_inicial = ' '
  i = contagem(afd, 2)
  i += 2
  while afd[i] != ',':
    if afd[i] != ' ' and afd[i] != ',':
      est_inicial = est_inicial + afd[i]
    i += 1
  return est_inicial
#Essa função separa o(s) estado(s) final(is) do AFD usando a 1ª linha do arquivo.TXT
def separar_est_final(afd):
  cont_chav = chav_inicio = 0
  aux =' '
  est_final = []
  i = contagem(afd, 2)
  while True:
    while afd[i]!=',':
      if cont_chav == 1:
        break
      if afd[i] == '}':
        cont_chav += 1
      if afd[i] == '{':
        chav_inicio += 1
      if afd[i]!=',' and afd[i]!='{' and afd[i]!='}' and afd[i]!=' ' and afd[i]!='(' and afd[i]!=')' and cont_chav <= 1 and chav_inicio >= 1:
        aux = aux + afd[i]
      i += 1
    if cont_chav <= 1 and chav_inicio >=1:
      if aux != ' ':
        est_final.append(aux)
      aux = ' '
    if cont_chav == 1:
      break
    i += 1
  return est_final
#Essa função demarca desde qual posição de afd[0] o laço nas funções começará
def contagem(afd, pos):
  j = i = cont = 0
  while j < pos:
    if afd[i] == '}':
      j += 1
    cont += 1
    i += 1
  cont += 3
  return cont