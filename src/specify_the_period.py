'''
jsonファイルにアクセスし整形する
'''

import json
from collections import defaultdict
import text_shaping
from datetime import datetime as dt


def clear_text_list_and_time_list():
    '''
    jsonファイルを取得。
    text_shaping.pyに渡す。
    整形されたテキストlistと
    整形された時間のlistを取得。
    '''
    user_tweets = "@MpYcgEiS8peCbqq.json"
    f = open(user_tweets, "r", encoding="utf-8")

    data = json.load(f)
    clear_text_list = []
    time_list = []

    for v in data.values():
        clear_text = text_shaping.format_text(v)
        if clear_text != "":
            clear_text_list.append(clear_text)
    # print(clear_text_list)

    for k in data.keys():
        temp_time = k.split()[0]
        time_list.append(temp_time)

    return clear_text_list, time_list


def json_to_dict():

    clear_text_list = clear_text_list_and_time_list()[0]
    time_list = clear_text_list_and_time_list()[1]
    # -----------------------------
    time_and_text_dict = defaultdict(list)

    for a in range(len(clear_text_list)):
        time_and_text_dict[time_list[a]].append(clear_text_list[a])

    with open("@MpYcgEiS8peCbqq.json", 'w', encoding="utf-8") as f:
        json.dump(time_and_text_dict, f, indent=2, ensure_ascii=False)

    # print(type(time_and_text_dict))
    # print(time_and_text_dict)

    print("\n以下が取得した期間です")
    print("\n-----------------------------")
    for tatd in time_and_text_dict:
        print(tatd)
    print("\n-----------------------------")

    # for tatd in time_and_text_dict:
    #     # print(time_and_text_dict[tatd])
    #     pass
    # print(time_and_text_dict)

    f = open("@MpYcgEiS8peCbqq.json", "r", encoding="utf-8")
    data = json.load(f)

    time_list = []
    for item in time_and_text_dict:
        tdatetime = dt.strptime(item, '%Y-%m-%d')
        time_list.append(tdatetime)

    print("期間指定の開始日を入力してください。")
    print("例: 2021-08-21")
    from_dt = dt(2021, 9, 19)
    # temp_from_dt = str(input())
    # from_dt = dt.strptime(temp_from_dt, '%Y-%m-%d')

    print("期間指定の終了日を入力してください。")
    print("例: 2021-12-5")
    to_dt = dt(2021, 12, 5)
    # temp_to_dt = str(input())
    # to_dt = dt.strptime(temp_to_dt, '%Y-%m-%d')

    test_time_list = []
    test_text_list = []

    for tar in time_list:
        if from_dt <= tar <= to_dt:
            tstr = tar.strftime('%Y-%m-%d')
            test_time_list.append(tstr)
            # test_text_list

    for tefn in test_time_list:
        for ummm in data[tefn]:
            # print(ummm)
            test_text_list.append(ummm)

    # print(test_text_list)

    return test_text_list


if __name__ == '__main__':
    json_to_dict()
