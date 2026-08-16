from DAO.tanqueDAO import tanqueDAO
from DAO.caracteristicaDAO import caracteristicaDAO

def carga_tanques():
    lista_tanques = tanqueDAO()
    lista_tanques = lista_tanques.obtener_todo()
    return lista_tanques

def carga_caracteristicas():
    lista_caracteristicas = caracteristicaDAO()
    lista_caracteristicas = lista_caracteristicas.obtener_todo()
    return lista_caracteristicas

#############estaría bueno poder filtrar también el tier, nacion, tipo, etc
# No sé si también alterar la base de datos, o simplemente hacer la forma más simple
# Puedo simplificar las cosas así, de la misma manera, podría hacer que los tier, nacion, etc. también sean parte de las características
#también los tipos de cañones
def mostrar_caracteristicas(caracteristicas, caracteristicas_seleccionadas):
  print("Sección características (ys: ya seleccionado):")
  for caracteristica in caracteristicas:
    if caracteristica.nombre in caracteristicas_seleccionadas:
      mensaje = f"{caracteristica.id}. {caracteristica.nombre} (ys)"
    else:
      mensaje = f"{caracteristica.id}. {caracteristica.nombre}"
    if caracteristica.id == 1:
      print("Potencia de fuego:\n\t", end = "")
      caracteres = 4
    elif caracteristica.id == 10:
      print("\nManiobrabilidad:\n\t", end = "")
      caracteres = 4
    elif caracteristica.id == 12:
      print("\nSupervivencia:\n\t", end = "")
      caracteres = 4
    if caracteres + len(mensaje) > 99:
      caracteres = 36
      print("\n\t", end = "")
    else:
      caracteres += 32
    print(mensaje, end = (32 - len(mensaje)) * " ")
  print()

def mostrar_tanques(tanques, tanques_seleccionados, caracteristicas_seleccionadas):
  print("Sección tanques: ", end = "")
  if tanques_seleccionados:
    lista = tanques_seleccionados
    print("\n\t", end = "")
  elif not tanques_seleccionados and caracteristicas_seleccionadas:
    lista = tanques
    print("Ningún tanque cumple con las características seleccionadas", end = "\n\t")
  else:
    lista = tanques
    print("\n\t", end = "")
  caracteres = 4
  for i in range(len(lista)):
    mensaje = f"T{i + 1}. {lista[i].nombre}"
    if caracteres + len(mensaje) > 87:
      caracteres = 32
      print("\n\t", end = "")
    else:
      caracteres += 28
    print(mensaje, end = (26 - len(mensaje)) * " ")
  print()

def eleccion(tanques, tanques_seleccionados, caracteristicas, caracteristicas_seleccionadas):
  respuesta = input('Elección("" o Esc para salir): ')
  if respuesta == "":
    pass
  else:
    try:
      if "T" in respuesta or "t" in respuesta:
        mostrar_tanque(tanques, tanques_seleccionados, respuesta)
        return tanques_seleccionados, caracteristicas_seleccionadas
      else:
        caracteristicas_seleccionadas = seleccionar_caracteristica(caracteristicas,caracteristicas_seleccionadas, respuesta)
        tanques_seleccionados = seleccionar_tanques(tanques, caracteristicas_seleccionadas)
        return tanques_seleccionados, caracteristicas_seleccionadas
    except:
      print("Ingresa un valor válido")
      tanques_seleccionados, caracteristicas_seleccionadas = eleccion(tanques, tanques_seleccionados, caracteristicas, caracteristicas_seleccionadas)

def seleccionar_caracteristica(caracteristicas, caracteristicas_seleccionadas, respuesta): #estaría bueno buscar por nombre
  print(f"Elección: {respuesta}. {caracteristicas[int(respuesta) - 1].nombre}")
  if caracteristicas[int(respuesta) - 1].nombre in caracteristicas_seleccionadas:
    caracteristicas_seleccionadas.remove(caracteristicas[int(respuesta) - 1].nombre)
  else:
    caracteristicas_seleccionadas.append(caracteristicas[int(respuesta) - 1].nombre)
  return caracteristicas_seleccionadas

def seleccionar_tanques(tanques, caracteristicas_seleccionadas):
  tanques_seleccionados = []
  for tanque in tanques:
    cumple_todo = True
    for caracteristica in caracteristicas_seleccionadas:
      if caracteristica not in tanque.caracteristicas:
        cumple_todo = False
        break
    if cumple_todo:
      tanques_seleccionados.append(tanque)
  return tanques_seleccionados

def mostrar_tanque(tanques, tanques_seleccionados, respuesta):
  respuesta = int(respuesta.upper().split("T")[1]) - 1
  if tanques_seleccionados:
    lista = tanques_seleccionados
  else:
    lista = tanques
  lista[respuesta].mostrar_todo()


def main():
    caracteristicas_seleccionadas = []
    tanques_seleccionados = []
    caracteristicas = carga_caracteristicas()
    tanques = carga_tanques()
    while True:
        mostrar_caracteristicas(caracteristicas, caracteristicas_seleccionadas)
        mostrar_tanques(tanques, tanques_seleccionados, caracteristicas_seleccionadas)
        try:
            tanques_seleccionados, caracteristicas_seleccionadas = eleccion(tanques, tanques_seleccionados, caracteristicas, caracteristicas_seleccionadas)
        except:
            break
        
if __name__ == "__main__":
        main()