from collections import Counter
from claseHelado import Helado

class ManejaHelados:
    def __init__(self):
        self.__helados = []

    def registrar_helado(self, helado):
        self.__helados.append(helado)

    # Aquí se pueden agregar los métodos para las opciones del menú.

    def mostrar_5_mas_pedidos(self):
        contador_sabores = Counter()
        for helado in self.__helados:
            for sabor in helado._Helado__sabores:
                contador_sabores[sabor._Sabor__idSabor] += 1
        top_5_sabores = contador_sabores.most_common(5)

        print("Los 5 sabores más pedidos son:")
        for sabor, cantidad in top_5_sabores:
            print(f"ID del sabor: {sabor}, cantidad de pedidos: {cantidad}")

    def estimar_gramos_vendidos(self, num_sabor):
        gramos_vendidos = 0
        for helado in self.__helados:
            if any(sabor._Sabor__idSabor == num_sabor for sabor in helado._Helado__sabores):
                gramos_vendidos += helado._Helado__gramos
        print(f"Se vendieron aproximadamente {gramos_vendidos} gramos del sabor {num_sabor}")

    def mostrar_sabores_por_tamano(self, tamano):
        sabores_tamano = set()
        for helado in self.__helados:
            if helado._Helado__gramos == tamano:
                for sabor in helado._Helado__sabores:
                    sabores_tamano.add(sabor._Sabor__idSabor)
        print(f"Sabores vendidos en helados de {tamano} gramos:")
        for sabor in sabores_tamano:
            print(f"ID del sabor: {sabor}")

    def calcular_importe_total(self):
        importe_total = 0
        for helado in self.__helados:
            importe_total += helado._Helado__precio
        print(f"El importe total recaudado es de {importe_total:.2f} pesos")
