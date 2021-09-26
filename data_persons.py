"""
    Generación de datos de las personas (Viajeros y Usuarios)
"""

def combinations(ruta):

    banco = open(ruta,"r", encoding = "utf8")

    first_name = [banco.readline().rstrip() for _ in range(100)]
    first_lastName = [banco.readline().rstrip() for _ in range(100)]

    return [

        first_name[i].rstrip()
        + " "
        + first_lastName[i].rstrip()

        for i in range(100)
    ]
