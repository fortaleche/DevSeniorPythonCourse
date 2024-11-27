import datetime

listaEquipos = [
    ["seleccion Colombia", "01/01/1924", "seleccion colombia", [0,2,1,2,3]],
    ["seleccion Chile", "01/01/1923", "Basquet", [0,2,1,2,3]]
]

def agregarEquipo():
    try:
        nombre = input('Ingrese el nombre del equipo: ')
        fecha = input('ingrese la fecha de creacion del equipo (DD/MM/YYYY): ')
        tipo = input('ingrese el tipo de deporte: ')
        