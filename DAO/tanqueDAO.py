from conexion import Conexion
from modelos.tanque import tanque

class tanqueDAO:
  def __init__(self):
    conexion = Conexion()
    self.conexion = conexion.obtener_conexion()
  def obtener_todo(self):
    cursor = self.conexion.cursor()
    sql = "SELECT * FROM tanques"
    cursor.execute(sql)
    variable = cursor.fetchall()
    lista = []
    for fila in variable:
      sql = "SELECT caracteristicas.nombre FROM tanques_caracteristicas JOIN caracteristicas ON caracteristicas.id = tanques_caracteristicas.caracteristica_id WHERE tanque_id = %s;"
      valores = [fila[0]]
      cursor.execute(sql, valores)
      caracteristicas = []
      for i in cursor.fetchall():
        caracteristicas.append(i[0])
      tanque_1 = tanque(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], caracteristicas)
      lista.append(tanque_1)
    self.conexion.close()
    return lista
  def insertar_tanques_web(self):
    try:
      mensaje_tanque, mensaje_caracteristica = ingresar_tanques_caracteristicas()
      cursor = self.conexion.cursor()
      cursor.execute(mensaje_tanque)
      print("Código ejecutado en MySQL:")
      for i in mensaje_caracteristica:
        cursor.execute(i)
        print(i)
      self.conexion.commit()
      self.conexion.close()
    except Exception as e:
      self.conexion.rollback()
      print("Error:", e)
  '''def insertar(self, tanque):
    cursor = self.conexion.cursor()
    sql = "INSERT INTO tanques(nombre, nacion, clase, tier, tipo) VALUES(%s, %s, %s, %s, %s)"
    valores = (
            tanque.nombre,
            tanque.nacion,
            tanque.clase,
            tanque.tier,
            tanque.tipo
        )
    cursor.execute(sql, valores)
    self.conexion.commit()
    print("Tanque insertado")'''
  '''def actualizar(self, tanque):
      cursor = self.conexion.cursor()
      sql = "UPDATE tanques SET nombre=%s, nacion=%s, clase=%s, tier=%s, tipo=%s WHERE id=%s"
      valores = (
            tanque.nombre,
            tanque.nacion,
            tanque.clase,
            tanque.tier,
            tanque.tipo,
            tanque.id
        )
      cursor.execute(sql, valores)
      self.conexion.commit()
      print("Tanque insertado")'''
  '''def eliminar(self, id):
    cursor = self.conexion.cursor()
    # primero eliminar relaciones
    sql_relaciones = "DELETE FROM tanques_caracteristicass WHERE tanque_id = %s"
    cursor.execute(sql_relaciones, (id,))
    # luego eliminar tanque
    sql_tanque = "DELETE FROM tanques WHERE id = %s"
    cursor.execute(sql_tanque, (id,))
    self.conexion.commit()
    print("Tanque eliminado")'''

def ingresar_tanques_caracteristicas(): # Esta función permite ingresar los tanques y sus características en la base de datos
    nombre = input("Nombre: ") # Pide al usuario que ingrese el nombre del tanque
    variable = input("Paste: ") # Pide al usuario que pegue la información del tanque desde la web
    # Determina la nación del tanque
    if "U.S.A." in variable:
        nacion = "Estados Unidos"
    elif "Germany" in variable:
        nacion = "Alemania"
    elif "U.S.S.R." in variable:
        nacion = "Unión Soviética"
    elif "U.K." in variable:
        nacion = "Reino Unido"
    elif "Japan" in variable:
        nacion = "Japón"
    elif "China" in variable:
        nacion = "China"
    elif "France" in variable:
        nacion = "Francia"
    elif "European Nation" in variable:
        nacion = "Nación Europea"
    elif "Hybrid Nation" in variable:
        nacion = "Nación Híbrida"

    # Determina la clase del tanque
    hola = variable.split("Class ")[1].split(" Tier")[0]
    if "Light" == hola:
        clase = "Ligero"
    elif "Medium" == hola:
        clase = "Medio"
    elif "Heavy" == hola:
        clase = "Pesado"
    elif "TD" == hola:
        clase = "Destructor"

    # Determina el tipo del tanque
    if "Tech tree" in variable:
        tipo = "Árbol tecnológico"
    elif "Collector" in variable:
        tipo = "Coleccionista"
    elif "Premium" in variable:
        tipo = "Premium"

    id = variable.split("DEV: ID ")[1].split("DEV: NAME")[0] # Determina el id del tanque
    tier = variable.split("Tier ")[2].split(" Type")[0] # Determina el tier del tanque

    #-----------------------------------------------------------------------

    # Según el tipo de cañón del tanque, la información pegada desde la web se encuentra en diferentes posiciones, por lo que se crean listas con las posiciones de las características
    caracteristicas = []
    if "Gun type Regular" in variable:
        caracteristicas.append(1)
        lista = [1, 6, 17, 66, [75, 80, 86, 92], 110, [143, 148], [212, 217, 222], 258, 270, [279, 284, 289, 294]]
    elif "Gun type Auto loader" in variable:
        caracteristicas.append(2)
        lista = [1, 6, 23, 82, [91, 96, 102, 108], 126, [159, 164], [228, 233, 238], 274, 286, [295, 300, 305, 310]]
    elif "Gun type Auto reloader" in variable:
        caracteristicas.append(3)
        lista = [1, 6, 23, 98, [107, 112, 118, 124], 142, [175, 180], [244, 249, 254], 290, 302, [311, 316, 321, 326]]

    caracteristica = 3
    variable = variable.split(" DPM ")[1].split(" ") # Se separa la cadena de información del tanque en una lista, para poder utilizar los índices de las características
    for i in lista:
        caracteristica += 1
        try: # Existen características que se juzgan con un solo parámetro
            if int(variable [i]) / int(variable[i + 2]) <= 1/3: # La información viene de la siguiente manera: x / y, donde y es la cantidad de tanques de la misma clase y tier, y x es la posición del tanque respecto a los demás tanques
                caracteristicas.append(caracteristica)
        except TypeError: # Existen características que se juzgan con varios parámetros
            dividendo = 0
            divisor = 0
            for j in i:
                dividendo += int(variable [j])
                divisor += int(variable [j + 2])
            if dividendo / divisor <= 1/3: # Si la característica del tanque se encuentra en el 33% mejor de los tanques, se agrega a la lista de características del tanque
                caracteristicas.append(caracteristica)
    # Esto ya es subjetivo, si el usuario cree que el tanque tiene una buena torreta, puede agregarla como característica, lo mismo con el casco
    if input("Torreta: ") != "": 
        caracteristicas.append(15)
    if input("Casco: ") != "":
        caracteristicas.append(16)

    mensaje_tanque = f'INSERT INTO tanques (id, nombre , nacion, clase, tier, tipo) VALUES ({id}, "{nombre}", "{nacion}", "{clase}", "{tier}", "{tipo}");' # Se crea el mensaje para ingresar el tanque en MySQLWorkbench
    mensaje_caracteristica = [] # Se crea la lista de mensajes para ingresar las características del tanque en MySQLWorkbench

    for i in caracteristicas:
        mensaje_caracteristica.append(f'INSERT INTO tanques_caracteristicas (tanque_id, caracteristica_id) VALUES ({id}, {i});')

    return mensaje_tanque, mensaje_caracteristica # Se devuelve el mensaje para que tanqueDAO pueda ingresar el tanque y sus características en la base de datos
