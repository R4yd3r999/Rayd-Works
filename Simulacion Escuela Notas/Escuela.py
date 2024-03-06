class Estudiante:
    def __init__(self, nombre, calificaciones, asistencia):
        self.nombre = nombre
        self.calificaciones = calificaciones
        self.asistencia = asistencia

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

    def verificar_aprobacion(self):
        promedio = self.calcular_promedio()
        if promedio >= 70 and self.asistencia >= 80:
            return f"{self.nombre} ha aprobado."
        else:
            return f"{self.nombre} no ha aprobado."

    def sugerir_plan_de_accion(self):
        promedio = self.calcular_promedio()
        if promedio < 70:
            return f"Sugerencia para {self.nombre}: Estudiar más y mejorar las calificaciones."
        elif self.asistencia < 80:
            return f"Sugerencia para {self.nombre}: Asistir a clases regularmente para mejorar la asistencia."
        else:
            return f"{self.nombre} está en buen camino."

def main():
    estudiantes = []  # Lista para almacenar estudiantes

    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'salir' para finalizar): ")
        if nombre.lower() == "salir":
            break

        calificaciones = [float(x) for x in input("Ingrese las calificaciones separadas por espacios: ").split()]
        asistencia = float(input("Ingrese el porcentaje de asistencia del estudiante: "))

        estudiante = Estudiante(nombre, calificaciones, asistencia)
        estudiantes.append(estudiante)

    # Imprimir información de todos los estudiantes
    for estudiante in estudiantes:
        print(estudiante.verificar_aprobacion())
        print(estudiante.sugerir_plan_de_accion())

if __name__ == "__main__":
    main()