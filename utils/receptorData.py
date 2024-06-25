import re

def dataReceptor(tipoFactura, text):
   
    receptor={
       "cuitReceptor": None,
    }
    regexCuitReceptor = r'CUIT: (\d+) Apellido y Nombre / Razón Social:'
    resultadoCuitReceptor = re.search(regexCuitReceptor, text)
   
    receptor["cuitReceptor"] = resultadoCuitReceptor.group(1).strip()  
     
    if  tipoFactura=='B':
        if not resultadoCuitReceptor: 
            #se ingresó DNI para hacer factura
            regexCuitReceptor = r'DNI: (\d+) Apellido y Nombre / Razón Social:'
            resultadoCuitReceptor = re.search(regexCuitReceptor, text)
            receptor["dniReceptor"] = resultadoCuitReceptor.group(1).strip()  
    
    return receptor; 

   
