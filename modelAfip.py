import json
import pdfplumber
import re
from utils.impuestosData import impuestosReturn
from utils.receptorData import dataReceptor
from utils.emisorData import dataEmisor
from utils.codigosFacturas import obtenerTipoFactura
from utils.returnItems import returnItems

# Función para extraer datos de un PDF usando pdfplumber
def extract_invoice_data(pdf_path):
    
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        page = pdf.pages[0]
        text = page.extract_text()
       
    data = {
        "factura":{
            "emisor":None,   
            "receptor":None,
            "tipoFactura":None,
            "puntoVenta":None,
            "numFactura":None,
            "periodoFacturado":{
                "desde":None,
                "hasta":None,
                "vencimientoPago":None
            },
            "subtotal":None,
            "impuestosTributos":None,
            "items":None,
            "totalFactura":None,
            "cae":{
            "numeroCae":None,
            "vencimientoCae":None
            }
        }
    }
    
    # Buscar patrones específicos en el texto
    tipoFacturaPattern = re.compile(r"COD\. (\d+)")
    puntoVentaPattern = re.compile(r"Punto de Venta: (\d+)")
    numFacturaPattern = re.compile(r"Comp. Nro: (\d+)")
    subtotalPattern = re.compile(r"Subtotal: \$ ([\d,]+.\d{2})")
    totalFacturaPattern = re.compile(r"Importe Total: \$ ([\d,]+.\d{2})")
    numeroCaePattern = re.compile(r"CAE N°: (\d+)")
    vencimientoCaePattern = re.compile(r"Fecha de Vto\. de CAE: (\d{2}/\d{2}/\d{4})")
    
    data["factura"]["tipoFactura"] = re.search(tipoFacturaPattern, text).group(1) if re.search(tipoFacturaPattern, text) else None
    data["factura"]["puntoVenta"] = re.search(puntoVentaPattern, text).group(1) if re.search(puntoVentaPattern, text) else None
    data["factura"]["numFactura"] = re.search(numFacturaPattern, text).group(1) if re.search(numFacturaPattern, text) else None
    data["factura"]["totalFactura"] = re.search(totalFacturaPattern, text).group(1) if re.search(totalFacturaPattern, text) else None
    data["factura"]["cae"]["numeroCae"] = re.search(numeroCaePattern, text).group(1) if re.search(numeroCaePattern, text) else None
    data["factura"]["cae"]["vencimientoCae"] = re.search(vencimientoCaePattern, text).group(1) if re.search(vencimientoCaePattern, text) else None
    
    #Tipo de Factura
    codTipoFactura = re.search(tipoFacturaPattern, text).group(1) if re.search(tipoFacturaPattern, text) else None
    tipoFactura = obtenerTipoFactura(codTipoFactura)
    data["factura"]["tipoFactura"] = tipoFactura
    
    if tipoFactura =='A':
        # el subtotal en la Factura A, es el Neto antes de Impuestos
        subtotalPattern = r'Importe Neto Gravado: \$ ([\d,]+(?:\.\d{2})?)'
        data["factura"]["subtotal"] = re.search(subtotalPattern, text).group(1) if re.search(subtotalPattern, text) else None
        
    data["factura"]["subtotal"] = re.search(subtotalPattern, text).group(1) if re.search(subtotalPattern, text) else None
    
    #Periodo Facturado, Desde , Hasta, Vencimiento para el pago
    periodo_facturado_pattern = re.compile(r"Período Facturado Desde: (\d{2}/\d{2}/\d{4}) Hasta:(\d{2}/\d{2}/\d{4}) Fecha de Vto. para el pago:(\d{2}/\d{2}/\d{4})")
    periodo_facturado_match = re.search(periodo_facturado_pattern, text)
    
    if periodo_facturado_match:
        data["factura"]["periodoFacturado"]["desde"] = periodo_facturado_match.group(1)
        data["factura"]["periodoFacturado"]["hasta"] = periodo_facturado_match.group(2)
        data["factura"]["periodoFacturado"]["vencimientoPago"] = periodo_facturado_match.group(3)
    
    #Items
    data["factura"]["items"] = returnItems(tipoFactura,text)  
    data["factura"]["emisor"] = dataEmisor(tipoFactura,text)
    data["factura"]["receptor"] = dataReceptor(tipoFactura,text)
    data["factura"]["impuestosTributos"] = impuestosReturn(tipoFactura,text)
  
    return data
   
# Rutas a los archivos PDF
pdf_paths = [ 
             './facturas/1.pdf',
             './facturas/2.pdf',
             './facturas/3.pdf',
             './facturas/4.pdf'
             ]
invoices_data = []

for pdf_path in pdf_paths:
    invoice_data = extract_invoice_data(pdf_path)
    invoices_data.append(invoice_data)

# Guardar los datos extraídos en un archivo para probar
with open('prueba.json', 'w') as json_file:
    json.dump(invoices_data, json_file, indent=4)
