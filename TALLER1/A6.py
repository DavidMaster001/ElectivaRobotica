#Realice un programa que calcule la fuerza de avance y retroceso de un cilindro neumático de doble
#efecto. Debe establecer previamente los valores de presión, así como las dimensiones físicas del
#cilindro para realizar el cálculo.

def cal_fuerza_ava(presion, diametro_embolo):
    area = (diametro_embolo / 2)**2 * 3.1416  # Área del émbolo en cm^2
    fuerza = presion * area  #Fuerza en gramos
    return fuerza

def cal_fuerza_retro(presion, diametro_embolo, diametro_barra):
    area = (diametro_embolo / 2)**2 * 3.1416  # Área del émbolo en cm^2
    area_barra = (diametro_barra / 2)**2 * 3.1416  # Área de la barra en cm^2
    fuerza = (presion * area) - (presion * area_barra)  # Fuerza en gramos
    return fuerza

# Valores de presión y dimensiones físicas del cilindro
presion = 6  # Presión en kg/cm^2
diametro_embolo = 5  # Diámetro del émbolo en cm
diametro_barra = 2  # Diámetro de la barra en cm

# Cálculo de la fuerza de avance
fuerza_avance = cal_fuerza_ava(presion, diametro_embolo)
print("Fuerza de avance:", fuerza_avance, "gramos")

# Cálculo de la fuerza de retroceso
fuerza_retroceso = cal_fuerza_retro(presion, diametro_embolo, diametro_barra)
print("Fuerza de retroceso: ", fuerza_retroceso, "gramos")
