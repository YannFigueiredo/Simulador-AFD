# Simulador-AFD
Características{
                *Escrito na linguagem Python.
                *Atualizado em 17/08/2018.
                *Autor: Yann Figueiredo.
                }

Esse programa registra um Autômato Finito Determinístico através de um arquivo.txt e testa se uma palavra, informada pelo usuário, é aceita pelo AFD registrado.

O arquivo.txt que descreverá o AFD terá a seguinte forma geral descrita abaixo. Na primeira linha serão apresentados os componentes do AFD, conforme abaixo:
(∑︀, Q, 𝛿, q0, F)
∑︀ = Alfabeto do AFD
Q = Estados do AFD
𝛿 = Regras de transição do AFD
q0 = Estado inicial do AFD
F = Estado(s) final(is) do AFD

Os componentes serão apresentados como conjuntos. Um exemplo da primeira linha do
arquivo seria:
({a, b}, {q0, q1, q2, qf}, D, q0, {qf})

A partir da segunda linha, estarão listadas as regras de transição segundo o esquema:
estado_origem, símbolo_lido, estado final
Por exemplo:
q0, a, q1
q1, a, qf
q0, b, q2
q1, b, q2

***Restrições***
-O AFD só deve ter estados que possuem a letra 'q' como inicial.
-O arquivo.txt deve ser informado sem a extensão(.txt) quando solicitado pelo programa.
-O arquivo.txt deve seguir estritamente o modelo informado acima(inclusive os espaços).

