import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


RUTA_ANUAL = Path("data/processed/yearly_sales.csv")
RUTA_MENSUAL = Path("data/processed/monthly_sales.csv")

RUTA_REPORTE_ANUAL = Path("reports/yearly_sales.png")
RUTA_REPORTE_MENSUAL = Path("reports/monthly_sales.png")


def crear_grafico_anual():
    df = pd.read_csv(RUTA_ANUAL)

    plt.figure(figsize=(10, 6))

    plt.bar(
        df["año"].astype(str),
        df["ventas_usd"]
    )

    plt.title("Ventas por año")
    plt.xlabel("Año")
    plt.ylabel("Ventas (USD)")
    plt.tight_layout()

    RUTA_REPORTE_ANUAL.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    plt.savefig(RUTA_REPORTE_ANUAL, dpi=150)
    plt.close()

    print(f"Reporte generado: {RUTA_REPORTE_ANUAL}")


def crear_grafico_mensual():
    df = pd.read_csv(RUTA_MENSUAL)

    df["periodo"] = (
        df["año"].astype(str)
        + "-"
        + df["mes"].astype(str).str.zfill(2)
    )

    plt.figure(figsize=(12, 6))

    plt.plot(
        df["periodo"],
        df["ventas_usd"],
        marker="o"
    )

    plt.title("Evolución mensual de ventas")
    plt.xlabel("Periodo")
    plt.ylabel("Ventas (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    RUTA_REPORTE_MENSUAL.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    plt.savefig(RUTA_REPORTE_MENSUAL, dpi=150)
    plt.close()

    print(f"Reporte generado: {RUTA_REPORTE_MENSUAL}")

def crear_grafico_clientes():
    df = pd.read_csv("data/processed/customer_sales.csv")

    plt.figure(figsize=(10, 6))

    plt.bar(
        df["cliente"],
        df["ventas_usd"]
    )

    plt.title("Ventas por cliente")
    plt.xlabel("Cliente")
    plt.ylabel("Ventas (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta = Path("reports/customer_sales.png")
    ruta.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(ruta, dpi=150)
    plt.close()

    print(f"Reporte generado: {ruta}")


def crear_grafico_productos():
    df = pd.read_csv("data/processed/product_sales.csv")

    plt.figure(figsize=(10, 6))

    plt.bar(
        df["producto"],
        df["ventas_usd"]
    )

    plt.title("Ventas por producto")
    plt.xlabel("Producto")
    plt.ylabel("Ventas (USD)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta = Path("reports/product_sales.png")
    ruta.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(ruta, dpi=150)
    plt.close()

    print(f"Reporte generado: {ruta}")
if __name__ == "__main__":
    crear_grafico_anual()
    crear_grafico_mensual()
    crear_grafico_clientes()
    crear_grafico_productos()