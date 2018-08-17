<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="estilo.css"/>
</head>
<body>
<b>SIMULADOR-AFD</b>

<i>Características{</i><br/>
                <i>*Escrito na linguagem Python.</i><br/>
                <i>*Atualizado em 17/08/2018.</i><br/>
                <i>*Autor: Yann Figueiredo.</i><br/>
                <i>}</i><br/>

<i>Esse programa registra um Autômato Finito Determinístico através de um arquivo.txt e testa se uma palavra, informada pelo usuário, é aceita pelo AFD registrado.</i>

<i>O arquivo.txt que descreverá o AFD terá a seguinte forma geral descrita abaixo. Na primeira linha serão apresentados os componentes do AFD, conforme abaixo:</i><br/>
<i>(∑︀, Q, 𝛿, q0, F)</i><br/>
<i>∑︀ = Alfabeto do AFD</i><br/>
<i>Q = Estados do AFD</i><br/>
<i>𝛿 = Regras de transição do AFD</i><br/>
<i>q0 = Estado inicial do AFD</i><br/>
<i>F = Estado(s) final(is) do AFD</i><br/>
<br/>
<i>Os componentes serão apresentados como conjuntos. Um exemplo da primeira linha do
arquivo seria:</i><br/>
<i>({a, b}, {q0, q1, q2, qf}, D, q0, {qf})</i><br/>

<i>A partir da segunda linha, estarão listadas as regras de transição segundo o esquema:</i><br/>
<i>estado_origem, símbolo_lido, estado final</i><br/>
<i>Por exemplo:</i><br/>
<i>q0, a, q1</i><br/>
<i>q1, a, qf</i><br/>
<i>q0, b, q2</i><br/>
<i>q1, b, q2</i><br/>

<i>***Restrições***</i><br/>
<i>-O AFD só deve ter estados que possuem a letra 'q' como inicial.<br/>
-O arquivo.txt deve ser informado sem a extensão(.txt) quando solicitado pelo programa.<br/>
-O arquivo.txt deve seguir estritamente o modelo informado acima(inclusive os espaços).</i>
</body>
</html>
