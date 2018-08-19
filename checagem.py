def testar_estado_final(est_final, estados_finais):
  teste = 0
  for i in range(0, len(estados_finais)):
    if est_final == estados_finais[i]:
      teste += 1
  return teste
def testar_estado_atual(est_atingido, transicao):
  num_virg = 0
  est_atual = ' '
  for i in range(0, len(transicao)):
    if transicao[i] == ',':
      num_virg += 1
    if num_virg >=2 and transicao[i] != ',' and transicao[i] != ' ':
      est_atual = est_atual + transicao[i]
  return est_atual 
def testar_alf(palavra, alfabeto):
  cont = teste = 0
  for i in range(0, len(palavra)):
    for j in range(0, len(alfabeto)):
      if palavra[i] == alfabeto[j]:
        cont += 1
    if cont > 0:
      teste += 0
    else:
      teste += 1
    cont = 0
  return teste
def testar_transicoes(palavra, afd, estado_atual):
  est = ' '
  k = ctrl = 0
  print('\nTransições:\n')
  for i in range(0, len(palavra)):
    for j in range(1, len(afd)):
      while afd[j][k] != ',':
        est = est + afd[j][k]
        k += 1
      k = 0
      if estado_atual.strip() in est.strip() and ctrl == 0:
        if ' '+palavra[i] in afd[j]:
          print(afd[j])
          estado_atual = testar_estado_atual(estado_atual, afd[j])
          ctrl += 1
      est = ' '
    ctrl = 0
  return estado_atual.strip()