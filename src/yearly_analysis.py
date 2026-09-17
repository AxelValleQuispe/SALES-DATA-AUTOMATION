import pandas as pd
from pathlib import Path


RUTA_ENTRADA = Path("data/processed/sales_clean.csv")
RUTA_SALIDA = Path("data/processed/yearly_sales.csv")


def analizar_ventas_anuales(df):
    """Calcula indicadores agrupados por año."""

    resumen = (
        df.groupby("año")
        .agg(
            ventas_usd=("monto_usd", "sum"),
            ventas_pen=("monto_pen", "sum"),
            operaciones=("cliente", "count"),
            clientes=("cliente", "nunique"),
        )
        .reset_index()
    )

    resumen["ventas_usd"] = resumen["ventas_usd"].round(2)
    resumen["ventas_pen"] = resumen["ventas_pen"].round(2)

    return resumen


def main():

    print("=" * 50)
    print("ANÁLISIS ANUAL DE VENTAS")
    print("=" * 50)

    df = pd.read_csv(RUTA_ENTRADA)

    resumen = analizar_ventas_anuales(df)

    print("\nRESULTADOS ANUALES")
    print("-" * 30)
    print(resumen)

    RUTA_SALIDA.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    resumen.to_csv(
        RUTA_SALIDA,
        index=False
    )

    print(
        f"\nResultado guardado en: {RUTA_SALIDA}"
    )

    print("\nAnálisis anual finalizado correctamente.")


if __name__ == "__main__":
    main()