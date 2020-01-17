<div tabindex="-1" id="notebook" class="border-box-sizing">

<div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

# Introdução à Inteligência Artificial - PEE / 2 - Formulação[¶](#Introdução-à-Inteligência-Artificial---PEE-/-2---Formulação)

# Guião Laboratorial[¶](#Guião-Laboratorial)

(7/Out:11/Out-2019)

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

## Revisão[¶](#Revisão)

Vamos formular mais um problema através do Paradigma do Espaço de Estados, usando o Python e a ferramanta [aima-python].

Note que formular neste caso, quer dizer construir uma programa em Python.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Recordando, para formularmos um problema de acordo com esta metododologia, precisamos de:

*   **Estados**: Idealizar uma representação para o que vamos considerar um estado. Notem que o estado deve ser mínimo, apenas deve conter a informação que muda com as acções;
*   **Estado Inicial**: Identificar o estado inicial;
*   **Objectivo**: Verificar se um estado satisfaz o objectivo, sendo assim, um dos estados finais;
*   **Acções**: Para cada estado, caracterizar rigorosamente as acções de mudança de estado, de que modo incrementam os custos dos caminhos, e quais os estados resultantes.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

## Recursos necessários[¶](#Recursos-necessários)

*   Para executar as experiências que se seguem, copie o módulo [searchPlus.py](searchPlus.py) para a directoria de trabalho.
*   Copie para o mesmo local os outros módulos auxiliares necessários: [utils.py](utils.py)
*   Crie um novo modulo **pee2.py** para ir realizando as experiências sugeridas ou então pode usar a versão notebook deste ficheiro.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="kn">from</span> <span class="nn">searchPlus</span> <span class="k">import</span> <span class="o">*</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

### O problema dos Jarros[¶](#O-problema-dos-Jarros)

Recordando o enunciado: Imagine que tem dois jarros com capacidade para 3 e 5 litros. Pretende-se medir 4 litros de vinho, usando as seguintes operações: encher um jarro, esvaziar um jarro, ou verter vinho de um jarro para outro.

![figura](water22.png)

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Representação dos estados[¶](#Representação-dos-estados)

Podemos definir um tuplo com o líquido em cada um dos jarros. É essa a informação que muda com as acções. A capacidade dos jarros deve ficar no problema, e informação estática. O tuplo que colcaremos no problema referente às capacidades dos jarros tem de respeitar a mesma ordem do estado.

Na verdade, podemos avançar já para a definição da classe do Problema, fazendo notar que podemos ter mais do que 2 jarros.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="k">class</span> <span class="nc">ProblemaJarros</span><span class="p">(</span><span class="n">Problem</span><span class="p">):</span>
    <span class="sd">"""Problem about pouring water between jugs to achieve some water level.</span>
 <span class="sd">Each state is a tuples of water levels. In the initialization, also provide a tuple of</span>
 <span class="sd">jug sizes, e.g. PourProblem(initial=(0, 0), goal=4, sizes=(5, 3)),</span>
 <span class="sd">which means two jugs of sizes 5 and 3, initially both empty, with the goal</span>
 <span class="sd">of getting a level of 4 in either jug."""</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">initial</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">),</span><span class="n">goal</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span><span class="n">capacidades</span><span class="o">=</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">5</span><span class="p">)):</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">initial</span><span class="p">,</span><span class="n">goal</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">capacidades</span> <span class="o">=</span> <span class="n">capacidades</span>

    <span class="k">def</span> <span class="nf">actions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">estado</span><span class="p">):</span>
        <span class="sd">"""As acções executáveis neste estado."""</span>
        <span class="n">jarros</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">estado</span><span class="p">))</span>
        <span class="k">return</span> <span class="p">([(</span><span class="s1">'Enche'</span><span class="p">,</span> <span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span>    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">jarros</span> <span class="k">if</span> <span class="n">estado</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o"><</span> <span class="bp">self</span><span class="o">.</span><span class="n">capacidades</span><span class="p">[</span><span class="n">i</span><span class="p">]]</span> <span class="o">+</span>
                <span class="p">[(</span><span class="s1">'Esvazia'</span><span class="p">,</span> <span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span>    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">jarros</span> <span class="k">if</span> <span class="n">estado</span><span class="p">[</span><span class="n">i</span><span class="p">]]</span> <span class="o">+</span>
                <span class="p">[(</span><span class="s1">'Verte'</span><span class="p">,</span> <span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span> <span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">jarros</span> <span class="k">if</span> <span class="n">estado</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="n">jarros</span> <span class="k">if</span> <span class="n">i</span> <span class="o">!=</span> <span class="n">j</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">estado</span><span class="p">,</span> <span class="n">accao</span><span class="p">):</span>
        <span class="sd">"""O estado sofre accao e passa a ser:."""</span>
        <span class="n">resultado</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">estado</span><span class="p">)</span>  <span class="c1"># converte tuplo em lista</span>
        <span class="n">a</span><span class="p">,</span> <span class="n">i</span><span class="p">,</span> <span class="o">*</span><span class="n">_</span> <span class="o">=</span> <span class="n">accao</span>
        <span class="n">i</span> <span class="o">=</span> <span class="n">i</span><span class="o">-</span><span class="mi">1</span>  <span class="c1"># O jarro i correspoinde à posição i - 1</span>
        <span class="k">if</span> <span class="n">a</span> <span class="o">==</span> <span class="s1">'Enche'</span><span class="p">:</span>   <span class="c1"># Enche jarro i até capacidade</span>
            <span class="n">resultado</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">capacidades</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
        <span class="k">elif</span> <span class="n">a</span> <span class="o">==</span> <span class="s1">'Esvazia'</span><span class="p">:</span> <span class="c1"># Esvazia i</span>
            <span class="n">resultado</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">elif</span> <span class="n">a</span> <span class="o">==</span> <span class="s1">'Verte'</span><span class="p">:</span> <span class="c1"># Verte i em j</span>
            <span class="n">j</span> <span class="o">=</span> <span class="n">accao</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">-</span><span class="mi">1</span>  <span class="c1"># o jarro j corresponde à posição j - 1</span>
            <span class="n">quantidade</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">estado</span><span class="p">[</span><span class="n">i</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">capacidades</span><span class="p">[</span><span class="n">j</span><span class="p">]</span> <span class="o">-</span> <span class="n">estado</span><span class="p">[</span><span class="n">j</span><span class="p">])</span>
            <span class="n">resultado</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">-=</span> <span class="n">quantidade</span>
            <span class="n">resultado</span><span class="p">[</span><span class="n">j</span><span class="p">]</span> <span class="o">+=</span> <span class="n">quantidade</span>
        <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">resultado</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">is_goal</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">estado</span><span class="p">):</span>
        <span class="sd">"""True if the goal level is in any one of the jugs."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">goal</span> <span class="ow">in</span> <span class="n">estado</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos criar um problema

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">p</span> <span class="o">=</span> <span class="n">ProblemaJarros</span><span class="p">()</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos agora criar uma instância deste problema, imprimir o estado inicial e perguntar quantos litros desejamos medir.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">prob_jarros</span> <span class="o">=</span> <span class="n">ProblemaJarros</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Estado Inicial:"</span><span class="p">,</span><span class="n">prob_jarros</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">'Capacidades dos jarros:'</span><span class="p">,</span><span class="n">prob_jarros</span><span class="o">.</span><span class="n">capacidades</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"O objectivo é medir "</span><span class="p">,</span><span class="n">prob_jarros</span><span class="o">.</span><span class="n">goal</span><span class="p">,</span> <span class="s2">"litros"</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos verificar quais são as acções que podemos aplicar ao estado inicial

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">prob_jarros</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">prob_jarros</span><span class="o">.</span><span class="n">initial</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos encher o jarro 2 (a primeira acção) e obter um novo estado...

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">e1</span> <span class="o">=</span> <span class="n">prob_jarros</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">prob_jarros</span><span class="o">.</span><span class="n">initial</span><span class="p">,(</span><span class="s1">'Enche'</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">e1</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">prob_jarros</span><span class="o">.</span><span class="n">actions</span><span class="p">(</span><span class="n">e1</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos verter o segundo jarro no primeiro...

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">e2</span> <span class="o">=</span> <span class="n">prob_jarros</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">e1</span><span class="p">,(</span><span class="s1">'Verte'</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">e2</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

Vamos agora reencher o 1º jarro

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">e3</span> <span class="o">=</span> <span class="n">prob_jarros</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">e2</span><span class="p">,(</span><span class="s1">'Enche'</span><span class="p">,</span><span class="mi">1</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">e3</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

Vamos testar a função **_path_cost_** que é herdada de **Problem**. Notem que essa função recebe 4 argumentos: o custo actual, o estado, a acção e o novo estado e devolve o novo custo acumulado: custo actual + o custo da transição entre estados, neste caso 1. Começamos com 0 no estado inicial.

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">In [ ]:</div>

<div class="inner_cell">

<div class="input_area">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">custo</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">e0</span> <span class="o">=</span> <span class="n">prob_jarros</span><span class="o">.</span><span class="n">initial</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Comecemos:"</span><span class="p">,</span><span class="n">e0</span><span class="p">,</span><span class="s2">", com custo ="</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
<span class="n">e1</span> <span class="o">=</span> <span class="n">prob_jarros</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">e0</span><span class="p">,(</span><span class="s1">'Enche'</span><span class="p">,</span><span class="mi">2</span><span class="p">))</span>
<span class="n">custo</span> <span class="o">=</span> <span class="n">prob_jarros</span><span class="o">.</span><span class="n">path_cost</span><span class="p">(</span><span class="n">custo</span><span class="p">,</span><span class="n">prob_jarros</span><span class="o">.</span><span class="n">initial</span><span class="p">,(</span><span class="s1">'Enche'</span><span class="p">,</span><span class="mi">2</span><span class="p">),</span><span class="n">e1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Vamos encher o segundo jarro:"</span><span class="p">,</span><span class="n">e1</span><span class="p">,</span> <span class="s2">", com custo ="</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
<span class="n">e2</span> <span class="o">=</span> <span class="n">prob_jarros</span><span class="o">.</span><span class="n">result</span><span class="p">(</span><span class="n">e1</span><span class="p">,(</span><span class="s1">'Verte'</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">1</span><span class="p">))</span>
<span class="n">custo</span> <span class="o">=</span> <span class="n">prob_jarros</span><span class="o">.</span><span class="n">path_cost</span><span class="p">(</span><span class="n">custo</span><span class="p">,</span><span class="n">prob_jarros</span><span class="o">.</span><span class="n">initial</span><span class="p">,(</span><span class="s1">'Verte'</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span><span class="n">e1</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Vamos verter o jarro 2 em jarro 1:"</span><span class="p">,</span><span class="n">e2</span><span class="p">,</span> <span class="s2">", com custo ="</span><span class="p">,</span><span class="n">custo</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Exercício1[¶](#Exercício1)

Experimente resolver outras instâncias deste problema. Por exemplo:

*   Como medir 3 litros com recipientes de 7 e 5
*   Como medir 6 litros com recipientes de 7, 8 e 3

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Exercício 2[¶](#Exercício-2)

Crie uma função **_exec()_** que pegue num estado e execute uma sequência de acções numa lista, devolvendo o estado resultante.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Exercício 3[¶](#Exercício-3)

Reformule o problema dos jarros, a versão verde, de modo a que o custo das acções deixe de ser unitário. Queremos calcular a água gasta da torneira até à medição desejada - enchem-se os jarros da torneira. Assim, apenas tem custo a acção de encher e o custo corresponde à água gasta.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Exercício 4[¶](#Exercício-4)

Complete a formulação esboçada a seguir do problema do puzzle de 8.

![](https://ece.uwaterloo.ca/~dwharder/aads/Algorithms/N_puzzles/images/puz3.png)

Estamos perante o problema clássico de um puzzle de peças deslizantes onde se pode deslocar qualquer peça ortogonalmente para a casa vazia. Partimos de uma configuração inicial (por exemplo, o puzzle da esquerda da figura) e queremos atingir a configuração objectivo (puzzle da direita).

<div class="highlight">

<pre><span></span><span class="k">class</span> <span class="nc">PuzzleN</span><span class="p">(</span><span class="n">Problem</span><span class="p">):</span>
    <span class="sd">""" O problema das N=dxd-1 peças deslizantes, num tabuleiro quadrado de dimensão dxd</span>
 <span class="sd">onde um dos quadrados está vazio, tentando atingir uma configuração particular</span>
 <span class="sd">Um estado é representado por um tuplo de dimensão dxd.</span>
 <span class="sd">As peças são representadas pelos próprios números e a peça vazia por 0.</span>
 <span class="sd">O objectivo por omissão no caso de 3x3:</span>
 <span class="sd">1 2 3</span>
 <span class="sd">4 5 6 ==> (1, 2, 3, 4, 5, 6, 7, 8, 0)</span>
 <span class="sd">7 8 _</span>
 <span class="sd">Existe um atributo d que representa a dimensão do quadrado, 3 no caso do puzzle de 8</span>
 <span class="sd">"""</span>

    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">initial</span><span class="p">,</span> <span class="n">goal</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">8</span><span class="p">)):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">initial</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">goal</span> <span class="o">=</span> <span class="n">initial</span><span class="p">,</span> <span class="n">goal</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">d</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">initial</span><span class="p">)))</span>

    <span class="k">def</span> <span class="nf">display</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="sd">""" print the state please"""</span>
        <span class="n">output</span><span class="o">=</span><span class="s2">""</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">d</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">d</span><span class="p">):</span>
            <span class="n">ch</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">state</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
            <span class="k">if</span> <span class="n">ch</span> <span class="o">==</span> <span class="s2">"0"</span><span class="p">:</span>
                <span class="n">ch</span> <span class="o">=</span> <span class="s1">'_'</span>
            <span class="n">output</span> <span class="o">+=</span> <span class="n">ch</span> <span class="o">+</span> <span class="s2">" "</span>
            <span class="n">i</span> <span class="o">=</span> <span class="n">i</span><span class="o">+</span><span class="mi">1</span>
            <span class="k">if</span> <span class="n">i</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">d</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">output</span> <span class="o">+=</span> <span class="s2">"</span><span class="se">\n</span><span class="s2">"</span>
        <span class="k">print</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

#### Exercício 5[¶](#Exercício-5)

Formule o problema das latas (nº 22 da [folha de exercícios de formulação](1819IIA_Exercicios_PEE_formulacao.pdf) ).

Temos uma colecção de N objectos de tamanhos S1, … , SN. Queremos colocar estes objectos em latas de capacidade B e queremos usar o menor número de latas possível. Por exemplo, suponha que temos:  
– B=100  
– 4 objectos com os tamanhos seguintes:  
S1=45, S2=80, S3=30 e S4=15.  
Então é possível colocar estes 4 objectos em duas latas, colocando por exemplo os objectos 1, 3 e 4 numa das latas e o objecto 2 noutra. Uma solução alternativa consiste em empacotar os objectos 1 e 3 numa das latas e os objectos 2 e 4 noutra.

</div>

</div>

</div>

</div>

</div>
