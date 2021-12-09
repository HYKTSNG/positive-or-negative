'''
textを使いやすいようにする。
'''

import re
import MeCab

tagger = MeCab.Tagger()


def format_text(normal_text):

    # re.sub や re.split を使い邪魔なものの削除
    normal_text = re.sub(' ', '　', normal_text)
    normal_text = re.sub('#', '　', normal_text)
    # @usernameを除去
    normal_text = re.sub("(@[A-Za-z0-9_:]+)", "　", normal_text)
    # URL情報の削除
    normal_text = re.sub(
        r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+$,%#]+)", "　",
        normal_text)
    # 改行文字削除
    normal_text = re.sub('\n', " ", normal_text)
    # 記号系削除
    normal_text = re.sub(
        '[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^＾_`’～{|}~ '
        '「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]', "　", normal_text)
    normal_text = re.sub("(ー)\\1", "　", normal_text)
    # 連続した文字の削除
    normal_text = re.sub("([ぁ-ん])\\1", "　", normal_text)
    # アルファベット削除
    normal_text = re.sub("([A-Za-z0-9ａ-ｚＡ-Ｚ０-９])", "　", normal_text)
    # normal_text = re.sub("([_:])", "", normal_text)

    # 全角スペースの削除
    normal_text = re.sub("　", " ", normal_text)

    # print(normal_text)
    return normal_text
