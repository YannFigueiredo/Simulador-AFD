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
print(f'Estado inicial:{estado_inicial}')
print(f'Estado(s) final(is): {estados_finais}')
while True:
  print('')
  print('\033[0;33m-=-\033[m'*20)
  print(f'{programa:^60}')
  print('\033[0;33m-=-\033[m'*20)
  palavra = str(input('Informe a palavra: '))
  #Aqui vai as checagens para ver se a palavra é aceita
  op = str(input('Informe se deseja testar outra palavra(S/N): ')).strip().upper()
  if op == 'N':
    print('\nPrograma encerrado...')
    break