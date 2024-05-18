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
        
    def main(self,input_file_name,output_file_name):
        self.logger.info(f'main start! output_text_file_name:{output_file_name} input_file_name:{input_file_name}')
        
        # 日本語解析用インスタンスを生成
        self.logger.info('create MyMecab instance')
        my_mecab = MyMecab(self.logger)
                
        self.test()
        self.logger.info("main End")

if __name__ == "__main__":
    print('WordRubyFromText Program Start!')
    psr = argparse.ArgumentParser(
        prog='ルビ入りWordファイル作成プログラム',
        usage='コマンドラインから引数を指定して実行',
        description='テキストファイルからルビが入ったWordファイルを自動で作成'
    )
    psr.add_argument('-i', '--input', required=True,help='インプットファイル名(拡張子はつけない)')
    psr.add_argument('-o', '--output', required=True,help='アウトプットファイル名(拡張子はつけない)')

    args = psr.parse_args()
    
    input_file_name = args.input
    output_file_name = args.output

    instance = WordRubyFromText()
    instance.main(input_file_name,output_file_name)
    print('WordRubyFromText Program End!')