# pdfplumber

Python / pdfplumber - 

# Librería utilizada  , pdfplumber
Instalacion de librería   - 

1) En la terminal (con el entorno virtual activado) ir a la ubicacion del archivo pdfplumber 

```ps
 > .../cd pdfplumber
``` 
2) escribir en terminal  pip install -r requirements.txt

2) En la terminal situado en pdfplumber,  

```ps
 > .../pdfplumber> python modelAfip.py
``` 

# Funcionalidades 

<h3>Cargar facturas de afip, en formato pdf ../pdfplumber/modelAfip.py </h3>

  * dentro del archivo modelAfip.py casi abajo al final hay una seccion para agregar los path de las facturas en forma de arreglo para probar. 

  * En la carpeta facturas, agregar las facturas a procesar 

  * en la seccion pdf_paths = [ 
             './facturas/1.pdf',
             './facturas/2.pdf',
             './facturas/3.pdf',
             './facturas/4.pdf'
             ]
  * Luego de ejecutar  python modelAfip.py se creara un archivo llamado prueba.json que tendrá un arreglo de json con los datos de la factura correspondiente 

# Pros.

<ul>
   <li> Todos los PDF se pueden procesar. </li>
   <li>La información se devuelve de manera organizada y clara.</li>
   <li> Si los PDF de un cliente tienen el mismo formato, es muy probable que se obtengan los datos de manera consistente y uniforme. </li>
</ul >

# Contras

<ul>
   <li>Para cada tipo de PDF es necesario crear un modelo específico con sus propias especificaciones.</li>
   <li>Se deben usar expresiones regulares personalizadas para cada tipo de PDF con el fin de extraer todos los datos necesarios.</li>
</ul>
