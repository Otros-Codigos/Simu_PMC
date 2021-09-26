
import random as rd

# Ciudades de los viajeros

def trip_cities():
    return {
        "Medellín":     [6.26868,   -75.59639],
        "La Dorada":    [5.53144,   -74.72005],
        "Aguadas":      [5.57937,   -75.45557],
        "Salamina":     [5.34395,   -75.40658],
        "Popayán":      [2.4427,    -76.57841],
        "Valledupar":   [10.46477,  -73.25915],
        "Bogotá":       [4.6483,    -74.10781],
        "Santana":      [3.58706,   -74.70524],
        "Neiva":        [3.03602,   -75.29684],
        "Santa Marta":  [11.23153,  -74.18245],
        "Cúcuta":       [8.07777,   -72.47725],
        "Pasto":        [1.05204,   -77.20717],
        "Génova":       [4.192,     -75.74795],
        "Calarcá":      [4.45392,   -75.68058],
        "Filandia":     [4.66388,   -75.65585],
        "Pereira":      [4.78502,   -75.65506],
        "Bucaramanga":  [7.16502,   -73.10824],
        "Barbosa":      [5.95458,   -73.62693],
        "Cali":         [3.39506,   -76.52566]
    }

# Ciudades de los usuarios

def user_cities():
    return {
        "Andes":                [5.62412, -75.95589],
        "Medellín":             [6.26868, -75.59639],
        "Dabeiba":              [6.95267, -76.29085],
        "Salgar":               [5.96643, -75.97188],
        "San Pablo de Borbur":  [5.67784, -74.10383],
        "Labranzagrande":       [5.53555, -72.59873],
        "Miraflores":           [5.15175, -73.17282],
        "Moniquirá":            [5.86963, -73.54944],
        "Manizales":            [5.07415, -75.50288],
        "Anserma":              [5.20035, -75.75022],
        "Pensilvania":          [5.40334, -75.17665],
        "Riosucio":             [5.45036, -75.73531],
        "Aguadas":              [5.57937, -75.45557],
        "Morales":              [2.84901, -76.74932],
        "El Tambo":             [2.45275, -76.81132],
        "Bolívar":              [1.89843, -76.97234],
        "Aguachica":            [8.30592, -73.61166],
        "San Diego":            [10.3357, -73.18045],
        "Caparrapí":            [5.37312, -74.51297],
        "Viotá":                [4.43705, -74.48354],
        "Sasaima":              [4.94796, -74.41729],
        "Neiva":                [3.03602, -75.29684],
        "Pitalito":             [1.77745, -76.13852],
        "Gigante":              [2.39452, -75.52775],
        "Santa Marta":          [11.2315, -74.18245],
        "La Unión":             [1.60903, -77.14714],
        "Pasto":                [1.05204, -77.20717],
        "Samaniego":            [1.38945, -77.72329],
        "Sardinata":            [8.25885, -72.79639],
        "Ocaña":                [8.22019, -73.39012],
        "Convención":           [8.83257, -73.18585],
        "Génova":               [4.19255, -75.74795],
        "Calarcá":              [4.45392, -75.68058],
        "Quimbaya":             [4.61334, -75.78586],
        "Pereira":              [4.78502, -75.65506],
        "Santuario":            [5.03229, -75.97494],
        "Belén de Umbria":      [5.19016, -75.86725],
        "Rionegro":             [7.54004, -73.42111],
        "Bucaramanga":          [7.16502, -73.10824],
        "Barbosa":              [5.95458, -73.62693],
        "Socorro":              [6.46604, -73.24775],
        "Simacota":             [6.67635, -73.62452],
        "Chaparral":            [3.75307, -75.59347],
        "Dolores":              [3.62215, -74.76516],
        "Ibagué":               [4.47824, -75.24365],
        "Líbano":               [4.87582, -75.04174],
        "Cartago":              [4.71034, -75.91931],
        "Tulua":                [4.03985, -76.06656],
        "Jamundí":              [3.20125, -76.62458],
        "Sevilla":              [4.15709, -75.88795],
        "Caicedonia":           [4.30725, -75.84114],
        "Florencia":            [1.61887, -75.60384],
        "Puerto Milán":         [1.33546, -75.51081],
        "Nunchía":              [5.53209, -72.07238],
        "Mesetas":              [3.10575, -74.12435]
}

def adjust_coordinate(coor):
        if rd.random() < .5:
                return round(coor + rd.random()*0.1, 6)
        else:
                return round(coor - rd.random()*0.1, 6)