def ingresar_calificaciones():
    calificaciones = []
    print("Programa para ingresar calificaciones")
    
    while True:
        try:
            nota = float(input("Ingresa una calificación: "))
            if 0 <= nota <= 10:
                calificaciones.append(nota)
                print(f"Nota {nota} agregada correctamente")
            else:
                print("Por favor, ingresa una calificación válida entre 0 y 10")
                continue
                
            respuesta = input("¿Deseas ingresar otra nota? (s/n): ")
            if respuesta.lower() != 's':
                break
                
        except ValueError:
            print("Por favor, ingresa un número válido")
    
    return calificaciones

def analizar_calificaciones(calificaciones):
    if not calificaciones:
        print("No se ingresaron calificaciones")
        return
    
    nota_maxima = max(calificaciones)
    nota_minima = min(calificaciones)
    promedio = sum(calificaciones) / len(calificaciones)
    
    print("\nResultados:")
    print("-" * 30)
    print(f"Calificación más alta: {nota_maxima}")
    print(f"Calificación más baja: {nota_minima}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Total de calificaciones ingresadas: {len(calificaciones)}")

print("Programa de análisis de calificaciones")
print("-" * 30)
calificaciones = ingresar_calificaciones()
analizar_calificaciones(calificaciones)