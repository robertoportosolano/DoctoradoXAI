import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Configuración para mejor visualización
plt.rcParams['font.size'] = 12
plt.rcParams['figure.figsize'] = (15, 10)

# Datos proporcionados
datos = [2, 3, 4, 5, 6, 6, 6, 6, 7, 8, 9, 9, 9, 10, 12, 14, 15, 16, 17, 18, 
         20, 20, 20, 20, 30, 30, 30, 30, 35, 80]

print("=== ANÁLISIS ESTADÍSTICO COMPLETO ===")
print(f"Datos ordenados: {sorted(datos)}")
print(f"Número de datos: {len(datos)}")

# Cálculos detallados
q1 = np.percentile(datos, 25)
q2 = np.percentile(datos, 50)
q3 = np.percentile(datos, 75)
iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

valores_atipicos = [x for x in datos if x < limite_inferior or x > limite_superior]
datos_no_atipicos = [x for x in datos if x >= limite_inferior and x <= limite_superior]

print(f"\n=== CUARTILES ===")
print(f"Q1 (Percentil 25): {q1}")
print(f"Q2 (Mediana): {q2}")
print(f"Q3 (Percentil 75): {q3}")
print(f"Rango intercuartílico (IQR): {iqr}")

print(f"\n=== LÍMITES ===")
print(f"Límite inferior para atípicos: {limite_inferior}")
print(f"Límite superior para atípicos: {limite_superior}")

print(f"\n=== VALORES ATÍPICOS ===")
print(f"Valores atípicos: {valores_atipicos}")
print(f"Dato menor no atípico: {min(datos_no_atipicos)}")
print(f"Dato mayor no atípico: {max(datos_no_atipicos)}")

# CREAR LA VISUALIZACIÓN COMPLETA
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

# =============================================
# GRÁFICO 1: Diagrama de caja básico con anotaciones
# =============================================
box_plot = ax1.boxplot(datos, vert=True, patch_artist=True, 
                      boxprops=dict(facecolor='lightblue', alpha=0.7),
                      medianprops=dict(color='red', linewidth=3),
                      whiskerprops=dict(color='black', linewidth=2),
                      capprops=dict(color='black', linewidth=2),
                      flierprops=dict(marker='o', color='red', markersize=8, markerfacecolor='red'))

ax1.set_title('DIAGRAMA DE CAJA Y BIGOTES - DETALLADO', fontsize=14, fontweight='bold')
ax1.set_ylabel('Valores')
ax1.grid(True, alpha=0.3)

# Añadir líneas y anotaciones
ax1.axhline(y=q1, color='blue', linestyle='--', alpha=0.7, linewidth=2)
ax1.axhline(y=q2, color='red', linestyle='--', alpha=0.7, linewidth=2)
ax1.axhline(y=q3, color='green', linestyle='--', alpha=0.7, linewidth=2)
ax1.axhline(y=limite_superior, color='orange', linestyle=':', alpha=0.7, linewidth=2)

# Anotaciones de texto
ax1.text(1.1, q1, f'Q1 = {q1}', va='center', ha='left', fontweight='bold', color='blue')
ax1.text(1.1, q2, f'Q2 = {q2}', va='center', ha='left', fontweight='bold', color='red')
ax1.text(1.1, q3, f'Q3 = {q3}', va='center', ha='left', fontweight='bold', color='green')
ax1.text(1.1, limite_superior, f'Límite Superior = {limite_superior:.1f}', 
         va='center', ha='left', fontweight='bold', color='orange')
ax1.text(1.1, min(datos_no_atipicos), f'Mínimo = {min(datos_no_atipicos)}', 
         va='center', ha='left', fontweight='bold', color='purple')
ax1.text(1.1, max(datos_no_atipicos), f'Máximo = {max(datos_no_atipicos)}', 
         va='center', ha='left', fontweight='bold', color='purple')

# =============================================
# GRÁFICO 2: Diagrama con seaborn + puntos
# =============================================
sns.boxplot(y=datos, ax=ax2, color='lightgreen')
sns.swarmplot(y=datos, color='darkblue', ax=ax2, size=6)
ax2.set_title('DIAGRAMA CON PUNTOS DE DATOS VISIBLES', fontsize=14, fontweight='bold')
ax2.set_ylabel('Valores')
ax2.grid(True, alpha=0.3)

# Añadir líneas de referencia
ax2.axhline(y=q1, color='blue', linestyle='--', alpha=0.5)
ax2.axhline(y=q2, color='red', linestyle='--', alpha=0.5)
ax2.axhline(y=q3, color='green', linestyle='--', alpha=0.5)

# =============================================
# GRÁFICO 3: Histograma con distribución
# =============================================
ax3.hist(datos, bins=15, color='skyblue', edgecolor='black', alpha=0.7)
ax3.axvline(x=q1, color='blue', linestyle='--', linewidth=2, label=f'Q1 = {q1}')
ax3.axvline(x=q2, color='red', linestyle='--', linewidth=2, label=f'Q2 = {q2}')
ax3.axvline(x=q3, color='green', linestyle='--', linewidth=2, label=f'Q3 = {q3}')
ax3.axvline(x=limite_superior, color='orange', linestyle=':', linewidth=2, 
           label=f'Límite Superior = {limite_superior:.1f}')
ax3.set_title('HISTOGRAMA CON CUARTILES', fontsize=14, fontweight='bold')
ax3.set_xlabel('Valores')
ax3.set_ylabel('Frecuencia')
ax3.legend()
ax3.grid(True, alpha=0.3)

# =============================================
# GRÁFICO 4: Diagrama de puntos vertical
# =============================================
y = np.random.normal(1, 0.04, len(datos))  # Pequeña dispersión aleatoria para visualización
ax4.scatter(datos, y, alpha=0.6, s=50, color='purple')

# Añadir líneas verticales para los cuartiles
ax4.axvline(x=q1, color='blue', linestyle='--', linewidth=2, label=f'Q1 = {q1}')
ax4.axvline(x=q2, color='red', linestyle='--', linewidth=2, label=f'Q2 = {q2}')
ax4.axvline(x=q3, color='green', linestyle='--', linewidth=2, label=f'Q3 = {q3}')
ax4.axvline(x=limite_superior, color='orange', linestyle=':', linewidth=2, 
           label=f'Límite Superior = {limite_superior:.1f}')

# Destacar valores atípicos
atipicos_x = [x for x in datos if x > limite_superior]
atipicos_y = [1] * len(atipicos_x)
ax4.scatter(atipicos_x, atipicos_y, color='red', s=100, marker='X', 
           label=f'Valores atípicos: {atipicos_x}')

ax4.set_title('DIAGRAMA DE PUNTOS VERTICAL', fontsize=14, fontweight='bold')
ax4.set_xlabel('Valores')
ax4.set_yticks([])
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# =============================================
# GRÁFICO ADICIONAL: Solo el diagrama de caja principal
# =============================================
plt.figure(figsize=(12, 8))
main_plot = plt.boxplot(datos, vert=True, patch_artist=True,
                       boxprops=dict(facecolor='lightyellow', alpha=0.8, edgecolor='black'),
                       medianprops=dict(color='red', linewidth=4),
                       whiskerprops=dict(color='black', linewidth=2),
                       capprops=dict(color='black', linewidth=3),
                       flierprops=dict(marker='X', color='darkred', markersize=10, 
                                     markeredgewidth=2))

plt.title('DIAGRAMA DE CAJA Y BIGOTES - VISIÓN PRINCIPAL\nConjunto de Datos Completo', 
          fontsize=16, fontweight='bold', pad=20)
plt.ylabel('Valores', fontsize=12)
plt.grid(True, alpha=0.3)

# Añadir todas las anotaciones importantes
plt.axhline(y=q1, color='blue', linestyle='--', alpha=0.8, linewidth=2)
plt.axhline(y=q2, color='red', linestyle='--', alpha=0.8, linewidth=2)
plt.axhline(y=q3, color='green', linestyle='--', alpha=0.8, linewidth=2)
plt.axhline(y=limite_superior, color='orange', linestyle=':', alpha=0.8, linewidth=2)

# Texto con flechas
plt.annotate(f'Q1 = {q1}', xy=(1, q1), xytext=(1.2, q1-2),
            arrowprops=dict(arrowstyle='->', color='blue'), fontweight='bold', color='blue')
plt.annotate(f'Mediana = {q2}', xy=(1, q2), xytext=(1.2, q2+2),
            arrowprops=dict(arrowstyle='->', color='red'), fontweight='bold', color='red')
plt.annotate(f'Q3 = {q3}', xy=(1, q3), xytext=(1.2, q3-2),
            arrowprops=dict(arrowstyle='->', color='green'), fontweight='bold', color='green')
plt.annotate(f'Límite Superior = {limite_superior:.1f}', xy=(1, limite_superior), 
            xytext=(1.2, limite_superior+2),
            arrowprops=dict(arrowstyle='->', color='orange'), fontweight='bold', color='orange')
plt.annotate(f'VALOR ATÍPICO: {valores_atipicos[0]}', xy=(1, valores_atipicos[0]), 
            xytext=(1.3, valores_atipicos[0]),
            arrowprops=dict(arrowstyle='->', color='darkred'), 
            fontweight='bold', color='darkred')

plt.tight_layout()
plt.show()

# =============================================
# RESUMEN FINAL EN CONSOLA
# =============================================
print(f"\n" + "="*50)
print("RESUMEN FINAL COMPLETO")
print("="*50)
print(f"📊 Total de datos: {len(datos)}")
print(f"🎯 Rango completo: {min(datos)} - {max(datos)}")
print(f"📦 IQR (Rango intercuartílico): {iqr}")
print(f"🔴 Valores atípicos: {valores_atipicos}")
print(f"📈 Forma de distribución: Asimétrica positiva (sesgo a la derecha)")
print(f"💡 El valor {valores_atipicos[0]} está muy alejado del resto de datos")
print("="*50)

# Estadísticas adicionales
print(f"\n=== ESTADÍSTICAS ADICIONALES ===")
print(f"Media: {np.mean(datos):.2f}")
print(f"Mediana: {np.median(datos):.2f}")
print(f"Desviación estándar: {np.std(datos):.2f}")
print(f"Varianza: {np.var(datos):.2f}")
print(f"Coeficiente de variación: {(np.std(datos)/np.mean(datos)*100):.2f}%")