# Calcular monto de descuento aplicando porcentaje en una compra
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicando el porcentaje al monto total de la compra.
    
    Args:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float, optional): El porcentaje de descuento. El valor predeterminado es 10%.
    
    Returns:
        float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la función con solo el monto total de la compra
monto_total = 1000
descuento = calcular_descuento(monto_total)
monto_final = monto_total - descuento
print(f"Monto total de la compra: ${monto_total:.2f}")
print(f"Descuento aplicado (10%): ${descuento:.2f}")
print(f"Monto final a pagar: ${monto_final:.2f}")

# Llamada a la función con el monto total de la compra y el porcentaje de descuento
monto_total = 4500
porcentaje_descuento = 15
descuento = calcular_descuento(monto_total, porcentaje_descuento)
monto_final = monto_total - descuento
print(f"\nMonto total de la compra: ${monto_total:.2f}")
print(f"Descuento aplicado ({porcentaje_descuento}%): ${descuento:.2f}")
print(f"Monto final a pagar: ${monto_final:.2f}")
