import MeCab
# from MyMecab import MyMecab
import docx
import sys
import argparse
import json,os

str_key_base_text = 'word'
str_key_ruby_text = 'ruby'
str_key_end_of_line = 'end_of_line'

# 親階層配下の他モジュールをインポートできるようにする
sys.path.append('../')
from MyLogger.MyLogger import MyLogger

class WordRubyFromText:
    const_str_dir_for_output = 'output'
    const_str_dir_for_output_excel = 'excelForEdit'
    const_str_dir_for_input = 'input'
    const_str_extension_word = '.docx'
    const_str_extension_excel = '.xlsx'
    const_str_extension_text = '.txt'
    const_dict_end_of_line = {
        str_key_end_of_line: 1
    }
    
    def __init__(self) -> None:
        self.logger = MyLogger().logger
        self.logger.info('test')

    def test(self):
        self.logger.info("Test Start")
        self.logger.info("Test End")

    def main(self,input_file_name,output_file_name):
        self.logger.info(f'main start! output_text_file_name:{output_file_name} input_file_name:{input_file_name}')

        # 日本語解析用インスタンスを生成
        # self.logger.info('create MyMecab instance')
        # my_mecab = MyMecab(self.logger)

        # Wordファイルインスタンスを生成
        # self.logger.info('create docx.Document instance')
        # document = docx.Document()
        
        # Excel出力用のJSON
        list_of_json_for_line = []
        
        # ファイルを読み込んで１行ずつ処理する
        input_text_file_path = os.path.join(self.const_str_dir_for_input,input_file_name + self.const_str_extension_text)
        self.logger.info(f'read input text file:{input_text_file_path}')
        
        try:
            self.logger.info(f'try to open file:{input_text_file_path}')
            with open(input_text_file_path) as f:
                for line in f:
                    self.logger.info(f'Begin the operation for line:{line}')
        except Exception as e:
            self.logger.error(f"{e.__class__.__name__}: {e}")
            print(f"{e.__class__.__name__}: {e}")
            return
        
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