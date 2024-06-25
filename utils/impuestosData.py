import re


def impuestosReturn(tipoFactura, text):
    impuestos={
        "iva27":None,
        "iva21":None,
        "iva10_5":None,
        "iva5":None,
        "iva2_5":None,
        "iva0":None,
        "otrosTributos":None,
    }
    
    if tipoFactura=='A':
        regexIva_27 = r'IVA 27%: \$ ([\d,]+(?:\.\d{2})?)'
        regexIva_21 = r'IVA 21%: \$ ([\d,]+(?:\.\d{2})?)'
        regexIva_10_5 = r'IVA 10\.5%: \$ ([\d,]+(?:\.\d{2})?)'
        regexIva_5 = r'IVA 5%: \$ ([\d,]+(?:\.\d{2})?)'
        regexIva_2_5 = r'IVA 2\.5%: \$ ([\d,]+(?:\.\d{2})?)'
        regexIva_0 = r'IVA 0%: \$ ([\d,]+(?:\.\d{2})?)'
        regexOtrosTributos = r'Importe Otros Tributos: \$ ([\d,]+(?:\.\d{2})?)'
        
        # Buscar coincidencias en el texto
        iva27 = re.search(regexIva_27, text)
        iva21 = re.search(regexIva_21, text)
        iva10_5 = re.search(regexIva_10_5, text)
        iva5= re.search(regexIva_5, text)
        iva2_5 = re.search(regexIva_2_5, text)
        iva0 = re.search(regexIva_0, text)
        otrosTributos = re.search(regexOtrosTributos, text)
        
        impuestos["iva27"] = iva27.group(1).strip() if iva27 else None
        impuestos["iva21"] = iva21.group(1).strip() if iva21 else None
        impuestos["iva10_5"] = iva10_5.group(1).strip() if iva10_5 else None
        impuestos["iva5"] = iva5.group(1).strip() if iva5 else None
        impuestos["iva2_5"] = iva2_5.group(1).strip() if iva2_5 else None
        impuestos["iva0"] = iva0.group(1).strip() if iva0 else None
        impuestos["otrosTributos"] = otrosTributos.group(1).strip() if otrosTributos else None
        
    
    return impuestos
