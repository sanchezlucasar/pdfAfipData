# Se agregan a medida que hace falta, a veces viene con 2 valores, y a veces con 3
codigosComprobantes = {
    "001": "A",
    "01":"A",
    "006": "B",
    "06": "B",
    "011": "C",
    "11": "C"
}

def obtenerTipoFactura(codigo):
    return codigosComprobantes.get(codigo, "Desconocido")
