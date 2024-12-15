import sys  
from logger import logging
#It will provide various function and variables that are used to manipulate different parts of python runtime environment
#Basically it gives access to the system as well as variable related information
# sys.version -> Python Version  sys.argv -> List of arguments passed to the particular script
# sys.exit all code above this will run and below will not execute.

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
# This info will give all the information on which file the exception has occured and on which line number error has occured.
    error_message="Error has occured in python script name [{0}] line number [{1}] and error message is [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message
    
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str(self):
        return self.error_message



if __name__ == '__main__':
    try:
        a=1/0
    except Exception as e:
        
        logging.info('Exception')
        raise CustomException(e,sys)