import logging
from datetime import datetime

def CustomLog(log_file, log_level, log_text):
    logger = logging.getLogger('customlog')

    # Check if handler already exist
    if not logger.handlers:
        logger.setLevel(logging.DEBUG) # Set min threshold log level
        handler = logging.FileHandler(f'{log_file}_.log') # Generic log file
        #handler = logging.FileHandler(datetime.now().strftime(f'{log_file}_%d_%m_%Y.log')) # Single day log file
        formatter = logging.Formatter(fmt='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    else:
        pass
    
    # Check log's level
    if log_level in ['debug', 'DEBUG']:
        logger.debug(log_text)
    elif log_level in ['info', 'INFO']:
        logger.info(log_text)
    elif log_level in ['warning', 'WARNING']:
        logger.warning(log_text)
    elif log_level in ['critical', 'CRITICAL']:
        logger.critical(log_text)
    elif log_level in ['error', 'ERROR']:
        logger.error(log_text)
