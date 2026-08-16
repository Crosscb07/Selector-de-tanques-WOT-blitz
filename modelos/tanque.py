class tanque:
  def __init__(self, id, nombre, nacion, clase, tier, tipo, caracteristicas):
    self.id = id
    self.nombre = nombre
    self.nacion = nacion
    self.clase = clase
    self.tier = tier
    self.tipo = tipo
    self.caracteristicas = caracteristicas
  def agregar_caracteristicas(self, nombre):
    self.caracteristicas.append(nombre)
  def mostrar_todo(self):
    print(f"Id: {self.id}")
    print(f"Nombre: {self.nombre}")
    print(f"Nación: {self.nacion}")
    print(f"Clase: {self.clase}")
    print(f"Tier: {self.tier}")
    print(f"Tipo: {self.tipo}")
    print(f"Características:")
    for i in self.caracteristicas:
      print(i)