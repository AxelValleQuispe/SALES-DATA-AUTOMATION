import pandas as pd
import numpy as np
from pathlib import Path


np.random.seed(42)


def generar_datos():
    """Genera información ficticia de ventas y operaciones."""

    n = 1000

    clientes = [
        "Cliente A",
        "Cliente B",
        "Cliente C",
        "Cliente D",
        "Cliente E",
    ]

    servicios = [
        "Servicio 1",
        "Servicio 2",
        "Servicio 3",
    ]

    productos = [
        "Producto A",
        "Producto B",
        "Producto C",
    ]

    ubicaciones = [
        "Zona Norte",
        "Zona Centro",
        "Zona Sur",
    ]

    fechas = pd.date_range(
        start="2023-01-01",
        end="2025-12-31",
        periods=n
    )

    df = pd.DataFrame({
        "cliente": np.random.choice(clientes, n),
        "fecha": fechas,
        "servicio": np.random.choice(servicios, n),
        "producto": np.random.choice(productos, n),
        "ubicacion": np.random.choice(ubicaciones, n),
        "cantidad": np.random.randint(1, 20, n),
        "monto_usd": np.round(
            np.random.uniform(500, 15000, n),
            2
        ),
    })

    df["monto_pen"] = np.round(
        df["monto_usd"] * 3.75,
        2
    )

    df["año"] = df["fecha"].dt.year
    df["mes"] = df["fecha"].dt.month

    return df


def guardar_datos(df):
    """Guarda los datos ficticios en data/raw."""

    ruta = Path("data/raw/sales_sample.xlsx")
    ruta.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_excel(
        ruta,
        index=False
    )

    print(f"Datos guardados en: {ruta}")
    print(f"Registros generados: {len(df)}")


if __name__ == "__main__":
    datos = generar_datos()

    print("Datos ficticios de ventas generados.")
    print(datos.head())

    guardar_datos(datos)