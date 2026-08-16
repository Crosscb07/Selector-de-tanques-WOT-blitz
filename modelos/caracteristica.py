class caracteristica:
  def __init__(self, id, nombre):
    self.id = id
    self.nombre = nombre
  def mostrar_todo(self):
    print(f"Id: {self.id}")
    print(f"Nombre: {self.nombre}")