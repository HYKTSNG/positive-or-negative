'''
jsonファイルにアクセスし整形する
'''

import json
from collections import defaultdict
import text_shaping
from datetime import datetime as dt


def clear_text_list_and_time_list(screen_name):
    '''
    全期間
    '''

    f = open(screen_name + ".json", "r", encoding="utf-8")
    data = json.load(f)
    clear_text_list = []
    time_list = []

    for v in data.values():
        clear_text = text_shaping.format_text(v)
        if clear_text != "":
            clear_text_list.append(clear_text)

    for k in data.keys():
        temp_time = k.split()[0]
        time_list.append(temp_time)

    return clear_text_list, time_list, screen_name


def fnc_screen_name():

    print("screen_nameを入力してください")
    screen_name = str(input())
    return screen_name


def json_to_dict(screen_name):

    clear_text_list = clear_text_list_and_time_list(screen_name)[0]
    time_list = clear_text_list_and_time_list(screen_name)[1]
    # -----------------------------
    time_and_text_dict = defaultdict(list)

    for a in range(len(clear_text_list)):
        time_and_text_dict[time_list[a]].append(clear_text_list[a])

    # 下のコードでjsonの上書きができる。
    with open(screen_name + ".json", 'w', encoding="utf-8") as f:
        json.dump(time_and_text_dict, f, indent=2, ensure_ascii=False)

    print("\n以下が取得した期間です")
    print("\n-----------------------------")
    for tatd in time_and_text_dict:
        print(tatd, " ツイート数: ", len(time_and_text_dict[tatd]))
    print("\n-----------------------------")

    f = open(screen_name + ".json", "r", encoding="utf-8")
    data = json.load(f)

    time_list = []
    for item in time_and_text_dict:
        tdatetime = dt.strptime(item, '%Y-%m-%d')
        time_list.append(tdatetime)

    print("期間指定の開始日を入力してください。")
    print("例: 2021-08-21")
    # from_dt = dt(2021, 9, 19)
    temp_from_dt = str(input())
    from_dt = dt.strptime(temp_from_dt, '%Y-%m-%d')

    print("期間指定の終了日を入力してください。")
    print("例: 2021-12-5")
    # to_dt = dt(2021, 11, 9)
    temp_to_dt = str(input())
    to_dt = dt.strptime(temp_to_dt, '%Y-%m-%d')

    test_time_list = []
    test_text_list = []

    for tar in time_list:
        if from_dt <= tar <= to_dt:
            tstr = tar.strftime('%Y-%m-%d')
            test_time_list.append(tstr)

    for tefn in test_time_list:
        for ummm in data[tefn]:
            test_text_list.append(ummm)

    return test_text_list
