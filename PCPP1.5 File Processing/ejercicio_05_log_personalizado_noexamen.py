import logging

# Clase que realiza la gestión del log
class CustomHandler(logging.Handler):
    # Método ejecutado al hacer el log
    def emit(self, record : logging.LogRecord):
        print(f'Registro: {record.msg}')

logger = logging.getLogger('MiApp')

custom_handler = CustomHandler()
custom_handler.setLevel(logging.ERROR)

# Filter determina si el log se realiza o no
custom_handler.addFilter(filter=lambda record : record.msg.endswith('*'))

logger.addHandler(custom_handler)

logger.error(msg='1. Este mensaje SÍ se escribe*')
logger.info(msg='2. Este mensaje NO se escribe*')
logger.critical(msg='3. Este mensaje NO se escribe')
logger.critical(msg='4. Este mensaje SÍ se escribe*')