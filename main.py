import registro
import checagem
programa = 'SIMULADOR AFD'
print('\033[0;33m-=-\033[m'*20)
print(f'{programa:^60}')
print('\033[0;33m-=-\033[m'*20)
afd = registro.leitura_afd()
alfabeto = registro.separar_alf(afd[0])
estados = registro.separar_estados(afd[0])
estado_inicial = registro.separar_est_inicial(afd[0])
estados_finais = registro.separar_est_final(afd[0])
print(f'\nAlfabeto: {alfabeto}')
print(f'Estados: {estados}')
print(f'Estado inicial: {estado_inicial}')
print(f'Estado(s) final(is): {estados_finais}')
while True:
  print('')
  print('\033[0;33m-=-\033[m'*20)
  print(f'{programa:^60}')
  print('\033[0;33m-=-\033[m'*20)
  palavra = str(input('Informe a palavra: ')).strip()
  teste = checagem.testar_alf(palavra, alfabeto)
  if teste == 0:
    n_est_final = checagem.testar_transicoes(palavra, afd, estado_inicial)
    teste = checagem.testar_estado_final(n_est_final, estados_finais)
    if teste == 1:
      print('\n\033[4;32mPALAVRA ACEITA!\033[m')
    else:
      print('\n\033[4;31mPALAVRA RECUSADA!\033[m')
  else:
    print('\n\033[1;31;40mA palavra contém símbolo(s) não aceito(s) pelo alfabeto do AFD cadastrado.\033[m')
  op = str(input('\nInforme se deseja testar outra palavra(S/N): ')).strip().upper()
  if op == 'N':
    print('\nPrograma encerrado...')
    break