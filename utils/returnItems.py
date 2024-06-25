import re

def returnItems(tipoFactura, text):
    
    if tipoFactura == 'B' or tipoFactura == 'C':
        regexItems = re.search(r'Código Producto \/ Servicio Cantidad U\. Medida Precio Unit\. % Bonif Imp\. Bonif\. Subtotal(.*?)CAE N°:', text, re.DOTALL)

        # Extraer el texto encontrado por el regex
        itemsTexto = regexItems.group(1).strip() if regexItems else ""
            
        if itemsTexto:
            # Eliminar la palabra 'Subtotal' y el contenido final no necesario
            itemsTexto = re.sub(r'Subtotal:.*', '', itemsTexto, flags=re.DOTALL).strip()
            # Regex para dividir en items completos
            itemRegex = re.compile(r'(.*?unidades \d+,\d{2} \d+,\d{2} \d+,\d{2} \d+,\d{2})', re.DOTALL)
            items = itemRegex.findall(itemsTexto)
            items = [item.strip() for item in items if item.strip()]
             # Crear la lista de objetos {Detalle, Precio}
            itemsObj = []
            for item in items:
                detalleRegex = re.search(r'^(.*?unidades)', item, re.DOTALL)
                detalle = detalleRegex.group(1).strip() if detalleRegex else ""
                detalle = detalle.replace('\n', ' ')
                    # Eliminar la palabra 'unidades' y el valor después de la coma
                detalle = re.sub(r',\d{2} unidades$', '', detalle)
                detalle = re.sub(r'unidades\s*$', '', detalle).strip()
                    # Extraer el precio correcto
                precioRegex = re.findall(r'unidades\s*\d+,\d{2}\s*\d+,\d{2}\s*\d+,\d{2}\s*\d+,\d{2}', item)
                if precioRegex:
                    precios = precioRegex[0].split()
                    if len(precios) >= 2:
                        precio = precios[1].strip()
                    else:
                        precio = ""
                else:
                    precio = ""

                itemsObj.append({
                    "detalle": detalle,
                    "precio": precio
                })

        return itemsObj
    
    elif tipoFactura == 'A':
        regexItems = re.search(  r'Código Producto / Servicio Cantidad U\. medida Precio Unit\. % Bonif Subtotal Subtotal c/IVA\s*IVA\s*(.*?)\s*Importe Otros Tributos:', text, re.DOTALL)

        # Extraer el texto encontrado por el regex
        itemsTexto = regexItems.group(1).strip() if regexItems else ""
           
        # Dividir el texto en ítems utilizando el patrón identificado
        itemRegex = re.compile(r'(.*?)\s*%\s*(\d+,\d{2})', re.DOTALL)
        itemsDivididos = itemRegex.findall(itemsTexto)

        # Crear la lista de objetos {Detalle, Precio}
        itemsObj = []
        for detalle, precio in itemsDivididos:
            detalle = detalle.strip()
            detalle = re.sub(r'\n', ' ', detalle.strip())  # Eliminar saltos de línea y espacios al inicio/final
            detalle = re.sub(r',\d{2}\s*unidades.*', '', detalle).strip()  # Asegurar que detalle termine antes de "unidades"
            precio = precio.strip()
            itemsObj.append({
                "Detalle": detalle,
                "Precio": precio
            })

        return itemsObj
    return []
