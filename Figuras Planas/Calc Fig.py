class FiguraPlana:
    def __init__(self):
        pass

    def perimetro(self):
        pass

    def area(self):
        pass

class Rectangulo(FiguraPlana):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)

    def area(self):
        return self.largo * self.ancho

class Cuadrado(FiguraPlana):
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado ** 2

class Triangulo(FiguraPlana):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def perimetro(self):
        # Esto es un placeholder, se necesita conocer los lados para calcular el perímetro
        return "Perímetro no calculable con los datos proporcionados"

    def area(self):
        return (self.base * self.altura) / 2

class Circulo(FiguraPlana):
    def __init__(self, radio):
        self.radio = radio

    def perimetro(self):
        return 2 * 3.1416 * self.radio

    def area(self):
        return 3.1416 * (self.radio ** 2)

if __name__ == "__main__":
    figura = input("Introduce la figura (rectangulo, cuadrado, triangulo, circulo): ").lower()
    operacion = input("¿Qué deseas calcular (perimetro, area)?: ").lower()

    if figura == 'rectangulo' and operacion == 'perimetro' or operacion == 'area':
        largo = float(input("Introduce el largo del rectángulo: "))
        ancho = float(input("Introduce el ancho del rectángulo: "))
        rectangulo = Rectangulo(largo, ancho)

        if operacion == 'perimetro':
            print(f"El perímetro del rectángulo es {rectangulo.perimetro()}")
        elif operacion == 'area':
            print(f"El área del rectángulo es {rectangulo.area()}")

    elif figura == 'cuadrado' and operacion == 'perimetro' or operacion == 'area':
        lado = float(input("Introduce el lado del cuadrado: "))
        cuadrado = Cuadrado(lado)

        if operacion == 'perimetro':
            print(f"El perímetro del cuadrado es {cuadrado.perimetro()}")
        elif operacion == 'area':
            print(f"El área del cuadrado es {cuadrado.area()}")

    elif figura == 'triangulo' and operacion == 'perimetro' or operacion == 'area':
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        triangulo = Triangulo(base, altura)

        if operacion == 'perimetro':
            print(triangulo.perimetro())
        elif operacion == 'area':
            print(f"El área del triángulo es {triangulo.area()}")

    elif figura == 'circulo' and operacion == 'perimetro' or operacion == 'area':
        radio = float(input("Introduce el radio del círculo: "))
        circulo = Circulo(radio)

        if operacion == 'perimetro':
            print(f"El perímetro del círculo es {circulo.perimetro()}")
        elif operacion == 'area':
            print(f"El área del círculo es {circulo.area()}")

    else:
        print("Operacion o Figura no reconocida.")