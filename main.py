from insurance.logger import logging
from insurance.exception import insuranceException
import os,sys

def test_logger_and_exception():
    try:
        logging.info("Starting point of the test_logger_and_exception")
        result = 3/0
        print(result)
        logging.info("Ending point of the test_logger_and_exception")
    except Exception as e:
        logging.debug(str(e))
        raise insuranceException(e, sys)
    
if __name__ == "__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)