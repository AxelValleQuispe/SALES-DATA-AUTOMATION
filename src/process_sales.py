import pandas as pd
from pathlib import Path


RUTA_ENTRADA = Path("data/raw/sales_sample.xlsx")
RUTA_SALIDA = Path("data/processed/sales_clean.csv")


def cargar_datos():
    """Carga el archivo Excel de ventas."""

    return pd.read_excel(RUTA_ENTRADA)


def limpiar_datos(df):
    """Realiza limpieza básica de la información."""

    df = df.copy()

    # Normalizar nombres de columnas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Convertir fecha
    df["fecha"] = pd.to_datetime(df["fecha"])

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Ordenar por fecha
    df = df.sort_values("fecha")

    return df


def generar_indicadores(df):
    """Genera indicadores básicos de ventas."""

    indicadores = {
        "registros": len(df),
        "clientes": df["cliente"].nunique(),
        "ventas_usd": round(df["monto_usd"].sum(), 2),
        "ventas_pen": round(df["monto_pen"].sum(), 2),
        "promedio_venta_usd": round(
            df["monto_usd"].mean(),
            2
        ),
    }

    return indicadores


def guardar_datos(df):
    """Guarda los datos procesados."""

    RUTA_SALIDA.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        RUTA_SALIDA,
        index=False
    )

    print(f"Datos procesados guardados en: {RUTA_SALIDA}")


def main():

    print("=" * 50)
    print("PROCESAMIENTO DE DATOS DE VENTAS")
    print("=" * 50)

    df = cargar_datos()

    print(f"\nRegistros originales: {len(df)}")

    df = limpiar_datos(df)

    print(f"Registros después de limpieza: {len(df)}")

    print("\nINDICADORES")
    print("-" * 30)

    indicadores = generar_indicadores(df)

    for clave, valor in indicadores.items():
        print(f"{clave}: {valor}")

    guardar_datos(df)

    print("\nProcesamiento finalizado correctamente.")


if __name__ == "__main__":
    main()