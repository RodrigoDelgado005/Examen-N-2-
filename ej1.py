alumnos = ["Rodrigo", "Rodolfo", "Romario", "Romero", "Ramardo"]  # Corregidos Rukunku y Raki

notas = {
    "Rodrigo": [7, 8, 6, 9, 7, 8],
    "Rodolfo": [9, 9, 9, 8, 9, 9],
    "Romario": [6, 7, 6, 7, 8, 7],
    "Romero": [8, 8, 8, 9, 8, 8],
    "Ramardo": [7, 6, 7, 7, 8, 7]
}

print("Promedios de los alumnos:")

for alumno, notas in notas.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio:.2f}")