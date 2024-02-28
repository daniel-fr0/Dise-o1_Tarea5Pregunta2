# Problema
Sea un conjunto $C$ de $n$ números enteros positivos distintos. ¿Cuál es la menor
cantidad de números que debe eliminarse de $C$ de tal forma que no existan $x,y \in C$ tal que
$x + y$ sea un número primo?

Diseñe un algoritmo que pueda responder esta consulta en tiempo $O(n^2 \sqrt{n})$. A efectos de
esta pregunta, puede suponer que consultar si un número es primo es $O(1)$.

Pista: El teorema de König puede ser de utilidad.

El teorema de König dice que en un grafo bipartito, el número de aristas en un emparejamiento máximo es igual al número de nodos de un minimo cubrimiento por vertices.