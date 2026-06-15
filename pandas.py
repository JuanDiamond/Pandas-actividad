import pandas as pd
df = pd.read_csv("peliculas.csv")
nuevo_df = df[["titulo", "genero", "calificacion"]].copy()

nuevo_df["clasica"] = df["anio"] < 1995
def clasificar(calificacion):
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

nuevo_df["Apreciacion"] = nuevo_df["calificacion"].apply(clasificar)

nuevo_df.to_csv("peliculas_transformadas.csv", index=False)

promedio_genero = (
    df.groupby("genero")["calificacion"]
    .mean()
    .reset_index()
)

cantidad_genero = (
    df.groupby("genero")
    .size()
    .reset_index(name="cantidad")
)

#Excel
with pd.ExcelWriter("analisis_peliculas.xlsx") as writer:
    promedio_genero.to_excel(
        writer,
        sheet_name="Promedios",
        index=False
    )

    cantidad_genero.to_excel(
        writer,
        sheet_name="Cantidades",
        index=False
    )

print("Archivos generados correctamente.")
