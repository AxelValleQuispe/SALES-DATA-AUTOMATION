# SALES DATA AUTOMATION

Proyecto de automatización y análisis de información comercial desarrollado como proyecto de portafolio.

> **Nota:** Los datos utilizados en este repositorio son completamente ficticios y fueron creados únicamente con fines demostrativos. No se utilizan datos reales, información confidencial ni archivos internos de empresas.

## Descripción

El proyecto recrea un flujo de trabajo orientado a organizar y analizar información comercial.

El proceso permite:

- Generar datos ficticios de ventas.
- Organizar información comercial.
- Limpiar y transformar los datos.
- Consolidar información para su análisis.
- Generar indicadores de ventas.
- Analizar resultados por diferentes dimensiones.
- Generar reportes visuales.

## Flujo del proyecto

```text
Datos de entrada
       ↓
Generación de información
       ↓
Limpieza y transformación
       ↓
Dataset procesado
       ↓
Análisis comercial
       ↓
Indicadores
       ↓
Reportes gráficos
```
## Análisis realizados

El proyecto incluye análisis de:

Ventas mensuales.
Ventas anuales.
Ventas por cliente.
Ventas por producto.
Ventas por servicio.

## Tecnologías

- Python
- Pandas
- NumPy
- Matplotlib
- Excel
- CSV

## Estructura
SALES-DATA-AUTOMATION/
├── data/
│   ├── raw/
│   └── processed/
├── reports/
├── src/
├── README.md
├── requirements.txt
└── .gitignore
## Scripts principales
generate_sales_data.py

Genera un conjunto de datos ficticios de ventas y lo almacena en formato Excel.

process_sales.py

Realiza la limpieza, transformación y generación de indicadores generales.

monthly_analysis.py

Genera el resumen mensual de ventas.

yearly_analysis.py

Genera el resumen anual de ventas.

customer_analysis.py

Genera indicadores de ventas por cliente.

product_analysis.py

Genera indicadores de ventas por producto.

service_analysis.py

Genera indicadores de ventas por servicio.

create_reports.py

Genera los reportes gráficos del proyecto.

## Reportes
Ventas por año

Evolución mensual

Ventas por cliente

Ventas por producto

## Ejecución

Instalar las dependencias:

pip install -r requirements.txt

Generar los datos ficticios:

python src/generate_sales_data.py

Procesar los datos:

python src/process_sales.py

## Ejecutar los análisis:

python src/monthly_analysis.py
python src/yearly_analysis.py
python src/customer_analysis.py
python src/product_analysis.py
python src/service_analysis.py

## Generar los reportes:

python src/create_reports.py
Aplicación profesional

Este proyecto representa una versión demostrativa de tareas de automatización y análisis de información comercial.

El objetivo es mostrar la capacidad para trabajar con datos estructurados, automatizar procesos de preparación y transformación, generar indicadores y facilitar la consulta de información mediante reportes.

## Autor

Axel Valle Quispe

Data Analyst | Python | SQL | PostgreSQL | Power BI | Machine Learning