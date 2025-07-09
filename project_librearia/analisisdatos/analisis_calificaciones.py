import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === Conexión a la base de datos ===
conn = psycopg2.connect(
    dbname='libreria',
    user='postgres',
    password='12345',
    host='localhost',
    port='5432'
)

# === Consulta SQL ===
query = '''
SELECT
    c.valor,
    c.descripcion,
    c.embedding,
    l.id AS libro_id,
    l.nombre AS libro_nombre,
    g.id AS genero_id,
    g.nombre AS genero_nombre
FROM calificaciones c
JOIN libros l ON c.id_libro_fk = l.id
JOIN generos g ON l.id_genero_fk = g.id;
'''

# === Leer los datos con pandas ===
df = pd.read_sql_query(query, conn)

# === Cerrar conexión ===
conn.close()

# === Gráfico: Género más valorado ===
genero_valorado = df.groupby('genero_nombre')['valor'].mean().sort_values(ascending=False)
plt.figure(figsize=(8, 4))
sns.barplot(x=genero_valorado.index, y=genero_valorado.values, palette="viridis")
plt.title('🎭 Promedio de Valoraciones por Género')
plt.ylabel('Promedio')
plt.xlabel('Género')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# === Libro peor valorado ===
peor = df.groupby('libro_nombre')['valor'].mean().sort_values().head(1)
print("📉 Libro peor valorado:")
print(peor)

# === Libro más calificado ===
mas_calificado = df['libro_nombre'].value_counts().head(1)
print("\n📊 Libro más calificado:")
print(mas_calificado)

# === Libro más recomendado (por promedio de valoraciones) ===
promedios = df.groupby('libro_nombre')['valor'].mean()
libro_mas_recomendado = promedios[promedios == promedios.max()]
print("\n🌟 Libro más recomendado (por promedio de calificaciones):")
print(libro_mas_recomendado)

# === Mostrar géneros disponibles con ID ===
generos_disponibles = df[['genero_id', 'genero_nombre']].drop_duplicates().sort_values('genero_id')
print("\n📚 Géneros disponibles:")
for _, row in generos_disponibles.iterrows():
    print(f"  📘 {row['genero_id']} - {row['genero_nombre']}")

# === Sugerencia personalizada por ID ===
try:
    genero_id_input = int(input("\n🔎 Ingresá el ID del género para sugerir el mejor libro: "))

    # Filtrar por género y calcular promedio
    df_genero = df[df['genero_id'] == genero_id_input]
    
    if not df_genero.empty:
        nombre_genero = df_genero['genero_nombre'].iloc[0]
        mejores_libros_genero = df_genero.groupby('libro_nombre')['valor'].mean()
        sugerido = mejores_libros_genero[mejores_libros_genero == mejores_libros_genero.max()]
        
        print(f"\n✅ El libro más recomendado del género '{nombre_genero}' es:")
        for nombre_libro in sugerido.index:
            print(f"📕 {nombre_libro} (promedio: {sugerido[nombre_libro]:.2f})")
    else:
        print("⚠️ No se encontraron libros para ese ID de género.")

except ValueError:
    print("❌ El ID debe ser un número entero.")
