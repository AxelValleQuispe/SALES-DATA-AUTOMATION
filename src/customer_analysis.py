import pandas as pd
from pathlib import Path


RUTA_ENTRADA = Path("data/processed/sales_clean.csv")
RUTA_SALIDA = Path("data/processed/customer_sales.csv")


def analizar_por_cliente(df):
    """Calcula indicadores de ventas por cliente."""

    resumen = (
        df.groupby("cliente")
        .agg(
            ventas_usd=("monto_usd", "sum"),
            ventas_pen=("monto_pen", "sum"),
            operaciones=("cliente", "count"),
            productos=("producto", "nunique"),
            servicios=("servicio", "nunique"),
        )
        .reset_index()
    )

    resumen["ventas_usd"] = resumen["ventas_usd"].round(2)
    resumen["ventas_pen"] = resumen["ventas_pen"].round(2)

    resumen = resumen.sort_values(
        "ventas_usd",
        ascending=False
    )

    return resumen


def main():

    print("=" * 50)
    print("ANÁLISIS DE VENTAS POR CLIENTE")
    print("=" * 50)

    df = pd.read_csv(RUTA_ENTRADA)

    resumen = analizar_por_cliente(df)

    print("\nRESULTADOS")
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

    print("\nAnálisis por cliente finalizado correctamente.")


if __name__ == "__main__":
    main()