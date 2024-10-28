#MODULO 1
def entrada_de_datos():
    costo_inicial = int(input("INGRESA EL COSTO INICIAL: "))
    valor_final = int(input("INGRESA EL VALOR FINAL: "))
    vida_util = int (input("INGRESA LA VIDA UTIL: "))
    return costo_inicial, valor_final, vida_util

#MODULO 2
def previsiones_de_depreciacion(costo_inicial, valor_final, vida_util):
    resultados = [ ]
    depreciacion = (costo_inicial - valor_final)/ vida_util
    acumulada = 0
    
    for valor_año in range (1, vida_util + 1):
        acumulada += depreciacion
        valor_actual = costo_inicial - acumulada
        resultados.apped((valor_año, 2005 + valor_año, depreciacion, acumulada, valor_actual))
        
        return resultados
    
#MODULO 3
def salida_de_datos(resultados):
    for r in resultados:
        print(f"| {r[0]} ({r[1]}) | {r[2]:.2f} | {r[3]:.2f} | {r[4]:.2f} |")