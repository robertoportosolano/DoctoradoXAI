Descripción general del repositorio DoctoradoXAI

El repositorio DoctoradoXAI reúne el conjunto de experimentos, scripts, modelos, documentación y artefactos analíticos desarrollados en el marco de una investigación doctoral orientada a la construcción de un modelo generalizable 
y explicable para sistemas de aprendizaje automático, aplicable tanto a dominios clínicos como no clínicos. Este repositorio constituye la implementación práctica del método descrito en los capítulos centrales de la tesis de Roberto Porto Solano,
estructurado en fases progresivas que permiten avanzar desde la exploración inicial del dataset hasta la obtención de modelos interpretables basados en Curvas de Rashomon y análisis multicriterio. Su propósito principal es operacionalizar 
un proceso riguroso de selección mínima de atributos, validación multidominio y construcción de modelos explicables, garantizando transparencia, reproducibilidad y coherencia metodológica en todas las etapas del experimento.


Propósito central del repositorio

El repositorio tiene como objetivo:

  ✔ Desarrollar un método replicable para identificar el conjunto mínimo de atributos que mantiene un alto rendimiento predictivo.
  
  Se integran 13 métricas estadísticas, de información y reglas simples para construir un ranking robusto de importancia de características.
  
  ✔ Construir modelos explicables sin sacrificar precisión.
  
  Mediante análisis de complejidad, poda, reducción de atributos y curvas de Pareto.
  
  ✔ Validar la estabilidad del método en múltiples dominios temáticos.
  
  Incluye experimentos clínicos (Statlog Heart Disease) y otros 6 dominios adicionales que permiten verificar la transferibilidad.
  
  ✔ Implementar Curvas de Rashomon para evidenciar la coexistencia de modelos equivalentes, priorizando simplicidad estructural.
  
  ✔ Documentar y almacenar todo el proceso: código, experimentos, tablas, figuras, resultados y artefactos metodológicos.


De esta manera, DoctoradoXAI es, simultáneamente:

Un repositorio de código
Un repositorio de experimentos
Un laboratorio de investigación explicable
Un sistema base para futuros estudios de XAI
