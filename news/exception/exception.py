import sys

class NewsException(Exception):
    def __init__(self, message,error_details:sys):
        self.message = message
        _,_,exc_tb=error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file = exc_tb.tb_frame.f_code.co_filename
    def __str__(self):
        return 'Error Occured in Python Script Name  [{}]  line number [{}] error message [{}]'.format(self.file,self.lineno, self.message)

if __name__ == '__main__':
    try:
        a=1/0
    except Exception as e:
        raise NewsException(e,sys)