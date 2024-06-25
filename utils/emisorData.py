import re

def dataEmisor(tipoFactura, text):
   
    emisor={
     "razonSocial":None,
     "condicionIva":None,
     "cuitEmisor": None,
     "fechaInicioActividades":None,
     "numIngresosBrutos":None,
    }
    
    razonSocialEmisorPattern = r'FACTURA\s*(.*?)\s*COD\.'
    razonSocialEmisor =re.search(razonSocialEmisorPattern, text, re.DOTALL)
    if razonSocialEmisor: emisor["razonSocial"]= razonSocialEmisor.group(1).strip()
        
    regexIngresosBrutos = r'Ingresos Brutos: (\d+)'
    regexCondicionIva = r'Condición frente al IVA: ([\w\s]+?) Fecha'
    regexFechaInicio = r'Fecha de Inicio de Actividades: (\d{2}/\d{2}/\d{4})'
        
    resultadoIngresosBrutos = re.search(regexIngresosBrutos, text)
    if resultadoIngresosBrutos:  emisor["numIngresosBrutos"] =resultadoIngresosBrutos.group(1).strip()
        
    resultadoCondicionIva = re.search(regexCondicionIva, text)
    if resultadoCondicionIva:  emisor["condicionIva"] =resultadoCondicionIva.group(1).strip()
        
    resultadoFechaInicio = re.search(regexFechaInicio, text)
    if resultadoFechaInicio: emisor["fechaInicioActividades"] =resultadoFechaInicio.group(1).strip()
    
    regexDomicilio = r'Domicilio Comercial: (.*?) CUIT:'
    regexCuit = r'CUIT: (\d+)'
    resultadoDomicilio = re.search(regexDomicilio, text)
    resultadoCuit = re.search(regexCuit, text)
    if resultadoDomicilio :  emisor["domicilioComercial"]  =  resultadoDomicilio.group(1).strip()
    if resultadoCuit :  emisor["cuitEmisor"]  =  resultadoCuit.group(1).strip()
        
    elif tipoFactura=='C': 
        
        regexRazonSocial = r'Razón Social: (.*?) Fecha de Emisión:'
        resultadoRazonSocial = re.search(regexRazonSocial, text)
        if resultadoRazonSocial: emisor["razonSocial"] = resultadoRazonSocial.group(1).strip()         
    
    return emisor; 

   
