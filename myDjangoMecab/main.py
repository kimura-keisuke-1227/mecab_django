import MeCab
import sys

# 親階層配下の他モジュールをインポートできるようにする
sys.path.append('../')
from MyLogger.MyLogger import MyLogger

logger = MyLogger().logger
logger.info('test')
