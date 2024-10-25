from atletas import *

if __name__ == "__main__" :
    corredor = Corredor('Usain Bolt', 38, 94)
    print(corredor)
    print(corredor.aquecer())
    print(corredor.correr())

    nadador = Nadador('Cesar Cielo', 37, 88.8)
    print(nadador)
    print(nadador.aquecer())
    print(nadador.nadar())

    ciclista = Ciclista('Henrique Avancini', 35, 67.2)
    print(ciclista)
    print(ciclista.aquecer())
    print(ciclista.pedalar())

    triatleta = Triatleta('Fernanda Keller', 61, 56)
    print(triatleta)
    print(triatleta.aquecer())
    print(triatleta.realizar_maratona())

    print(Triatleta.__mro__)
