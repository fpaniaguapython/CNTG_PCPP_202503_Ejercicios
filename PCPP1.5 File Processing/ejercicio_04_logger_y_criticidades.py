import logging
logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

otro_logger = logging.getLogger('mi')
otro_logger.setLevel(logging.INFO)

mi_logger = logging.getLogger('mi.logger')
# Ejecutar con la línea comentada y descomentada
mi_logger.setLevel(logging.ERROR)

# logger.critical('Your CRITICAL message')
# logger.error('Your ERROR message')
# logger.warning('Your WARNING message')
# logger.info('Your INFO message')
# logger.debug('Your DEBUG message')
mi_logger.critical('Your CRITICAL message')
mi_logger.error('Your ERROR message')
mi_logger.warning('Your WARNING message')
mi_logger.info('Your INFO message')
mi_logger.debug('Your DEBUG message')