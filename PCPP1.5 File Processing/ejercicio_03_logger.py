import logging

logging.basicConfig()

logger = logging.getLogger()
hello_logger = logging.getLogger('hello')
hello_world_logger = logging.getLogger('hello.world')
recommended_logger = logging.getLogger(__name__)

hello_logger.debug('Debug')
hello_logger.critical('Error Critical')