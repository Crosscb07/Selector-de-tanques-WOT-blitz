from conexion import Conexion
from modelos.caracteristica import caracteristica

class caracteristicaDAO:
  def __init__(self):
    conexion = Conexion()
    self.conexion = conexion.obtener_conexion()
  def obtener_todo(self):
    cursor = self.conexion.cursor()
    sql = "SELECT * FROM caracteristicas"
    cursor.execute(sql)
    lista = []
    for i in cursor.fetchall():
      caracteristica_1 = caracteristica(i[0], i[1])
      lista.append(caracteristica_1)
    self.conexion.close()
    return lista