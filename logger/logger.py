# take input string and varible to print in consistent manner
import os 
import logging
import logging.handlers
import time
logger = logging.getLogger("")
logger.setLevel(logging.INFO)

def logging_data(module_name,input_string_key,values):
    directory = os.path.dirname(os.getcwd())
    os. makedirs(f"{directory}/Logs", exist_ok=True)

    path = f"{directory}/Logs/{module_name}"
    os.makedirs(path , exist_ok =True)
    print(path)

    f_handler = logging.handlers.RotatingFileHandler(f"{path}/{module_name}_logs.log", maxBytes=(1048576 * 10),backupCount=5)
    f_format = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    logging.info(f'{input_string_key}:-{values}')
    
    
