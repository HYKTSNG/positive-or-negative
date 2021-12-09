'''
return list でjudge.pyに渡す
'''

import MeCab
import os
import specify_the_period

tagger = MeCab.Tagger()


def analysis_json():

    files = os.listdir()
    # print(files)
    files_in = [s for s in files if ".json" in s]

    print("どのユーザーを判定しますか？")
    print("現在取得済みのユーザー　一覧です↓↓")
    print(files_in, "\n")
    print("screen_nameを入力してください")
    # screen_name = str(input())
    screen_name = "@MpYcgEiS8peCbqq"
    print("screen_nameは、", screen_name, " ですね")
    print("期間指定はしますか？")
    print("y/n でお願いします。")
    # y_or_n = str(input())
    y_or_n = "y"

    # 期間指定がない場合
    if y_or_n == "n":
        clear_text_list = specify_the_period.clear_text_list_and_time_list()[0]
        print(clear_text_list)

    # 期間指定がある場合
    elif y_or_n == "y":
        # ---期間指定できるようにする---
        time_and_text_dict = specify_the_period.json_to_dict()
        print(time_and_text_dict)

    # y_or_n がy/nでもない場合
    else:
        print("y/n 以外の文字なため全期間で表示します")
        clear_text_list = specify_the_period.clear_text_list_and_time_list()[0]
        print(clear_text_list)

    # print(specify_the_period.json_to_dict())
    return


if __name__ == '__main__':
    analysis_json()
