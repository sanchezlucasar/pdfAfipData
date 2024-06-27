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

<h3>para probar Cargar facturas de afip, en formato pdf dentro de la direccion../pdfplumber/modelAfip.py </h3>

  *  al final del archivo modelAfip.py hay una seccion para agregar los path de las facturas en forma de arreglo para probar. 
  
  * en la seccion pdf_paths = [ 
             './facturas/1.pdf',
             './facturas/2.pdf',
             './facturas/3.pdf',
             './facturas/4.pdf'
             ]
  * Luego de ejecutar  python modelAfip.py se creara un archivo llamado prueba.json que tendrá un arreglo de json con los datos de la factura correspondiente 

<h3>para probar La api </h3>

  * Ejecutar el siguiente comando con el entorno virtual activado, debe aparecer de la siguiente manera , Si no aparece (mi_entorno) delante hay que activar el entorno virtual de python

```ps
 > (mi_entorno) PS C:\........\pdfplumber> uvicorn main:app --reload
``` 

  * Si todo es correcto debe aparecer lo siguiente

 ```ps
 > INFO:     Will watch for changes in these directories: ['C:\\.....\\.....\\....\\pdfplumber']
 > INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
 > INFO:     Started reloader process [1456] using WatchFiles
 > INFO:     Started server process [12040]
 > INFO:     Waiting for application startup.
 > INFO:     Application startup complete.
``` 

 *  para correr la api, desde el puerto http://127.0.0.1:8000/process_pdf/ , seleccionar el pdf, desde Form, seleccionar file, Luego ponerle nombre files y submit
  


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
