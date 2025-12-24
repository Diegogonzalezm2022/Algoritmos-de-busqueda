# Algoritmos de búsqueda

En este proyecto se pretende implementar y comparar múltiples algoritmos de búsqueda. Para ello partimos de un código base previamente proporcionado, sobre el cuál implementamos los algoritmos añadidos y la recolección de datos sobre su rendimiento. Para aplicar los algoritmos, seleccionamos dos nodos en el mapa de Rumanía y aplicamos los algoritmos para buscar una ruta que los una.

## Apartado 1: Branch and bound

En este apartado implementamos el algoritmo de ramificación y acotación, en el que los nodos a expandir se seleccionan en función del coste del camino desde el nodo inicial al nodo seleccionado, expandiendo el nodo con un menor coste acumulado en cada iteración.

Para implementar el algoritmo, creamos una cola de prioridad (que hereda de la clase FIFOQueue implementada en el código base) para ordenar los nodos en función del coste que se incurre para llegar a estos. Para ello se incluye un nuevo atributo en la estructura, una "función de clave", cuyo resultado tras aplicarse sobre los elementos será el clave de ordenación. Este atributo se inicializa en la definición de la estructura de datos. Para mantener el orden de los elementos, estos se insertan en la estructura subyacente de manera que siempre se mantenga un orden de menor a mayor en esta. Para conseguir esto, primero comprobamos si la lista esta vacía o si el elemento es mayor al nodo que se encuantra al final de la cola (el elemento de mayor valor), en cuyo caso se inserta el nodo al final de la lista. Si esto no ocurre, se busca en la cola el primer elemento que es mayor o igual al nodo insertar, insertando el nodo delante de este. Debido al nuevo algoritmo de inserción, es necesario modificar la función extend, que ahora simplemente realiza tantas inserciones para como número de nodos pasados como argumentos. 
Para implementar la búsqueda, llamamos al método graph_search previamente implementado definiendo como fringe la estructura de datos creada anteriormente, siendo su función de clave el coste del camino entre el nodo inicial y el nodo argumento (que es un atributo incluido en el propio nodo).

Para mostrar el funcionamiento de este algoritmo, realizamos 6 iteraciones de la traza de la resolución del camino entre Oradea y Eforie en el mapa de Rumanía.

<table>
<tr><th>Actual</th><th>Lista abierta</th></tr>
<tr><td></td><td>{O1}</td></tr>
<tr><td>O1</td><td>{Z1/71, S1/151}</td></tr>
<tr><td>Z1</td><td>{A1/146, S1/151}</td></tr>
<tr><td>A1</td><td>{S1/151, T1/264, S2/286}</td></tr>
<tr><td>S1</td><td>{R1/231, F1/250, T1/264, S2/286}</td></tr>
<tr><td>R1</td><td>{F1/250, T1/264, S2/286, P1/328, C1/377}</td></tr>
</table>

## Apartado 2: Branch and bound con subestimación

En este apartado implementamos el algoritmo de ramificación y acotación, en el que los nodos a expandir se seleccionan en función de la suma del coste definido en el apartado anterior y una heurística de distancia que ofrece una aproximación del coste entre el nodo actual y el nodo destino. En este caso, la heurística es la distancia euclídea entre nodo actual y destino.

Para implementar este algoritmo, utilizamos la misma metodología que en el apartado anterior que en el apartado anterior, cambiando la función de clave en el método de busqueda de manera que esta sea la resultante de sumar el coste del nodo al valor heurístico de este.

Para que el algoritmo de ramificación y acotación con subestimación alcance una solución óptima, es necesario que la heurística sea una subestimación del coste real del camino elegido, ya que una heurística sobreestimada permite que los caminos con menor coste real se visiten más tarde con un camino de mayor coste que se encuentra heurísticamente más cerca de la solución. Para ejemplificar esto, realizamos una prueba con una heurística sobreestimada (distancia euclídea multiplicada por 10):
<table>
<tr><th>Origen</th><th>Destino</th><th>Ramificación y acotación con subestimación</th><th>Ramificación y acotación con sobreestimación</th></tr>
<tr><td>Arad</td><td>Bucharest</td><td>
<p>Generados:  16</p>

<p>Visitados:  6</p>

<p>Costo total:  418</p>

<p>Ruta:  [&lt;Node B&gt;, &lt;Node P&gt;, &lt;Node R&gt;, &lt;Node S&gt;, &lt;Node A&gt;]</p>

<p>Tiempo transcurrido: 169.99 µs</p>
</td><td>
<p>Generados:  10</p>
<p>Visitados:  4</p>
<p>Costo total:  450</p>
<p>Ruta:  [&lt;Node B&gt;, &lt;Node F&gt;, &lt;Node S&gt;, &lt;Node A&gt;]</p>
<p>Tiempo transcurrido: 263.93 µs</p>
</td></tr>
</table>

Se observa que el camino hallado ya no es el óptimo, demostrando que sobreestimar la heurística en el algoritmo conlleva la perdida de la optimalidad de este.

## Apartado 3: Estudio de resultados de los algoritmos

Para comparar los distintos algoritmos, los aplicamos al problema de búsqueda de caminos entre dos nodos en un mapa, contabilizando nodos generados y visitados, el tiempo de ejecución, además de la solución hallada y el coste de esta.

Para estudiar el rendimiento de los distintos algoritmos implementados se modifica el código de la función graph search para contabilizar los distintos datos explicados anteriormente. Esta información se recoge para cinco búsquedas distintas, en la que se comparan los cuatro algoritmos implementados (no se incluye el branch and bound con sobreestimación realizado en el apartado anterior, ya que este solo se ha creado con motivo de demostrar que este algoritmo no encuentra la ruta óptima). Los resultados de esta prueba se incluyen a continuación:

<table border="0" cellspacing="0" cellpadding="0" class="table-ta1"><colgroup><col width="72"/><col width="72"/><col width="72"/><col width="228"/><col width="236"/><col width="230"/><col width="222"/><col width="72"/></colgroup><tr class="row-ro1"><th style="text-align:left;width:1.655cm; " class="cell-ce1">
<p>ID</p>
</th><th style="text-align:left;width:1.655cm; " class="cell-ce5">
<p>Origen</p>
</th><th style="text-align:left;width:1.655cm; " class="cell-ce5">
<p>Destino</p>
</th><th style="text-align:left;width:5.219cm; " class="cell-ce5">
<p>Amplitud</p>
</th><th style="text-align:left;width:5.398cm; " class="cell-ce5">
<p>Profundidad</p>
</th><th style="text-align:left;width:5.255cm; " class="cell-ce1">
<p>Ramificación y Acotación </p>
</th><th style="text-align:left;width:5.076cm; " class="cell-ce5">
<p>Ramificación y acotación con subestimación </p>
</th></td></tr><tr class="row-ro2"><td style="text-align:right; width:1.655cm; " class="cell-ce2">
<p>1</p>
</td><td style="text-align:left;width:1.655cm; " class="cell-ce6">
<p>Arad</p>
</td><td style="text-align:left;width:1.655cm; " class="cell-ce6">
<p>Bucharest</p>
</td><td style="text-align:left;width:5.219cm; " class="cell-ce6">
<p>Generados:  21</p>

<p>Visitados:  16</p>

<p>Costo total:  450</p>

<p>Ruta:  [&lt;Node B&gt;, &lt;Node F&gt;, &lt;Node S&gt;, &lt;Node A&gt;]</p>

<p>Tiempo transcurrido: 130.41 µs</p>
</td><td style="text-align:left;width:5.398cm; " class="cell-ce6">
<p>Generados:  18</p>

<p>Visitados:  10</p>

<p>Costo total:  733</p>

<p>Ruta:  [&lt;Node B&gt;, &lt;Node P&gt;, &lt;Node C&gt;, &lt;Node D&gt;, &lt;Node M&gt;, &lt;Node L&gt;, &lt;Node T&gt;, &lt;Node A&gt;]</p>

<p>Tiempo transcurrido: 64.85 µs</p>
</td><td style="text-align:left;width:5.255cm; " class="cell-ce6">
<p>Generados:  31</p>

<p>Visitados:  24</p>

<p>Costo total:  418</p>

<p>Ruta:  [&lt;Node B&gt;, &lt;Node P&gt;, &lt;Node R&gt;, &lt;Node S&gt;, &lt;Node A&gt;]</p>

<p>Tiempo transcurrido: 210.52 µs</p>
</td><td style="text-align:left;width:5.076cm; " class="cell-ce6">
<p>Generados:  16</p>

<p>Visitados:  6</p>

<p>Costo total:  418</p>

<p>Ruta:  [&lt;Node B&gt;, &lt;Node P&gt;, &lt;Node R&gt;, &lt;Node S&gt;, &lt;Node A&gt;]</p>

<p>Tiempo transcurrido: 169.99 µs</p>
</td></tr><tr class="row-ro3"><td style="text-align:right; width:1.655cm; " class="cell-ce2">
<p>2</p>
</td><td style="text-align:left;width:1.655cm; " class="cell-ce6">
<p>Oradea</p>
</td><td style="text-align:left;width:1.655cm; " class="cell-ce6">
<p>Eforie</p>
</td><td style="text-align:left;width:5.219cm; " class="cell-ce6">
<p>Generados:  45</p>

<p>Visitados:  43</p>

<p>Costo total:  730</p>

<p>Ruta:  [&lt;Node E&gt;, &lt;Node H&gt;, &lt;Node U&gt;, &lt;Node B&gt;, &lt;Node F&gt;, &lt;Node S&gt;, &lt;Node O&gt;]</p>

<p>Tiempo transcurrido: 147.58 µs</p>
</td><td style="text-align:left;width:5.398cm; " class="cell-ce6">
<p>Generados:  41</p>

<p>Visitados:  31</p>

<p>Costo total:  698</p>

<p>Ruta:  [&lt;Node E&gt;, &lt;Node H&gt;, &lt;Node U&gt;, &lt;Node B&gt;, &lt;Node P&gt;, &lt;Node R&gt;, &lt;Node S&gt;, &lt;Node O&gt;]</p>

<p>Tiempo transcurrido: 104.90 µs</p>
</td><td style="text-align:left;width:5.255cm; " class="cell-ce6">
<p>Generados:  43</p>

<p>Visitados:  40</p>

<p>Costo total:  698</p>

<p>Ruta:  [&lt;Node E&gt;, &lt;Node H&gt;, &lt;Node U&gt;, &lt;Node B&gt;, &lt;Node P&gt;, &lt;Node R&gt;, &lt;Node S&gt;, &lt;Node O&gt;]</p>

<p>Tiempo transcurrido: 300.88 µs</p>
</td><td style="text-align:left;width:5.076cm; " class="cell-ce6">
<p>Generados:  32</p>

<p>Visitados:  15</p>

<p>Costo total:  698</p>

<p>Ruta:  [&lt;Node E&gt;, &lt;Node H&gt;, &lt;Node U&gt;, &lt;Node B&gt;, &lt;Node P&gt;, &lt;Node R&gt;, &lt;Node S&gt;, &lt;Node O&gt;]</p>

<p>Tiempo transcurrido: 412.94 µs</p>
</td></tr><tr class="row-ro4"><td style="text-align:right; width:1.655cm; " class="cell-ce2">
<p>3</p>
</td><td style="text-align:left;width:1.655cm; " class="cell-ce6">
<p>Giurgiu</p>
</td><td style="text-align:left;width:1.655cm; " class="cell-ce6">
<p>Zerind</p>
</td><td style="text-align:left;width:5.219cm; " class="cell-ce6">
<p>Generados:  41</p>

<p>Visitados:  34</p>

<p>Costo total:  615</p>

<p>Ruta:  [&lt;Node Z&gt;, &lt;Node A&gt;, &lt;Node S&gt;, &lt;Node F&gt;, &lt;Node B&gt;, &lt;Node G&gt;]  </p>

<p>Tiempo transcurrido: 153.78 µs</p>
</td><td style="text-align:left;width:5.398cm; " class="cell-ce6">
<p>Generados:  32</p>

<p>Visitados:  21</p>

<p>Costo total:  1284</p>

<p>Ruta:  [&lt;Node Z&gt;, &lt;Node A&gt;, &lt;Node T&gt;, &lt;Node L&gt;, &lt;Node M&gt;, &lt;Node D&gt;, &lt;Node C&gt;, &lt;Node P&gt;, &lt;Node R&gt;, &lt;Node S&gt;, &lt;Node F&gt;, &lt;Node B&gt;, &lt;Node G&gt;] </p>

<p>Tiempo transcurrido: 92.03 µs</p>
</td><td style="text-align:left;width:5.255cm; " class="cell-ce6">
<p>Generados:  41</p>

<p>Visitados:  35</p>

<p>Costo total:  583</p>

<p>Ruta:  [&lt;Node Z&gt;, &lt;Node A&gt;, &lt;Node S&gt;, &lt;Node R&gt;, &lt;Node P&gt;, &lt;Node B&gt;, &lt;Node G&gt;]</p>

<p>Tiempo transcurrido: 182.63 µs</p>
</td><td style="text-align:left;width:5.076cm; " class="cell-ce6">
<p>Generados:  26</p>

<p>Visitados:  12</p>

<p>Costo total:  583</p>

<p>Ruta:  [&lt;Node Z&gt;, &lt;Node A&gt;, &lt;Node S&gt;, &lt;Node R&gt;, &lt;Node P&gt;, &lt;Node B&gt;, &lt;Node G&gt;]</p>

<p>Tiempo transcurrido: 258.45 µs</p>
</td></tr><tr class="row-ro5"><td style="text-align:right; width:1.655cm; " class="cell-ce2">
<p>4</p>
</td><td style="text-align:left;width:1.655cm; " class="cell-ce6">
<p>Neamt</p>
</td><td style="text-align:left;width:1.655cm; " class="cell-ce6">
<p>Dobreta</p>
</td><td style="text-align:left;width:5.219cm; " class="cell-ce6">
<p>Generados:  32</p>

<p>Visitados:  26</p>

<p>Costo total:  765</p>

<p>Ruta:  [&lt;Node D&gt;, &lt;Node C&gt;, &lt;Node P&gt;, &lt;Node B&gt;, &lt;Node U&gt;, &lt;Node V&gt;, &lt;Node I&gt;, &lt;Node N&gt;]</p>

<p>Tiempo transcurrido: 118.02 µs</p>
</td><td style="text-align:left;width:5.398cm; " class="cell-ce6">
<p>Generados:  31</p>

<p>Visitados:  19</p>

<p>Costo total:  1151</p>

<p>Ruta:  [&lt;Node D&gt;, &lt;Node C&gt;, &lt;Node P&gt;, &lt;Node R&gt;, &lt;Node S&gt;, &lt;Node F&gt;, &lt;Node B&gt;, &lt;Node U&gt;, &lt;Node V&gt;, &lt;Node I&gt;, &lt;Node N&gt;]</p>

<p>Tiempo transcurrido: 96.32 µs</p>
</td><td style="text-align:left;width:5.255cm; " class="cell-ce6">
<p>Generados:  32</p>

<p>Visitados:  26</p>

<p>Costo total:  765</p>

<p>Ruta:  [&lt;Node D&gt;, &lt;Node C&gt;, &lt;Node P&gt;, &lt;Node B&gt;, &lt;Node U&gt;, &lt;Node V&gt;, &lt;Node I&gt;, &lt;Node N&gt;]</p>

<p>Tiempo transcurrido: 152.83 µs</p>
</td><td style="text-align:left;width:5.076cm; " class="cell-ce6">
<p>Generados:  23</p>

<p>Visitados:  12</p>

<p>Costo total:  765</p>

<p>Ruta:  [&lt;Node D&gt;, &lt;Node C&gt;, &lt;Node P&gt;, &lt;Node B&gt;, &lt;Node U&gt;, &lt;Node V&gt;, &lt;Node I&gt;, &lt;Node N&gt;]</p>

<p>Tiempo transcurrido: 208.62 µs</p>
</td></tr><tr class="row-ro5"><td style="text-align:right; width:1.655cm; " class="cell-ce2">
<p>5</p>
</td><td style="text-align:left;width:1.655cm; " class="cell-ce6">
<p>Mehadia</p>
</td><td style="text-align:left;width:1.655cm; " class="cell-ce6">
<p>Fagaras</p>
</td><td style="text-align:left;width:5.219cm; " class="cell-ce6">
<p>Generados:  31</p>

<p>Visitados:  23</p>

<p>Costo total:  520</p>

<p>Ruta:  [&lt;Node F&gt;, &lt;Node S&gt;, &lt;Node R&gt;, &lt;Node C&gt;, &lt;Node D&gt;, &lt;Node M&gt;]  </p>

<p>Tiempo transcurrido: 108.48 µs</p>
</td><td style="text-align:left;width:5.398cm; " class="cell-ce6">
<p>Generados:  29</p>

<p>Visitados:  18</p>

<p>Costo total:  928</p>

<p>Ruta:  [&lt;Node F&gt;, &lt;Node B&gt;, &lt;Node P&gt;, &lt;Node R&gt;, &lt;Node S&gt;, &lt;Node A&gt;, &lt;Node T&gt;, &lt;Node L&gt;, &lt;Node M&gt;]</p>

<p>Tiempo transcurrido: 82.02 µs</p>
</td><td style="text-align:left;width:5.255cm; " class="cell-ce6">
<p>Generados:  36</p>

<p>Visitados:  27</p>

<p>Costo total:  520</p>

<p>Ruta:  [&lt;Node F&gt;, &lt;Node S&gt;, &lt;Node R&gt;, &lt;Node C&gt;, &lt;Node D&gt;, &lt;Node M&gt;]  </p>

<p>Tiempo transcurrido: 167.85 µs</p>
</td><td style="text-align:left;width:5.076cm; " class="cell-ce6">
<p>Generados:  25</p>

<p>Visitados:  14</p>

<p>Costo total:  520</p>

<p>Ruta:  [&lt;Node F&gt;, &lt;Node S&gt;, &lt;Node R&gt;, &lt;Node C&gt;, &lt;Node D&gt;, &lt;Node M&gt;]  </p>

<p>Tiempo transcurrido: 196.70 µs</p>
</td></table>

Para tener una mejor perspectiva del rendimiento de los algoritmos, calculamos las medias de nodos generados, visitados y tiempo de ejecución (no realizamos media del coste de la solución ya que esta forma parte de la solución hallada y no es representativa del coste computacional del algoritmo).

<table>
<tr><th>Amplitud</th><th>Profundidad</th><th>Ramificación y acotación</th><th>Ramificación y acotación con subestimación</th> </tr>
<tr><td><p>Generados: 34</p>
<p>Visitados: 28.4</p>
<p>Tiempo transcurrido: 131.64 us</p> </td>
<td><p>Generados: 30.2</p>
<p>Visitados: 19.8</p>
<p>Tiempo transcurrido: 88.02 us</p> </td>
<td><p>Generados: 36.6</p>
<p>Visitados: 30.4</p>
<p>Tiempo transcurrido: 202.852 us</p></td>
<td><p>Generados: 24.4</p>
<p>Visitados: 11.8</p>
<p>Tiempo transcurrido: 249.54 us</p></td>
</tr>
</table>

Observamos que el algoritmo que encuentra una solución en el mínimo tiempo es el dfs, aunque cabe destacar que este algoritmo carece de optimalidad, por lo que no es útil si queremos encontrar la solución óptima. Además, si el mapa fuese de mayor tamaño, este algoritmo puede explorar completamente ramas lejanas a la solución, lo cual puede alargar considerablemente el tiempo de ejecución. Por otra parte, el algoritmo con el mínimo número de nodos generados y visitados es el de ramificación y acotación con subestimación, aunque también es el algoritmo con el máximo tiempo de ejecución. Esto se debe a que existe un overhead en el la inserción de nodos en la lista abierta, ya que se requiere obtener coste acumulado y valor heurístico (solo en el de subestimación) del nodo a insertar y de los nodos con los que se compara, lo que hace que la inserción en la estructura de datos de los algoritmos de ramificación y acotación sea más costosa que en el bfs y dfs. Esto se evidencia al comparar el bfs y la ramificación y acotación, que a pesar de tener un similar número de nodos generados y visitados, el b&b resulta un 54% más lento que el bfs. Sin embargo, en problemas de mayor tamaño este overhead representa una parte menos significativa del tiempo de ejecución, influyendo más el número de nodos generados y visitados (que en este caso es sufre reducción de un 28% y un 58% respectivamente sobre el bfs). Adicionalmente, los algoritmos de ramificación y acotación son óptimos respecto al coste del camino, mientras que el bfs es óptimo sobre la longitud en número de nodos del camino, que no es necesariamente coincidente con el camino de mínimo coste.
