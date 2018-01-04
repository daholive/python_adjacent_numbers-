# Adjacent Numbers

Neste caso, a regra é:

<p>Um array A não-vazio com índice zero contém N inteiros.</p>
<p>Um par de índices (P, Q) onde 0 ≤ P < Q < N, é dito adjacente, se nenhum valor "encontra-se estritamente" entre A[P] e A[Q].</p>
    
<p>Aqui, a regra para criar as tuplas (P, Q) indica que não pode haver valores intermediários entre 2 elementos, portanto:</p>


Valor   |  0 |  3 |  3 |  7 |  5 |  3 | 11 |  1 |  
--------+----+----+----+----+----+----+----+----+  
Índice  |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  


Tuplas (P, Q) de índices (explicação segue a notação valor[índice] ou valor):

(0, 1)  => não, porque tem o valor 1[7] entre 0 e 3<br>
(0, 2)  => não, porque tem o valor 1[7] entre 0 e 3<br>
(0, 3)  => não, porque tem o valores 1[7] e 5[4] entre 0 e 7<br>
(0, 4)  => não, porque tem o valor 1[7] e 3[1] entre 0 e 5<br>
(0, 5)  => não, porque tem o valor 1[7] entre 0 e 3<br>
(0, 6)  => não, porque tem o valores 1[7], 3[1], 5[4] e 7[3] entre 0 e 11<br>
(0, 7)  => SIM, porque não há valor entre 0 e 1 (adjacentes)<br><br>

(1, 2)  => SIM, porque não há valor entre 3 e 3 (adjacentes)<br>
(1, 3)  => não, porque tem o valor 5[4] entre 3 e 7<br>
(1, 4)  => SIM, porque não há valor entre 3 e 5 (adjacentes)<br>
(1, 5)  => SIM, porque não há valor entre 3 e 3 (adjacentes)<br>
(1, 6)  => não, porque tem o valores 5[4] e 7[3] entre 3 e 11<br>
(1, 7)  => SIM, porque não há valor entre 3 e 1 (adjacentes)<br><br>

(2, 3)  => não, porque tem o valor 5[4] entre 3 e 7<br>
(2, 4)  => SIM, porque não há valor entre 3 e 5 (adjacentes)<br><br>
.....
.....
.....

E seguindo esses passos, obtém-se o conjunto das tuplas:<br>

(0, 7), (1, 2), (1, 4),<br>
(1, 5), (1, 7), (2, 4),<br>
(2, 5), (2, 7), (3, 4),<br>
(3, 6), (4, 5), (5, 7)<br>

