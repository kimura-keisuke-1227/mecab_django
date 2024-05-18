import MeCab

tagger = MeCab.Tagger()
print(tagger.parse("すもももももももものうち").split())
