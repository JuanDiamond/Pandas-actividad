import pandas as pd

peliculas = pd.read_csv("peliculas.csv")

resultado = peliculas[["titulo", "genero", "calificacion"]].copy()

resultado["clasica"] = peliculas["anio"].apply(
    lambda anio: "Si" if anio < 1995 else "No"
)

def obtener_apreciacion(calificacion):

    if calificacion > 8.5:
        return "Excelente"

    elif calificacion >= 7.0:
        return "Buena"

    elif calificacion >= 5.0:
        return "Regular"

    elif calificacion >= 3.0:
        return "Mala"

    else:
        return "Pesima"

resultado["Apreciacion"] = resultado["calificacion"].apply(
    obtener_apreciacion
)

resultado.to_csv(
    "peliculas_transformadas.csv",
    index=False
)

promedio_por_genero = (
    peliculas.groupby("genero")["calificacion"]
    .mean()
    .reset_index()
)

cantidad_por_genero = (
    peliculas.groupby("genero")
    .size()
    .reset_index(name="cantidad")
)

with pd.ExcelWriter("analisis_peliculas.xlsx") as archivo_excel:

    promedio_por_genero.to_excel(
        archivo_excel,
        sheet_name="Promedios",
        index=False
    )

    cantidad_por_genero.to_excel(
        archivo_excel,
        sheet_name="Cantidades",
        index=False
    )

print("Proceso finalizado correctamente.")
print("Se generó peliculas_transformadas.csv")
print("Se generó analisis_peliculas.xlsx")
