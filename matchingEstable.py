from MatchingEstable.creadorArchivos import CreadorArchivos
from MatchingEstable.lectorArchivos import LectorArchivos
from MatchingEstable.galeShapley import galeShapley
from MatchingEstable.galeShapley import galeShapleyVacants

def main():
    creador = CreadorArchivos()
    creador.crearArchivo(3, 3, "MatchingEstable/files/m1.txt")
    #creador.crearArchivo(1000, 1000, "MatchingEstable/files/m2.txt")
    #creador.crearArchivo(10000, 10000, "MatchingEstable/files/m3.txt")
    #creador.crearArchivo(100000, 100000, "MatchingEstable/files/m4.txt")

    lector = LectorArchivos()
    E = [] #Lista de listas de estudiantes
    H = [] #Lista de listas de hospitales
    Q = [] #Lista de listas de vacantes
    (E, H, Q) = lector.initListas("MatchingEstable/files/m1.txt")

    print galeShapleyVacants(E, H, Q)

main()
