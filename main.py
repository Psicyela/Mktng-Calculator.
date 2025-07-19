def calcular_roi(ganancia, costo):
    """Calcula el Retorno de Inversión (ROI)."""
    if costo <= 0:
        raise ValueError("El costo debe ser mayor que 0.")
    return (ganancia - costo) / costo * 100


def calcular_cpc(costo_total, total_clics):
    """Calcula el Costo Por Clic (CPC)."""
    if total_clics <= 0:
        raise ValueError("El total de clics debe ser mayor que 0.")
    return costo_total / total_clics


def calcular_cpa(costo_total, total_adquisiciones):
    """Calcula el Costo Por Adquisición (CPA)."""
    if total_adquisiciones <= 0:
        raise ValueError("El total de adquisiciones debe ser mayor que 0.")
    return costo_total / total_adquisiciones


def calcular_tasa_conversion(total_conversiones, total_acciones):
    """Calcula la tasa de conversión como un porcentaje."""
    if total_acciones <= 0:
        raise ValueError("El total de acciones debe ser mayor que 0.")
    return (total_conversiones / total_acciones) * 100


def simulacion_inputs_usuario():
    """Simula inputs del usuario y muestra los resultados."""
    try:
        presupuesto_total = float(input("Introduce tu presupuesto total: "))
        ganancia_total_esperada = float(input("Introduce la ganancia total esperada: "))
        total_clics_esperados = float(input("Introduce el total de clics esperados: "))
        total_adquisiciones_esperadas = float(input("Introduce el total de adquisiciones esperadas: "))
        total_conversiones_esperadas = float(input("Introduce el total de conversiones esperadas: "))

        roi = calcular_roi(ganancia_total_esperada, presupuesto_total)
        cpc = calcular_cpc(presupuesto_total, total_clics_esperados)
        cpa = calcular_cpa(presupuesto_total, total_adquisiciones_esperadas)
        tasa_conversion = calcular_tasa_conversion(total_conversiones_esperadas, total_clics_esperados)

        print("\nResultados basados en los inputs:")
        print(f"ROI: {roi:.2f}%")
        print(f"CPC: ${cpc:.2f}")
        print(f"CPA: ${cpa:.2f}")
        print(f"Tasa de conversión: {tasa_conversion:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    simulacion_inputs_usuario()
