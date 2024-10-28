from src.modulos import entrada_de_datos, previsionjes_de_depreciacion, salida_de_datos

costo_inicial, valor_final, vida_util = entrada_de_datos()
resultados = previsiones_de_depreciacion(costo_inicial, valor_final, vida_util)
salida_de_datos(resultados)