from logging import getLogger , FileHandler,DEBUG
from logging import Formatter
import datetime
import os

# 時刻関係の処理
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

d = now.strftime('%Y_%m%d_%H%M%S_')


class MyLogger():
    def __init__(self,log_file_name="python"):
        print('create instance MyLogger')
        self.log_file_name = os.path.join('../log',f'{log_file_name}_{d}.log')

        if not (os.path.isdir('../log')):
            os.mkdir('../log')
        
        self.logger = getLogger(__name__)
        self.handler = FileHandler(self.log_file_name)
        self.handler.setLevel(DEBUG)
        self.logger.setLevel(DEBUG)
        self.logger.addHandler(self.handler)
        self.formatter = Formatter('[%(levelname)s]%(asctime)s-[(%(filename)s) %(funcName)s(%(lineno)s)]%(message)s')
        self.handler.setFormatter(self.formatter)
        print(f'log file path:{self.log_file_name}')
    pass

if __name__ =='__main__':
    myLogger = MyLogger('MyLogger')
    logger = myLogger.logger
    logger.debug('test')

