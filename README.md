<h1 id="supplyflow">SupplyFlow</h1>

<p>
  O <strong>SupplyFlow</strong> é uma solução criada para melhorar o controle de estoque da <strong>Dasa</strong>,
  melhorando ao máximo seu histórico de consumo, com uma consulta rápida de insumos e listas sempre ordenadas para navegação.<br>
</p>

<h2 id="funcionalidades">🔧 Funcionalidades</h2>
<ul>
  <li>📜 Histórico de consumo cronológico via <em>Fila</em></li>
  <li>🔁 Histórico inverso via <em>Pilha</em></li>
  <li>🔎 Busca Sequencial Recursiva para localizar insumos</li>
  <li>⚡ Busca Binária (em lista ordenada) para respostas rápidas</li>
  <li>🧩 Merge Sort para ordenação estável e previsível</li>
  <li>⚡ Quick Sort para ordenação <em>in-place</em> com ótima performance média</li>
  <li>🧾 Exibição do consumo em ordem cronológica e inversa</li>
</ul>

<h2 id="como-funciona">🧠 Como funciona (estruturas e algoritmos)</h2>

<ol>
  <li>
    <h3>Fila (Queue) — consumo cronológico ⏩</h3>
    <ul>
      <li>Implementada como lista Python: <code>fila_consumo</code></li>
      <li>Cada retirada registra um evento: <code>_registrar_consumo(nome, quantidade, timestamp)</code></li>
      <li>Exibição FIFO: <code>exibir_consumo_cronologico()</code> percorre do início ao fim</li>
    </ul>
  </li>

  <li>
    <h3>Pilha (Stack) — últimos eventos primeiro 🔙</h3>
    <ul>
      <li>Implementada como lista Python: <code>pilha_consumo</code></li>
      <li>Mesmo evento também vai para a pilha (LIFO)</li>
      <li>Exibição LIFO: <code>exibir_consumo_inverso()</code> percorre de trás pra frente</li>
    </ul>
  </li>

  <li>
    <h3>Busca Sequencial Recursiva 🧭</h3>
    <pre><code>busca_sequencial_recursiva(lista, elemento, indice=0)</code></pre>
    <ul>
      <li>Compara elemento por elemento de forma recursiva</li>
      <li>Retorna <code>True/False</code> e é usada em <code>self.lista_insumos</code></li>
    </ul>
  </li>

  <li>
    <h3>Busca Binária 🎯</h3>
    <pre><code>busca_binaria(lista, alvo)  # em lista previamente ordenada</code></pre>
    <ul>
      <li>Usa <code>inicio</code>, <code>fim</code> e <code>meio</code> com <code>lower()</code> para ignorar caixa</li>
      <li>Exige <code>self.lista_insumos</code> sempre ordenada</li>
    </ul>
  </li>

  <li>
    <h3>Merge Sort 🧩</h3>
    <pre><code>merge_sort(lista)  # divide e conquista
_merge(esq, dir)   # intercala sublistas</code></pre>
    <ul>
      <li>Retorna nova lista ordenada alfabeticamente</li>
    </ul>
  </li>

  <li>
    <h3>Quick Sort ⚡</h3>
    <pre><code>quick_sort(lista)  # in-place com pivô aleatório</code></pre>
    <ul>
      <li>Particiona menores à esquerda e maiores à direita</li>
      <li>Retorna a mesma lista, agora ordenada</li>
    </ul>
  </li>
</ol>

<h2 id="integracao">💡 Integração no projeto</h2>
<ul>
  <li>Fila e Pilha mantêm o histórico de consumo sob duas perspectivas (cronológica e inversa).</li>
  <li>Buscas permitem localizar insumos rapidamente.</li>
  <li>Ordenações garantem a eficácia e consistência da busca binária e melhoram a exibição.</li>
</ul>