import sys,os

def error_message_detail(error, erroe_detail:sys):
    _, _, exc_tb = erroe_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format():
        file_name ,exc_tb.tb_lineno, str(error)
    )

    return error_message




class SensorException(Exception):

    def __init__(self, error_message, erroe_detail:sys):

