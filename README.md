# Clustering K-means 
K-means clustering es un algoritmo de agrupamiento clásica que utiliza una expectativa de maximización como técnica para particionar un número de puntos de datos en k grupos.

El objetivo de este proyecto fue la implementación de un marco de Java para la realización de k-means clustering utilizando Hadoop MapReduce.

En este problema, hemos considerado las entradas de un conjunto de datos obtenidos desde Twitter, hemos utilizado la libreria Tweepy (http://www.tweepy.org/) para la extraccion de los mismos,
la misma que funciona con Python.
Luego se aplico un analisis de sentimientos (Machine Learning) para ordenar una matriz con estos puntos que seran los niveles de 
aceptacion que las personas han dado acerca del producto evaluado, los niveles son desde -6 hasta 6.

Al tener ya la matriz vamos a Hadoop y enviamos como datos de entrada para su analisis en Map-Reduce.

#### Algoritmo

Paso 1: Inicialmente centroide al azar se selecciona sobre la base de datos.

Paso 2: El archivo de entrada contiene centroide inicial y datos.

Paso 3: En función de la clase Mapper "configurar" se utiliza para abrir primero el archivo y leer los centroides y se guardan en la estructura de datos (utilizamos ArrayList)

Paso 4: Mapper lee el archivo de datos y emite el centroide más cercano con el punto en el reduce.

Paso 5: Reduce recoge todos estos datos y calcular los nuevos centroides correspondientes y emiten.

Paso 6: En la configuración del trabajo, estamos leyendo ambos archivos y la comprobación ;si la diferencia entre el antiguo y el nuevo centro de gravedad es menor de 0,1 y luego
se alcanza la convergencia ;sino repita el paso 2 con nuevos centroides.

#### Pasos de inicio a final

#####¿Qué se necesita?

-Una o mas de una computadora superior a 8 gb de Ram, procesador core i5 2.5 ghz en adelante.

-Python (Tweepy, Matplotlib, Numpy).

-CentOS.

-Eclipse.

-Hadoop.

1. Descargar datos tweets streaming, ejecutar el archivo "/source/descarga_twitter.py", esto creara un JSON y en este se guardaran los datos "/input/datos_twitter.json".
2. Analisis de sentimientos de los datos obtenidos, ejecutar el archivo "/source/descarga_twitter.py", este generara los puntos que iran al Map-Reduce para su analisis "/input/data.txt".
3. Enviar data.txt a Hadoop para que este realize el algoritmo de K-means en Map-Reduce "/SOURCE-MAPREDUCE/K-means_Map_reduce/map_reduce_kmeans.java" y entregue el resultado.
4. Enviar data.txt a Hadoop para que este realize el algoritmo de K-means en Stand-Alone "SOURCE-MAPREDUCE/K-means_Stand_Alone/" y entregue el resultado.

