import shelve

# NOTA: Este ejercicio incluye solo la funcionalidad básica 
# En el ejercicio 065 está expuesta más funcionalidad

# Apertura
# flag='c' -> Abrir para lectura y escritura, crea si no existe
fichero_persistencia = shelve.open('datos.shlv', flag='c') 

# Escritura
fichero_persistencia['Zamora']='Castilla y Leon'
fichero_persistencia['Cáceres']='Extremadura'
fichero_persistencia['Lugo']='Galicia'

# Lectura
print(fichero_persistencia['Cáceres'])

# Modificación
fichero_persistencia['Cáceres']='Comunidad de Madrid'
print(fichero_persistencia['Cáceres'])

# Cierre
fichero_persistencia.close()

