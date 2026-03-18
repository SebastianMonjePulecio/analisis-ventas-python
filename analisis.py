import pandas as pd

data = {
    "producto": ["A", "B", "A", "C", "B", "A", "C", "B"],
    "ventas": [100, 200, 150, 300, 250, 120, 180, 220],
    "ciudad": ["Cali", "Bogota", "Cali", "Medellin", "Bogota", "Cali", "Medellin", "Bogota"]
}

df = pd.DataFrame(data)

# Total ventas
total = df["ventas"].sum()

# Ventas por ciudad
ventas_ciudad = df.groupby("ciudad")["ventas"].sum()

# Ciudad top
mejor_ciudad = ventas_ciudad.idxmax()

# Ventas por producto
ventas_producto = df.groupby("producto")["ventas"].sum()

# Producto top
mejor_producto = ventas_producto.idxmax()

print("Total ventas:", total)
print("Ventas por ciudad:\n", ventas_ciudad)
print("Mejor ciudad:", mejor_ciudad)
print("Producto más vendido:", mejor_producto)
