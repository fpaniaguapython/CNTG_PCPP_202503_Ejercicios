import shelve

# Proceso de escritura
fichero_persistencia = shelve.open('datos.shlv', flag='c') # Abrir para lectura y escritura, crea si no existe

fichero_persistencia['Zamora']='Castilla y Leon'
fichero_persistencia['Cáceres']='Extremadura'
fichero_persistencia['Lugo']='Galicia'

fichero_persistencia.close()

# Proceso de lectura
fichero_persistencia = shelve.open('datos.shlv', flag='c')

print(fichero_persistencia['Cáceres'])
fichero_persistencia['Cáceres']='Comunidad de Madrid'
print(fichero_persistencia['Cáceres'])

fichero_persistencia.close()

