import logging
import os

FORMAT = '%(asctime)s - (%(name)s) - (%(filename)s:%(lineno)d) - [%(levelname)s] - %(message)s'

class Formatter(logging.Formatter):
    grey = "\x1b[38;20m"
    green = "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = FORMAT
    datefmt = '%d-%b-%y %H:%M:%S'

    FORMATS = {
        logging.DEBUG: f'{grey}{format}{reset}',
        logging.INFO: f'{green}{format}{reset}',
        logging.WARNING: f'{yellow}{format}{reset}',
        logging.ERROR: f'{red}{format}{reset}',
        logging.CRITICAL: f'{bold_red}{format}{reset}',
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

class Logger:
    def __init__(self, file_path='/home/steam/server/logs/py_scripts.log'):            
        self.current_step = 0
        logging.basicConfig(
          level=logging.INFO, 
          filename=file_path,
          format=FORMAT,
        )
        
        logger = logging.getLogger()
        console = logging.StreamHandler()
        
        logger.setLevel(logging.DEBUG)
        console.setLevel(logging.DEBUG)
        console.setFormatter(Formatter())
        logger.addHandler(console)
        

            
    def info(self, message):
      logging.info(message)
      
    def error(self, message):
      logging.error(message)
      
    def warning(self, message):
      logging.warning(message)
      
    def debug(self, message):
      logging.debug(message)
      
    def critical(self, message):
      logging.critical(message)
      
    def exception(self, message):
      logging.exception(message)
    
    def step(self, message):
      self.current_step += 1
      logging.info(f'[{self.current_step}] {message}')