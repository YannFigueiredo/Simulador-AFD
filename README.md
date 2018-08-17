<b>SIMULADOR-AFD</b>

<i>Características{</i>
                <i>*Escrito na linguagem Python.</i>
                <i>*Atualizado em 17/08/2018.</i>
                <i>*Autor: Yann Figueiredo.</i>
                <i>}</i>

<i>Esse programa registra um Autômato Finito Determinístico através de um arquivo.txt e testa se uma palavra, informada pelo usuário, é aceita pelo AFD registrado.</i>

<i>O arquivo.txt que descreverá o AFD terá a seguinte forma geral descrita abaixo. Na primeira linha serão apresentados os componentes do AFD, conforme abaixo:</i>
<i>(∑︀, Q, 𝛿, q0, F)</i>
<i>∑︀ = Alfabeto do AFD</i>
<i>Q = Estados do AFD</i>
<i>𝛿 = Regras de transição do AFD</i>
<i>q0 = Estado inicial do AFD</i>
<i>F = Estado(s) final(is) do AFD</i>

<i>Os componentes serão apresentados como conjuntos. Um exemplo da primeira linha do
arquivo seria:</i>
<i>({a, b}, {q0, q1, q2, qf}, D, q0, {qf})</i>

<i>A partir da segunda linha, estarão listadas as regras de transição segundo o esquema:
<i>estado_origem, símbolo_lido, estado final</i>
<i>Por exemplo:</i>
<i>q0, a, q1</i>
<i>q1, a, qf</i>
<i>q0, b, q2</i>
<i>q1, b, q2</i>

<i>***Restrições***</i>
<i>-O AFD só deve ter estados que possuem a letra 'q' como inicial.</i>
<i>-O arquivo.txt deve ser informado sem a extensão(.txt) quando solicitado pelo programa.</i>
<i>-O arquivo.txt deve seguir estritamente o modelo informado acima(inclusive os espaços).</i>

