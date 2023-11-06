import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s][%(levelname)s][%(message)s]', datefmt='%Y-%m-%d %I:%M:%S %p')

def info(msg):
    logging.info(msg)

def warning(msg):
    logging.warning(msg)

def debug(msg):
    logging.debug(msg)

def error(msg):
    logging.error(msg)
