import MeCab
import jaconv
import re,sys
import json
import MyLogger
# from RubyDictJsonMaker import RubyDictJsonMaker
# from MyRubyTools import MyRubyTools

column_text = 'word'
column_kana = 'ruby'
column_type1 = 'type1'
column_type2 = 'type2'
column_is_end_of_line = 'end_of_line'

const_int_new_line = 1
const_int_NOT_new_line = 0

int_index_text = 0
int_index_type1 = 1
int_index_type2 = 2
int_index_kana = 8
sample_input_text = '''パーティのお返事お待ちしております。毎日食事補助必要。お申込ありがとうございます。'''

class MyMecab:
    def __init__(self, logger):
        print('initialize MyMecab!')
        self.logger = logger
        # self.myRubyTools = MyRubyTools(logger)
        # self.rubyDictJsonMaker = RubyDictJsonMaker()
        # 初期化の段階で辞書を取得しておく
        # self.dictionary = self.rubyDictJsonMaker.get_dict_of_words()
        # self.logger.info('initialize MyMecab!')
        pass
    
    def get_ruby_list_from_text_in_line(self, input_text):
        self.logger.debug(f'{sys._getframe().f_code.co_name} start!')
        # list_of_column = [column_text,column_kana,column_type]
        mecab = MeCab.Tagger()  # MeCabオブジェクトを作成
        malist = mecab.parse(input_text).split('\n')  # 形態素解析を行う
        
        list_of_line_data = []
        
        # 形態解析の１つの要素ごとの処理
        for row in malist:
            # self.logger.info('Row::')
            word_list_in_row = row.replace(',', '\t').split('\t')
            
            
            if len(word_list_in_row) < 3:
                continue
            
            # よみがなとひらがな文字を取り出す
            yomigana = jaconv.kata2hira(word_list_in_row[int_index_kana])
            hira_text = jaconv.kata2hira(word_list_in_row[int_index_text])

            if hira_text in self.dictionary:
                word_dict = self.dictionary[hira_text]
                for kanji_in_dict in word_dict:

                    data = {
                        column_is_end_of_line: const_int_NOT_new_line,
                        column_text: kanji_in_dict['漢字'],
                        column_kana: kanji_in_dict['よみがな'],
                    }
                    list_of_line_data.append(data)
                continue
            print(f'word_list_in_row:{word_list_in_row}')
            self.logger.info(f'word_list_in_row:{word_list_in_row}')
            # ひらがなの場合、読み仮名を空欄に
            if yomigana == hira_text:
                self.logger.info(' row is HIRAGANA. No Yomigana!')
                yomigana = ''
                data = {

                    column_is_end_of_line: const_int_NOT_new_line,
                    column_text: word_list_in_row[int_index_text],
                    column_kana: yomigana,
                }

                list_of_line_data.append(data)
            # 漢字の場合は分割してルビをふる
            else:
                self.logger.info(' row is KANJI. Adding Yomigana!')
                dict_list_kanji_and_ruby = self.myRubyTools.separate_kanji_hiragana(hira_text,yomigana)
                self.logger.debug(f'dict_list_kanji_and_ruby:{dict_list_kanji_and_ruby}')

                # 長いので変数に入れておく
                kanji_in_list = dict_list_kanji_and_ruby[self.myRubyTools.key_kanji_list][0]
                ruby_in_list  = dict_list_kanji_and_ruby[self.myRubyTools.key_list_ruby][0]

                self.logger.debug(f'Search in the dictionary, with {kanji_in_list}')

                if kanji_in_list in self.dictionary:
                    self.logger.info(f'Word [{kanji_in_list}] Existing_in_the_ dictionary!')
                    print(kanji_in_list , ruby_in_list)

                self.logger.info(f'get_separated_kana_kanji_ruby (kanji_in_list:{kanji_in_list})')
                dict_list_kanji_and_ruby = self.myRubyTools.get_separated_kana_kanji_ruby(dict_list_kanji_and_ruby[self.myRubyTools.key_kanji_list], dict_list_kanji_and_ruby[self.myRubyTools.key_list_ruby])

                self.logger.debug(dict_list_kanji_and_ruby)

                for kanji, ruby in zip(dict_list_kanji_and_ruby[self.myRubyTools.key_kanji_list],dict_list_kanji_and_ruby[self.myRubyTools.key_list_ruby]):
                    self.logger.info(f'data kanji:{kanji} , ruby:{ruby}')
                    data = {
                        column_is_end_of_line: const_int_NOT_new_line,
                        column_text: kanji,
                        column_kana: ruby,
                    }
                    list_of_line_data.append(data)

        data = {column_is_end_of_line: const_int_new_line}
        list_of_line_data.append(data)
        # print(list_of_line_data)
        self.logger.debug(f'list_of_line_data:{list_of_line_data}')
        
        self.logger.debug(f'{sys._getframe().f_code.co_name} end!')
        return list_of_line_data    