<b>SIMULADOR-AFD</b>

<i>Características{<br/>
                *Escrito na linguagem Python.<br/>
                *GUI: Não.<br/>
                *Atualizado em 19/08/2018.<br/>
                *Autor: Yann Figueiredo.<br/>
                }<br/>

Esse programa registra um Autômato Finito Determinístico através de um arquivo.txt e testa se uma palavra, informada pelo usuário, é aceita pelo AFD registrado.

O arquivo.txt que descreverá o AFD terá a seguinte forma geral descrita abaixo. Na primeira linha serão apresentados os componentes do AFD, conforme abaixo:<br/>
(∑︀, Q, 𝛿, q0, F)<br/>
∑︀ = Alfabeto do AFD<br/>
Q = Estados do AFD<br/>
𝛿 = Regras de transição do AFD<br/>
q0 = Estado inicial do AFD<br/>
F = Estado(s) final(is) do AFD<br/>
<br/>
Os componentes serão apresentados como conjuntos. Um exemplo da primeira linha do
arquivo seria:<br/>
({a, b}, {q0, q1, q2, qf}, D, q0, {qf})<br/>

A partir da segunda linha, estarão listadas as regras de transição segundo o esquema:<br/>
estado_origem, símbolo_lido, estado final<br/>
Por exemplo:<br/>
q0, a, q1<br/>
q1, a, qf<br/>
q0, b, q2<br/>
q1, b, q2<br/>

***Restrições***<br/>
-O arquivo.txt deve ser informado sem a extensão(.txt) quando solicitado pelo programa.<br/>
-O arquivo.txt deve seguir estritamente o modelo informado acima(inclusive os espaços).</i>
