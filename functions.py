def promedio_estudiante(notas):
    if len(notas) == 0:
        return 0.0
    return float(sum(notas) / len(notas))