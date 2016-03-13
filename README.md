Clustering K-means

K-means clustering es un algoritmo de agrupamiento clásica que utiliza una expectativa de maximización como técnica para particionar un número de puntos de datos en k grupos.

El objetivo de este proyecto fue la implementación de un marco de Java para la realización de k-means clustering utilizando Hadoop MapReduce.

En este problema, hemos considerado las entradas de un conjunto de datos obtenidos desde Twitter, hemos utilizado la libreria Tweepy (http://www.tweepy.org/) para la extraccion de los mismos,
la misma que funciona con Python.
Luego se aplico un analisis de sentimientos (Machine Learning) para ordenar una matriz con estos puntos que seran los niveles de 
aceptacion que las personas han dado acerca del producto evaluado, los niveles son desde -6 hasta 6.

Al tener ya la matriz vamos a Hadoop y enviamos como datos de entrada para su analisis ya sea Stand-Alone o Map-Reduce.


Algoritmo:
Paso 1: Inicialmente centroide al azar se selecciona sobre la base de datos.

Paso 2: El archivo de entrada contiene centroide inicial y datos.

Paso 3: En función de la clase Mapper "configurar" se utiliza para abrir primero el archivo y leer los centroides y se guardan en la estructura de datos (utilizamos ArrayList)

Paso 4: Mapper lee el archivo de datos y emite el centroide más cercano con el punto en el reduce.

Paso 5: Reduce recoge todos estos datos y calcular los nuevos centroides correspondientes y emiten.

Paso 6: En la configuración del trabajo, estamos leyendo ambos archivos y la comprobación ;si la diferencia entre el antiguo y el nuevo centro de gravedad es menor de 0,1 y luego
se alcanza la convergencia ;sino repita el paso 2 con nuevos centroides.

Ejemplo:

Para los datos esto deberia funcionar de manera sencilla:

3.0
0.0
0.0
0.0
0.0
0.0
1.0
0.0
3.0
0.0
0.0
-1.0
-2.0
1.0
0.0
0.0
1.0
0.0
6.0
...




