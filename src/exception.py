import sys

from src.logger import logging

def error_message_detail(error,error_detail=sys.exc_info()):
    """
    We will call this function whenever an error is raised
    """
    _, _, exc_tb=error_detail
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

    else:
        file_name = "Unknown"
        line_number="Unknown"

    error_message= f"Error occured in python script name [{file_name}] line number [{line_number}] error message[{str(error)}]"

    return error_message



class CustomException(Exception):
    def __init__(self,error_message,error_detail=sys.exc_info()):
        super().__init__(self,error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

    
