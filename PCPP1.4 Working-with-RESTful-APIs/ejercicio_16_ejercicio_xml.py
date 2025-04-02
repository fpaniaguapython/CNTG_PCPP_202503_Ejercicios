# Crear una película y agregarla a ejercicio_16.xml
# Título
# Director
# Genero
# Guardar a fichero para comprobar el resultado
import xml.etree.ElementTree

# Leyendo el documento y haciendo un parse 
tree = xml.etree.ElementTree.parse('ejercicio_16.xml')
# Obtener el elemento raíz
peliculas = tree.getroot()
# Construimos el nuevo elemento
nueva_pelicula = xml.etree.ElementTree.Element('pelicula')
# Asignamos subelementos al elemento nuevo
xml.etree.ElementTree.SubElement(nueva_pelicula, 'titulo').text = 'Tiburón'
xml.etree.ElementTree.SubElement(nueva_pelicula, 'director').text = 'Steven Spielberg'
xml.etree.ElementTree.SubElement(nueva_pelicula, 'genero').text = 'Terror'
# Vinculamos el elemento nuevo al elemento raíz
peliculas.append(nueva_pelicula)
xml.etree.ElementTree.indent(tree, space="  ", level=0)
tree.write('videoteca.xml', method='')