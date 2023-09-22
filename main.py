import sqlite3

def menu():
    print("¿Qué desea hacer?")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Introduzca una opción: ")
    return opcion
  
def validar_tabla_usuarios_existe(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='usuarios'")
    resultados = cursor.fetchall()

    if len(resultados) == 1:
        return True
    else:
        return False

def validar_inicio_sesion(conn, usuario, clave):

    # Ejecutamos la consulta SQL
    cursor = conn.cursor()
    cursor.execute("SELECT usuario, clave FROM usuarios WHERE usuario = ? AND clave = ?", (usuario, clave))

    # Obtenemos los resultados
    resultados = cursor.fetchall()

    # Validamos si los datos son correctos
    if len(resultados) == 1:
        return True
    else:
        return False

def inicio_sesion(conn):
    # Solicitamos el nombre de usuario y la contraseña
    usuario = input("Introduce tu nombre de usuario: ")
    clave = input("Introduce tu contraseña: ")

    # Validamos los datos de inicio de sesión
    if validar_inicio_sesion(conn, usuario, clave):
        # Inicio de sesión correcto
        print("Inicio de sesión correcto.")
        return True
    else:
      # Inicio de sesión incorrecto
      print("Inicio de sesión incorrecto.")
      return False

def registrar_usuario(conn):
    # Solicitamos el nombre de usuario y la contraseña
    usuario = input("Introduce tu nombre de usuario: ")
    clave = input("Introduce tu contraseña: ")

    # Insertamos el nuevo usuario en la base de datos
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (usuario, clave) VALUES (?, ?)", (usuario, clave))
    conn.commit()
    # Mostramos un mensaje de confirmación
    print("Registro correcto.")
    return True

# Creamos una base de datos llamada "login.db"
conn = sqlite3.connect("login.db")

# Validamos si la tabla usuarios existe
if validar_tabla_usuarios_existe(conn):
    #print("La tabla usuarios existe.")
    tablaExiste = 1
else:
  # Creamos una tabla llamada "usuarios"
  conn.execute("CREATE TABLE usuarios (usuario TEXT, clave TEXT)")

# Ejecutamos el menú
while True:
    opcion = menu()

    # Iniciamos sesión
    if opcion == "1":
        if inicio_sesion(conn):
            break

    # Registramos un usuario
    elif opcion == "2":
        if registrar_usuario(conn):
            if inicio_sesion(conn):
              break

    # Salir
    elif opcion == "3":
          break

# Cerramos la conexión
conn.close()