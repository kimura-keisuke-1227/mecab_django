import MeCab
import sys
import argparse

# 親階層配下の他モジュールをインポートできるようにする
sys.path.append('../')
from MyLogger.MyLogger import MyLogger

class WordRubyFromText:
    def __init__(self) -> None:
        self.logger = MyLogger().logger
        self.logger.info('test')
    
    def test(self):
        self.logger.info("Test Start")
        self.logger.info("Test End")
        
    def main(self):
        self.logger.info("main Start")
        self.test()
        self.logger.info("main End")

if __name__ == "__main__":
	print('WordRubyFromText Program Start!')
	psr = argparse.ArgumentParser(
        prog='ルビ入りWordファイル作成プログラム',
        usage='コマンドラインから引数を指定して実行',
        description='テキストファイルからルビが入ったWordファイルを自動で作成'
    )
	instance = WordRubyFromText()
	instance.main()
	print('WordRubyFromText Program End!')